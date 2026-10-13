---
doc_id: run-service-identity
title: Introduction to service identity
url: https://docs.cloud.google.com/run/docs/securing/service-identity
category: security
fetched_at: '2026-10-13T15:13:49+00:00'
license: CC BY 4.0 (Google Cloud documentation)
---

This page describes the two Cloud Run identities and how the
Cloud Client Libraries use the service identity to call Google Cloud APIs. Examples
of Google Cloud products that have Cloud Client Libraries include
Cloud Storage, Firestore, Cloud SQL, Pub/Sub, and
Cloud Tasks. This page is for admins, operators, or developers who
manage organization policies and user access, or anyone who would like to learn
about such topics.

## Cloud Run identities

To use Cloud Run, Google Cloud requires two types of
identities with the appropriate permissions:

- **Cloud Run deployer account**: The identity (either a user
  account or service account) that you use to deploy and manage a
  Cloud Run resource by making requests to the
  Cloud Run Admin API.
- **Cloud Run service identity**: The identity (a service
  account) that the Cloud Run instance uses. When the
  Cloud Run code you wrote interacts with
  Cloud Client Libraries, or calls another Cloud Run service
  for service-to-service communication,
  you use this identity to make requests from Cloud Run to
  Google Cloud APIs or other Cloud Run services.

To access and make requests to the Google Cloud APIs or
communicate between services, each identity must have the appropriate
permissions granted to them in Identity and Access Management (IAM).

## Call the Cloud Run Admin API with the deployer account

You call the Cloud Run Admin API from Cloud Run using the
**Cloud Run deployer account**. The deployer account can be either a
user account or a service account, and represents the account that was signed
into the Google Cloud environment.

When the deployer account uses Cloud Run, IAM
checks if the deployer account has the necessary permissions to perform the
Cloud Run operation. The following diagram shows how a user
account calls the Cloud Run Admin API to deploy a new revision from the
Google Cloud console:

**Figure 1.** A user uses the Google Cloud console to deploy a
new revision by sending a request with an access token to the
Cloud Run Admin API. IAM uses that access token to verify
that the user account is authenticated to access the Cloud Run Admin API
before performing the operation.

## Call Google Cloud APIs with the service identity

When a Cloud Run instance interacts with other
IAM-authenticated Cloud Run services, or calls
Cloud Client Libraries either through application code or built-in features
like Cloud Run integrations or
Cloud Storage volume mounts,
the Google Cloud environment uses
Application Default Credentials (ADC)
to automatically detect whether the
**Cloud Run service identity** is authenticated to perform the
API operation. The Cloud Run service identity is a service
account that was assigned as the Cloud Run instance's identity
when you deploy a revision or execute a job.

A service account that is used as the deployer account will only be used as
the service identity if you configure the same service account in your
Cloud Run configuration.

The rest of this guide describes how a Cloud Run resource
uses service identity to call and access Google services and APIs. For more
information on service identity configuration, see the service identity
configuration pages for services,
jobs, and
worker pools.

### Types of service accounts for service identity

When your Cloud Run instance makes calls to Google Cloud APIs to
perform the operations it needs, Cloud Run automatically uses a
service account as the service identity. The two types of service accounts that
can be used as the service identity are as follows:

- **User-managed service account (recommended)**: You manually create this
  service account and determine the most minimal set of permissions that the
  service account needs to access specific Google Cloud resources. The
  user-managed service account follows the format of
  `SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com`.
- **Compute Engine default service account**: Cloud Run
  automatically provides the Compute Engine default service account as the
  default service identity. The Compute Engine default service account follows
  the format of
  `PROJECT_NUMBER-compute@developer.gserviceaccount.com`.

### Avoid the default service account when configuring service identity

By default, the Compute Engine default service account is automatically
created. If you don't specify a service account when the
Cloud Run resource is created, Cloud Run
uses this service account.

Depending on your organization policy configuration, the default service account might
automatically be granted the Editor role on your
project. We strongly recommend that you disable the automatic role grant by
enforcing the `iam.automaticIamGrantsForDefaultServiceAccounts` organization policy
constraint. If you created your organization after May 3, 2024, this
constraint is enforced by default.

