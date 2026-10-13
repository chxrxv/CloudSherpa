---
doc_id: kms-cmek
title: Customer-managed encryption keys (CMEK)
url: https://docs.cloud.google.com/kms/docs/cmek
category: security
fetched_at: '2026-10-13T15:13:49+00:00'
license: CC BY 4.0 (Google Cloud documentation)
---

This document provides an overview of using Cloud Key Management Service (Cloud KMS) for
customer-managed encryption keys (CMEK). Using Cloud KMS CMEK gives you
ownership and control of the keys that protect your data at rest in
Google Cloud.

## Comparison of CMEK and Google-owned and Google-managed encryption keys

The Cloud KMS keys that you create are customer-managed keys.
Google Cloud services that use your keys are said to have a
*CMEK integration*.
You can manage these CMEKs directly, or through
Cloud KMS Autokey. The following
factors differentiate Google Cloud's default encryption at rest from
customer-managed keys:

| Type of key | Cloud KMS Autokey | Cloud KMS customer-managed (manual) | Google-owned and Google-managed encryption key (Google default encryption) |
| --- | --- | --- | --- |
| Can view key metadata | Yes | Yes | No |
| Ownership of keys1 | Customer | Customer | Google |
| Can manage2 and control3 keys | Key creation and assignment is automated. Customer manual control is fully supported. | Customer, manual control only | Google |
| Supports regulatory requirements for customer-managed keys | Yes | Yes | No |
| Key sharing | Unique to a customer | Unique to a customer | Data from multiple customers is typically protected by shared key encryption keys (KEKs). |
| Control of key rotation | Yes | Yes | No |
| CMEK organization policies | Yes | Yes | No |
| Log administrative and data access to encryption keys | Yes | Yes | No |
| Logical data separation through encryption | Yes | Yes | No |
| Pricing | Varies | Varies | Free |

1 The owner of the key indicates who holds the
rights to the key. Keys that you own have tightly restricted access or no access
by Google.

2 Management of keys includes the following
tasks:

- Create keys.
- Choose the protection level of the keys.
- Assign authority for management of the keys.
- Control access to keys.
- Control usage of keys.
- Set and modify the rotation period of keys, or trigger a rotation of keys.
- Change key status.
- Destroy key versions.
- Delete key versions, keys, and key rings.

3 Control of keys means setting controls on the
kind of keys and how the keys are used, detecting variance, and planning
corrective action if needed. You can control your keys, but delegate management
of the keys to a third party.

### Default encryption with Google-owned and Google-managed encryption keys

All data stored within Google Cloud is encrypted at rest using the same
hardened key management systems that Google Cloud uses for our own
encrypted data. These key management systems provide strict key access controls
and auditing, and encrypt user data at rest using the AES-256 encryption
standard. Google Cloud owns and controls the keys used to encrypt your
data. You can't view or manage these keys or review key usage logs. Data from
multiple customers might use the same key encryption key (KEK). No setup,
configuration, or management is required.

For more information about default encryption in Google Cloud, see
Default encryption at rest.

### Customer-managed encryption keys (CMEK)

Customer-managed encryption keys are encryption keys that you own. This
capability lets you have greater control over the keys used to encrypt data
at rest within supported Google Cloud services, and provides a
cryptographic boundary around your data.
You can manage CMEKs directly in Cloud KMS, or automate provisioning
and assignment by using Cloud KMS Autokey.

Services that support CMEK have a *CMEK integration*. CMEK integration is a
server-side encryption technology that you can use in place of
Google Cloud's default encryption. After CMEK is set up, the operations to
encrypt and decrypt resources are handled by the resource service agent. Because
CMEK-integrated services handle access to the encrypted resource, encryption and
decryption can take place transparently, without end-user effort. The experience
of accessing resources is similar to using Google Cloud's default
encryption. For more information about CMEK integration, see
What a CMEK-integrated service provides.

You can use unlimited key versions for each key.

To learn whether a service supports CMEKs, see the
list of supported services.

