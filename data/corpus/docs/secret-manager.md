---
doc_id: secret-manager
title: Secret Manager overview
url: https://docs.cloud.google.com/secret-manager/docs/overview
category: security
fetched_at: '2026-10-13T15:13:49+00:00'
license: CC BY 4.0 (Google Cloud documentation)
---

Secret Manager is a secrets and credential management service
that lets you store and manage sensitive data such as API keys, usernames, passwords,
certificates, and more.

This is the documentation for the default *global* service, which lets you store and access secrets from any Google Cloud region.
To learn about the regional service, see the
regional service documentation. If you're not sure which service you need, see
Global and regional service options.

## Key concepts

A *secret*
is a global resource that contains a collection of metadata and secret versions. The metadata can include
labels, annotations, and permissions.

A *secret version*
stores the actual secret data, such as API keys, passwords, or certificates. Each version is
identified by a unique ID or timestamp.

Using Secret Manager, you can do the following:

- **Manage rollback, recovery, and auditing using versions**: Versions help you
  manage gradual rollouts and emergency rollback, If a secret is accidentally changed
  or compromised, you can revert to a previous, known-good version. This minimizes
  potential downtime and security breaches. Versioning maintains a historical record
  of changes made to a secret, including who made the changes and when. It helps you
  audit secret data and track any unauthorized access attempts. You can pin secret
  versions to specific workloads and add
  aliases for
  easier access to secret data. You can also
  disable or
  destroy secret
  versions that you don't require.
- **Encrypt your secret data in transit and at rest**: All secrets are
  encrypted by default, both in transit using TLS and at rest with AES-256-bit encryption
  keys. For those requiring more granular control, you can encrypt your secret data
  with Customer-Managed
  Encryption Keys (CMEK). Using CMEK, you can generate new encryption keys or import existing ones
  to meet your specific requirements.
- **Manage access to secrets using fine-grained Identity and Access Management (IAM) roles and conditions**:
  With IAM roles and permissions,
  you can provide granular access
  to specific Secret Manager resources. You can segregate responsibilities for accessing,
  managing, auditing, and rotating secrets.
- **Ensure high availability and disaster recovery with secret replication**: You
  can replicate your secrets
  across multiple regions to ensure high availability and disaster recovery for your applications
  regardless of their geographic location. You can choose between the following replication policies:
  - Automatic replication: Google Cloud decides
    the regions considering availability and latency. You are only charged for one location.
  - User managed replication: You can
    select a custom set of regions depending on your requirements. You are charged per location.
- **Rotate secrets automatically to meet your security and compliance requirements**:
  Rotating your secrets
  protects against unauthorized access and data breaches. Regularly changing your secrets reduces the risk
  of stale or forgotten secrets and ensures compliance with many regulatory frameworks
  that require periodic rotation of sensitive credentials.
- **Enforce data residency using regional secrets**:
  Data residency
  requires that certain types of data, often belonging to specific individuals or
  organizations, be stored within a defined geographic location. You can create
  regional secrets
  and store your sensitive data within a specific location to comply with data sovereignty laws
  and regulations.
- **Manage operational parameters for your applications using
  Parameter Manager**:
  Parameter Manager
  is an extension to the Secret Manager service that you can use to store and manage
  application configurations such as database connection strings, feature flags, environment names,
  port numbers to listen on, and settings for application features. You can also
  reference secrets
  stored in Secret Manager within your parameter configurations. To use Parameter Manager,
  you must enable the Parameter Manager API and grant your users the
  required IAM roles.

## Difference between secrets management and key management

Secrets management and key management are both critical components of data security,
but they serve distinct purposes and handle different types of sensitive information.
The choice between secrets management and key management depends on your specific needs.
If you want to securely store and manage confidential data, a secrets management system
is the right tool. If you want to manage encryption keys and perform cryptographic operations,
a key management system is the better choice.

You can use the following table to understand the key differences between Secret Manager
and a key management system, such as
Cloud Key Management Service(Cloud KMS).

| Feature | Secret Manager | Cloud KMS |
| --- | --- | --- |
| Primary function | Store, manage, and access secrets as binary blobs or text strings. | Manage cryptographic keys and use them to encrypt or decrypt data. |
| Data stored | Actual secret values. With the appropriate permissions, you can view the contents of the secret. | Cryptographic keys. You can't view, extract, or export the actual cryptographic secrets (the bits and bytes) that are used for encryption and decryption operations. |
| Encryption | Encrypts secrets at rest and in transit using Google-owned and managed keys or customer-managed keys. | Provides encryption and decryption capabilities for other services. |
| Typical use cases | Store configuration information such as database passwords, API keys, or TLS certificates needed by an application at runtime. | Handle large encryption workloads, such as encrypting rows in a database or encrypting binary data such as images and files. You can also use Cloud KMS to perform other cryptographic operations such as signing and verification. |

## Encryption of secrets

Secret Manager always encrypts your secret data before it is persisted
to disk. To learn more about Google Cloud encryption options, refer to
Encryption at rest.

Secret Manager manages server-side encryption keys on your behalf using
the same hardened key management systems that we use for our own encrypted data,
including strict key access controls and auditing. Secret Manager
encrypts user data at rest using AES-256. There is no setup or
configuration required, no need to modify the way you access the service, and no
visible performance impact. Your secret data is automatically and transparently
decrypted when accessed by an authorized user.

The Secret Manager API always communicates over a secure HTTP(S) connection.

Those who require an extra layer of protection can enable CMEK and use their own
encryption keys stored in Cloud Key Management Service to protect the secrets stored in
Secret Manager. See the CMEK documentation
for details on how to configure and use customer-managed encryption keys.

## What's next

- Learn how to
  create a secret.
- Learn how to add a secret version.
- Learn how to edit a secret.
- Learn about quotas and limitations.
- Learn about best practices.