If you disable the automatic role grant, you must decide which roles to grant to the default
service accounts, and then grant these
roles yourself.

If the default service account already has the Editor role, we recommend that you replace the
Editor role with less permissive roles.To safely modify the service account's roles, use Policy Simulator to see the impact of
the change, and then grant and revoke the
appropriate roles.

## How service identity works

When your code uses Cloud Client Libraries that makes requests to
Google Cloud API, the following happens:

1. The client library requests an OAuth 2.0 access token for the service
   identity from the instance metadata server.
2. The instance metadata server provides an IAM access token for
   the service account that is configured as the service identity.
3. The request to the Google Cloud API is sent
   with an OAuth 2.0 access token.
4. IAM verifies the service identity referenced in the access
   token for the necessary permissions, and checks policy bindings before it
   forwards the call to the API endpoint.
5. The Google Cloud API performs the operation.

**Figure 1.** Cloud Run generates an
access token from the metadata server, and IAM uses that
access token to verify that the assigned Cloud Run service
identity is authenticated to access the Google Cloud APIs.

## Generate an access token for the Cloud Run request to call Google Cloud APIs

**Warning:** If your Cloud Run service, job, or worker pool uses
service identity to authenticate access
to Google Cloud APIs, never set `GOOGLE_APPLICATION_CREDENTIALS` as an
environment variable on a Cloud Run service, job, or worker pool. Always
configure a user-managed service account instead.

If your Cloud Run code uses
Cloud Client Libraries, you configure service
identity in Cloud Run by assigning a service account at
deployment or execution. This lets the library automatically acquire an access
token to authenticate your code's request. If your Cloud Run code
communicates with other authenticated Cloud Run services, you
must add the access token to your
requests.

To assign a service account as the service identity, see the following guides:

- Configure service identity for services
- Configure service identity for jobs
- Configure service identity for worker pools

However, if you use your own custom code or need to make requests
programmatically, you can use the
metadata server
directly to manually fetch identity tokens and access token described in the
next section. Note that you cannot query this server directly from your local
machine as the metadata server is only available for workloads running on
Google Cloud.

### Fetch ID and access tokens using the metadata server

The two types of tokens you can fetch with the metadata server are as follows:

- OAuth 2.0 access tokens, which are used to call most Google API Client Libraries.
- ID tokens, which are used to call other
  Cloud Run services
  or to invoke any service to
  validate an ID token.

To fetch a token, follow the instructions in the appropriate tab for the type of
token you are using:

### Access tokens

For example, if you want to create a Pub/Sub topic, use the
`projects.topics.create`
method.

1. Use the Compute Metadata Server to
   fetch an access token:

   ```
   curl "http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token" \
       --header "Metadata-Flavor: Google"
   ```

   This endpoint returns a JSON response with an `access_token` attribute.
2. In your HTTP protocol request, the request must be authenticated with an
   access token in the `Authorization` header:

   ```
   PUT https://pubsub.googleapis.com/v1/projects/PROJECT_ID/topics/TOPIC_ID
   Authorization: Bearer ACCESS_TOKEN
   ```

   Where:

   - `PROJECT_ID` is your project ID.
   - `TOPIC_ID` is your topic ID.
   - `ACCESS_TOKEN` is the access token you fetched
     in the previous step.

   Response:

   ```
   {
       "name": "projects/PROJECT_ID/topics/TOPIC_ID"
   }
   ```

### ID tokens

Use the Compute Metadata Server to
fetch an identity token
with a specific audience:

```
curl "http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/identity?audience=AUDIENCE" \
    --header "Metadata-Flavor: Google"
```

Where `AUDIENCE` is the JWT Audience requested.

For Cloud Run services, the audience should be either the
URL of the service you are invoking or a
custom audience,
such as a custom domain, configured for the service.

```
https://service.domain.com
```

For other resources, it is likely the OAuth Client ID of an IAP-protected
resource:

```
1234567890.apps.googleusercontent.com
```

## Next steps

- Configure service identity for
  services,
  jobs, or
  worker pools.
- Learn how to manage access to or
  securely authenticate developers, services, and end-users
  to your services.
- For an end-to-end walkthrough of an application using service identity to
  minimize security risk, follow the
  securing Cloud Run services tutorial.