Using Cloud KMS incurs costs related to the number of key versions and
cryptographic operations with those key versions.
For more information about pricing, see Cloud Key Management Service pricing. No
minimum purchase or commitment is required.

### Customer-managed encryption keys (CMEK) with Cloud KMS Autokey

Cloud KMS Autokey simplifies creating and managing CMEKs by automating
provisioning and assignment. With Autokey, key rings and keys are
generated on demand as part of resource creation, and service agents that use
the keys for encrypt and decrypt operations are automatically granted the
necessary Identity and Access Management (IAM) roles. Using Autokey is simpler
than provisioning keys yourself, and is the recommended choice if the keys
created by Autokey meet all of your requirements.

Using keys generated by Autokey can help you consistently align with
industry standards and recommended practices for data security, including
key-data location alignment, key specificity, multi-tenant hardware (HSM)
protection level, key rotation schedule, and separation of duties.
Autokey creates keys that follow both general guidelines and
guidelines specific to the resource type for Google Cloud services that
integrate with Autokey. Keys created using Autokey function
identically to other Cloud HSM keys with the same settings,
including support for regulatory requirements for customer-managed keys. For
more information about Autokey, see
Autokey overview.

## When to use customer-managed encryption keys

You can use manually-created CMEKs or keys created by Autokey in
compatible services to help you meet the following goals:

- Own your encryption keys.
- Control and manage your encryption keys, including choice of location,
  protection level, creation, access control, rotation, use, and destruction.
- Generate key material in Cloud KMS or import key material that is
  maintained outside of Google Cloud.
- Set policy regarding where your keys must be used.
- Selectively delete data protected by your keys in the case of off-boarding
  or to remediate security events (crypto-shredding).
- Create and use keys that are unique to a customer, establishing a
  cryptographic boundary around your data.
- Log administrative and data access to encryption
  keys.
- Meet current or future regulation that requires any of these goals.

## What a CMEK-integrated service provides

Like Google Cloud's default encryption, CMEK is server-side, symmetric,
envelope encryption of customer data. The difference from Google Cloud's
default encryption is that CMEK protection uses a key that a customer controls.
CMEKs created manually or automatically using Autokey operate the same
way during service integration.

- Cloud services that have a *CMEK integration*
  use keys you create in Cloud KMS to protect your resources.
- Services that are integrated with Cloud KMS use symmetric
  encryption.
- You choose the protection level of the key.
- All keys are 256-bit AES-GCM.
- Key material never leaves the Cloud KMS system boundary.
- Your symmetric keys are used to encrypt and decrypt in the envelope
  encryption model.

### CMEK-integrated services track keys and resources

- CMEK-protected resources have a metadata field that holds the name of the
  key that encrypts it. Generally, this will be customer-visible in the
  resource metadata.
- Key tracking tells you what resources a key protects, for
  services that support key tracking.
- Keys can be listed by project.

### CMEK-integrated services handle resource access

The principal that creates or views resources in the CMEK-integrated service
does not require the
Cloud KMS CryptoKey Encrypter/Decrypter
(`roles/cloudkms.cryptoKeyEncrypterDecrypter`) for the CMEK used to protect the
resource.

Each project resource has a special service account called a
service agent that performs encryption and decryption with
customer-managed keys. After you give the service agent access to a CMEK, that
service agent will use that key to protect the resources of your choice.

When a requester wants to access a resource encrypted with a customer-managed
key, the service agent automatically attempts to decrypt the requested resource.
If the service agent has permission to decrypt using the key, and you have not
disabled or destroyed the key, the service agent provides encrypt and decrypt
use of the key. Otherwise, the request fails.

No additional requester access is required, and since the service agent handles
the encryption and decryption in the background, the user experience for
accessing resources is similar to using Google Cloud's default encryption.

## Using Autokey for CMEK

