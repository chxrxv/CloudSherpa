---
doc_id: sdp-overview
title: Sensitive Data Protection overview
url: https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview
category: security
fetched_at: '2026-10-13T15:13:49+00:00'
license: CC BY 4.0 (Google Cloud documentation)
---

Sensitive Data Protection helps you discover, classify, and de-identify
sensitive data inside and outside Google Cloud. This page describes the services
that make up Sensitive Data Protection.

## When to use Sensitive Data Protection

The following are some common use cases:

- **Discover shadow data across enterprise cloud repositories**: Continuously
  scan and profile data assets across BigQuery, Cloud SQL, and
  Cloud Storage to locate uncatalogued sensitive data and evaluate
  organizational security posture.
- **Prevent sensitive data exposure in real-time applications**: Inspect and
  redact sensitive tokens (such as PII or credentials) from streaming API
  payloads, user forms, and LLM prompt inputs before storing the data.
- **De-identify analytical datasets while preserving utility**: Transform
  direct and indirect identifiers using pseudonymization, date shifting, or
  bucketing so research and business intelligence teams can analyze data
  without exposing plaintext PII.
- **Automate compliance auditing and regulatory reporting**: Detect and
  monitor protected health information (PHI) and financial records to satisfy
  compliance obligations under GDPR, HIPAA, and PCI DSS.
- **Stream security findings into incident response pipelines**: Send
  high-risk finding alerts to Pub/Sub and Security Command Center to trigger
  automated data tagging, access revocation, and security remediation
  workflows.

## Sensitive data discovery

The discovery service lets you generate profiles for your data across
an organization, folder, or project. Data profiles contain metrics and metadata
about your data assets and help you determine where sensitive and high-risk
data reside. Sensitive Data Protection reports these metrics at various
levels of detail. For information about the types of data you can profile, see
Supported resources.

You use a *scan configuration* to specify the resource to scan, the
types of information (*infoTypes*) to
look for, the profiling frequency, and the actions to take when profiling
is complete.

**Tip:** Data profiling is useful if you want to scan large amounts of
data at a high level. If you need to know the granular
details, like the exact location of every instance of sensitive data, consider
performing an inspection as well.

For more information about the discovery service, see Data
profiles overview.

## Sensitive data inspection

The inspection service lets you perform a deep scan of an individual
resource to find instances of sensitive data. You specify the infoType that you
want to search for, and the inspection service generates a report about
every instance of data that matches that infoType. For example, the report tells
you how many credit card numbers are in a Cloud Storage bucket and the
exact location of each instance.

**Tip:** An inspection is useful if you need
detailed information about each instance of sensitive data stored in a resource,
like a single
BigQuery table. It is especially useful if you have
unstructured data—like user-provided comments—that might have
intermittent instances of personally identifiable information.

If you
need to perform automated scans of multiple resources across projects, folders,
or the entire organization, use the discovery
service to generate data profiles.

There are two ways to perform an inspection:

- Create an inspection or hybrid job through the Google Cloud console or
  through the Cloud Data Loss Prevention API of Sensitive Data Protection (DLP API).
- Send a
  `content.inspect`
  request to the DLP API.

### Inspection through a job

You can configure inspection and hybrid jobs through the Google Cloud console
or through the Cloud Data Loss Prevention API. The results of inspection and hybrid jobs are
stored in Google Cloud.

You can specify actions that you want Sensitive Data Protection to take
when the inspection or hybrid job is complete. For example, you can configure a
job to save the findings to a BigQuery table or send a
Pub/Sub notification.

#### Inspection jobs

Sensitive Data Protection has built-in support for select
Google Cloud products. You can inspect a BigQuery table, a
Cloud Storage bucket or folder, and a Datastore kind. For more
information, see Inspect Google Cloud storage and databases for sensitive
data.

#### Hybrid jobs

A hybrid job lets you scan payloads of data sent from any source, and
then store the inspection findings in Google Cloud. For more information,
see Hybrid jobs and job triggers.

### Inspection through a `content.inspect` request

The `content.inspect` method of the DLP API lets you send data
directly to the DLP API for inspection. The response contains the
inspection findings. Use this approach if you require a synchronous operation or
if you don't want to store the findings in Google Cloud.

## Sensitive data de-identification

The de-identification service lets you obfuscate instances of sensitive data.
Various transformation methods
are available, including masking, redaction, bucketing, date shifting, and
tokenization.

There are two ways to perform de-identification:

- Create a de-identified copy of Cloud Storage data using an inspection
  job. For more information, see De-identification of sensitive data in
  storage.
- Send a
  `content.deidentify`
  request to the DLP API. For more information, see De-identifying
  sensitive data.

## Risk analysis

The risk analysis service lets you analyze structured
BigQuery data to identify and visualize the risk that sensitive
information will be revealed (*re-identified*).

You can use risk analysis methods before de-identification to help
determine an effective de-identification strategy, or after de-identification to
monitor for any changes or outliers.

You perform risk analysis by creating a risk analysis job. For more information,
see Re-identification risk analysis.

## Cloud Data Loss Prevention API

The Cloud Data Loss Prevention API lets you use the Sensitive Data Protection services
programmatically. Through the DLP API, you can inspect data from
inside and outside Google Cloud and build custom workloads on or off
cloud. For more information, see Service method
types.

### Asynchronous operations

If you want to asynchronously inspect or analyze data at rest, you can use the
DLP API to create a
`DlpJob`. Creating a
`DlpJob` is the equivalent of creating an inspection job, hybrid job, or risk
analysis job through the Google Cloud console. The results of a `DlpJob` are
stored in Google Cloud.

### Synchronous operations

If you want to inspect, de-identify, or re-identify data synchronously, use the
inline `content` methods of the DLP API. To de-identify data in
images, you can use the
`image.redact`
method. You send the data in an API request and the DLP API responds
with the inspection, de-identification, or re-identification results. The
results of `content` methods and the `image.redact` method aren't stored
in Google Cloud.

## Pricing

For information about costs associated with using Sensitive Data Protection,
see Sensitive Data Protection pricing.

## What's next

- Learn how to profile data in a project.
- Learn how to start or schedule an
  inspection.
- Learn how to inspect data from external sources using hybrid jobs.
- Learn how to create a de-identified copy of data stored in Cloud Storage.
- Learn how to compute k-anonymity for a dataset.
- Learn how to de-identify and re-identify data using the DLP API.