For each folder or project where you want to use Autokey, there is a
one-time setup process. You can enable Autokey with
dedicated-project key storage (formerly known as *centralized key
management*) on a folder or with same-project key storage (formerly known
as *delegated key management*) on an individual project or for all projects
within a folder. When you use dedicated-project key storage, you specify a
single key project where Autokey creates keys for resources created in
the folder. When you use same-project key storage, Autokey creates
keys in the same project as the resources that they protect. For more
information about enabling Autokey, see Enable
Cloud KMS Autokey.

Compared to manually creating CMEKs, Autokey does not require the
following setup steps:

- Key administrators don't need to manually create key rings or keys or
  assign privileges to the service agents that encrypt and decrypt data. The
  Cloud KMS service agent does these actions on their behalf.
- Developers don't need to plan ahead to request keys prior to resource
  creation. They can request keys themselves from Autokey as needed,
  while still preserving separation of duties.

When you use Autokey, there is only one step: the developer requests
the keys as part of resource creation. Keys returned are consistent for the
intended resource type.

Your CMEKs created with Autokey behave in the same way as
manually-created keys for the following features:

- CMEK-integrated services behave the same way.
- The key administrator can continue to monitor all keys created and used
  through the Cloud KMS dashboard and
  key usage tracking.
- Organization policies work in the same way with Autokey as they do
  with manually created CMEKs.

For an overview of Autokey, see
Autokey overview. For more information about
creating CMEK-protected resources with Autokey, see Create protected
resources using Cloud KMS Autokey.

## Manually creating CMEKs

When you manually create your CMEKs, you must plan and create key rings, keys,
and resource locations before you can create protected resources.
You can then use your keys to protect the resources.

For the exact steps to enable CMEK, see the documentation for the relevant
Google Cloud service. Some services, such as GKE,
have multiple CMEK integrations for protecting different types of data related
to the service. You can expect to follow steps similar to the following:

1. Create a Cloud KMS key ring or choose an existing key ring. When
   creating your key ring, choose a location that is geographically near to the
   resources you're protecting. The key ring can be in the same project as the
   resources you're protecting or in different projects. Using different
   projects gives you greater control over IAM roles and helps
   support separation of duties.
2. You create or import a Cloud KMS key in the chosen key ring. This
   key is the CMEK.
3. You grant the CryptoKey Encrypter/Decrypter IAM
   role
   (`roles/cloudkms.cryptoKeyEncrypterDecrypter`) on the CMEK to the service
   account for the service.
4. When creating a resource, configure the resource to use the CMEK. For
   example, you can configure a BigQuery table to protect data at
   rest in the table.

For a requester to gain access to the data, they don't need direct access to the
CMEK.

As long as the service agent has the **CryptoKey Encrypter/Decrypter**
role, the service can encrypt and decrypt its data. If you revoke this role, or
if you disable or destroy the CMEK, that data can't be accessed.

**Caution:** Some services can experience permanent data loss when the CMEK remains
disabled or inaccessible for too long.

### CMEK compliance

Some services have CMEK integrations, and allow you to manage keys yourself.
Some services instead offer *CMEK compliance*, meaning the temporary data and
ephemeral key are never written to disk. For a complete list of integrated and
compliant services, see CMEK compatible services.

## Key usage tracking

Key usage tracking shows you the Google Cloud resources within your
organization that are protected by your CMEKs. Using key usage tracking, you
can view the protected resources, projects, and unique Google Cloud products
that use a specific key, and whether keys are in use. For more information about
key usage tracking, see View key usage

## CMEK organization policies

Google Cloud offers organization policy constraints to help ensure
consistent CMEK usage across an organization resource. These constraints provide
controls to Organization Administrators to
require CMEK usage and to specify limitations and controls
on the Cloud KMS keys used for CMEK protection, including the
following:

- Limits on which Cloud KMS keys are used for CMEK
  protection
- Limits on the allowed
  protection levels of keys
- Limits on the location of CMEKs
- Controls for key version destruction

## What's next

- See the list of services with CMEK
  integrations.
- See the list of CMEK-compliant
  services.
- See the list of
  resource types that can
  have key usage tracking.
- See the list of services supported by
  Autokey.
