---
doc_id: vpc-sc
title: Overview of VPC Service Controls
url: https://docs.cloud.google.com/vpc-service-controls/docs/overview
category: security
fetched_at: '2026-10-13T15:13:49+00:00'
license: CC BY 4.0 (Google Cloud documentation)
---

This topic provides an overview of VPC Service Controls and describes its advantages
and capabilities.

## Who should use VPC Service Controls

Your organization might own intellectual property in the form of highly
sensitive data, or your organization might handle sensitive data that is subject
to additional data protection regulations, such as PCI DSS. Unintended loss or
disclosure of sensitive data can lead to significant negative business
implications.

If you are migrating from on-premises to the cloud, one of your goals might be
to replicate your on-premises network based security architecture as you move
your data to Google Cloud. To protect your highly sensitive data, you might want
to ensure that your resources can only be accessed from trusted networks. Some
organizations might allow public access to resources as long as the request
originates from a trusted network, which can be identified based on the IP
address of the request.

To mitigate data exfiltration risks, your organization might also want to ensure
secure data exchange across organizational boundaries with fine-grained
controls. As an administrator, you might want to ensure the following:

- Clients with privileged access don't also have access to partner resources.
- Clients with access to sensitive data can only read public data sets but not
  write to them.

## How VPC Service Controls reduces data exfiltration risks

VPC Service Controls helps protect against accidental or targeted action
by external entities or insider entities, which helps to minimize unwarranted
data exfiltration risks from Google Cloud services such as Cloud Storage
and BigQuery. You can use VPC Service Controls to create perimeters
that protect the resources and data of services that you explicitly specify.

VPC Service Controls secures your Google Cloud services by defining the
following controls:

- Clients within a perimeter that have private access to resources do not
  have access to unauthorized (potentially public) resources outside the
  perimeter.
- Data cannot be copied to unauthorized resources outside the perimeter using
  service operations such as `gcloud storage cp`
  or `bq mk`.
- Data exchange between clients and resources separated by perimeters
  is secured by using ingress and egress rules.
- Context-aware access to resources is based on client attributes, such as
  identity type (service account or user), identity, device data, and network
  origin (IP address or VPC network). The following are examples of
  context-aware access:

  - Clients outside the perimeter that are on Google Cloud or
    on-premises are within authorized VPC resources and use
    Private Google Access to access resources within a perimeter.
  - Internet access to resources within a perimeter is restricted to a range
    of IPv4 and IPv6 addresses.

  For more information, see
  Context-aware access using ingress rules.
- Access to Google services not fully integrated with VPC Service Controls on
  private network paths can be controlled by using
  VPC Service Controls service patterns.
  Administrators can permit access only to specific unsupported API URL
  patterns, which mitigates risks associated with overly broad access.

VPC Service Controls provides an extra layer of security defense for
Google Cloud services that is independent of Identity and Access Management
(IAM). While IAM enables granular *identity-based
access control*, VPC Service Controls enables broader *context-based perimeter
security*, including controlling data egress across the perimeter. We recommend
using both VPC Service Controls and IAM for defense in depth.

VPC Service Controls lets you monitor resource access patterns across your
service perimeters using Cloud Audit Logs. For more information, see
VPC Service Controls audit logging.

## Security benefits of VPC Service Controls

VPC Service Controls helps mitigate the following security risks without sacrificing
the performance advantages of direct private access to Google Cloud
resources:

- **Access from unauthorized networks using stolen credentials**: By
  allowing private access only from authorized VPC networks,
  VPC Service Controls helps protect against the risk of data exfiltration
  presented by clients using stolen OAuth or service account credentials.
- **Data exfiltration by malicious insiders or compromised code:**
  VPC Service Controls complements network egress controls by preventing clients
  within those networks from accessing the resources of Google-managed
  services outside the perimeter.

  VPC Service Controls also prevents reading data from or copying data to a
  resource outside the perimeter. VPC Service Controls prevents
  service operations such as a `gcloud storage cp` command copying to a public
  Cloud Storage bucket or a `bq mk` command copying to a permanent
  external BigQuery table.

  Google Cloud also provides a restricted virtual IP that is integrated
  with VPC Service Controls.
  The restricted VIP also allows requests to be
  made to services supported by VPC Service Controls
  without exposing those requests to the internet.
- **Public exposure of private data caused by misconfigured IAM
  policies**: VPC Service Controls provides an extra layer of security by
  denying access from unauthorized networks, even if the data is exposed by
  misconfigured IAM policies.
- **Monitoring access to services**: Use VPC Service Controls in dry run
  mode to monitor requests to
  protected services without preventing access and to understand traffic
  requests to your projects. You can also create honeypot perimeters to
  identify unexpected or malicious attempts to probe accessible services.

You can use an organization access policy and configure VPC Service Controls for
your entire Google Cloud organization, or use scoped
policies and configure
VPC Service Controls for a folder or project in the organization. You retain the
flexibility to process, transform, and copy data within the perimeter.

VPC Service Controls configurations are managed at the organization level by
default, but scoped access policies for folders or projects can be used to
delegate administration of service perimeters further down the resource
hierarchy.

### VPC Service Controls and metadata

VPC Service Controls is not designed to enforce comprehensive controls on
metadata movement.

In this context, *data* is defined as content stored in
a Google Cloud resource. For example, the contents of a
Cloud Storage object. *Metadata* is defined as the attributes of the
resource or its parent. For example, Cloud Storage bucket names.

The primary goal of VPC Service Controls is to control the movement of data,
rather than metadata, across a service perimeter through supported services.
VPC Service Controls also manages access to metadata, but there might be scenarios
in which metadata can be copied and accessed without VPC Service Controls policy checks.

We recommend that you rely on IAM, including the use of
custom roles,
to ensure appropriate control over access to metadata.

## Capabilities

VPC Service Controls lets you define security policies that prevent access
to Google-managed services outside of a trusted perimeter, block access to data
from untrusted locations, and mitigate data exfiltration risks.

You can use VPC Service Controls for the following use cases:

- Isolate Google Cloud resources and VPC networks
  into service perimeters
- Extend perimeters to on-premises networks using authorized
  VPN or Cloud Interconnect landing zone VPC networks.
- Control access to Google Cloud resources from the internet
- Protect data exchange across perimeters and organizations
  by using ingress and egress rules
- Allow context-aware access to resources based on
  client attributes by using ingress rules

### Isolate Google Cloud resources into service perimeters

A **service perimeter** creates a security boundary around Google Cloud
resources. A service perimeter allows free communication within the perimeter
but, by default, blocks communication to Google Cloud services across the
perimeter.

The perimeter works specifically with Google Cloud managed services. The
perimeter doesn't block access to any third-party APIs or services on the
internet.

You can configure a perimeter to control the following types of communications:

- From public internet to customer resources within managed services
- From virtual machines (VMs) to a Google Cloud service (API)
- Between Google Cloud services

VPC Service Controls doesn't require you to have a Virtual Private Cloud
(VPC) network. To use
VPC Service Controls without having any resources on a VPC
network, you can allow traffic from external IP ranges or certain
IAM principals. For more information, see
Create and manage access levels.

Here are some examples of VPC Service Controls creating a security boundary:

- A VM within a VPC network
  that is part of a service perimeter can read from or write to a Cloud Storage
  bucket in the same perimeter. However, VPC Service Controls doesn't allow
  VMs within VPC networks that are outside the perimeter to
  access Cloud Storage buckets that are inside the perimeter. You must
  specify an ingress policy to allow VMs within VPC networks that are outside the
  perimeter to access Cloud Storage buckets that are inside the perimeter.
- A host project that contains multiple VPC networks has a different perimeter
  policy for each VPC network in the host project.
- A copy operation between two Cloud Storage buckets succeeds if both
  buckets are in the same service perimeter, but if one of the
  buckets is outside the perimeter, the copy operation fails.
- VPC Service Controls doesn't allow a VM within a VPC network that is inside a
  service perimeter to access Cloud Storage buckets that
  are outside the perimeter.

The following diagram shows a service perimeter that allows communication between a
VPC project and Cloud Storage bucket inside the perimeter but blocks
all communication across the perimeter:

### Extend perimeters to an authorized VPN or Cloud Interconnect

You can configure private communication to Google Cloud resources from
VPC networks that span hybrid environments with
Private Google Access on-premises extensions. To privately access
Google Cloud resources within a perimeter, the VPC network
that contains the landing zone from on-premises must be a part of the perimeter
for resources in the on-premises network.

VMs with private IP addresses in a VPC network secured by a
service perimeter cannot access managed resources outside the service perimeter.
If necessary, you can continue to enable inspected and audited access to all
Google APIs (for example, Gmail) over the internet.

The following diagram shows a service perimeter that extends to hybrid environments
with Private Google Access:

### Control access to Google Cloud resources from the internet

Access from the internet to managed resources within a service perimeter is
denied by default. Optionally, you can enable access based on the context of the
request. To do so, you can create ingress rules or access levels to permit
access based on various attributes, such as the source IP address, identity, or
source Google Cloud project. If requests made from the internet don't meet
the criteria defined in the ingress rule or access level, the requests are
denied.

To use the Google Cloud console to access resources within a perimeter,
you must configure an access level that allows access from one or more IPv4
and IPv6 ranges, or to specific user accounts.

The following diagram shows a service perimeter that allows access from the internet
to protected resources based on the configured access levels, such as IP address or device policy:

## Other controls to mitigate data exfiltration risks

- **Domain restricted sharing**: You can consider setting up an
  organizational policy to limit resource sharing to identities that belong to a
  particular organization resource. For more information, see
  Restricting
  identities by domain.
- **Uniform bucket-level access**: To uniformly control access to your
  Cloud Storage buckets, consider setting up bucket-level
  IAM permissions. Using uniform bucket-level access lets you use
  other Google Cloud security features such as domain restricted sharing,
  Workforce Identity Federation,
  and IAM conditions.
- **Multi-factor authentication**: We recommend using
  multi-factor authentication to
  access your Google Cloud resources.
- **Post-deployment scans**: You can consider using the following
  post-deployment scanning tools to scan for open Cloud Storage buckets:
  1. Security Command Center
  2. Cloud Asset Inventory to search asset metadata history and analyse
     IAM policy to understand who has access to what.
  3. Third-party tools like Palo Alto PrismaCloud
- **De-identification of sensitive data**: You can consider using
  Sensitive Data Protection to discover, classify, and de-identify
  sensitive data inside and outside Google Cloud. De-identification of
  sensitive data can be done by redaction, tokenization, or encryption.
- **Automation using infrastructure-as-code tools**: We recommend that
  you deploy Cloud Storage buckets using an automation tool to control access
  to the buckets. Pass the infrastructure-as-code through human or automated
  reviews before deployment.

## Unsupported Services

For more information on products and services that are supported by
VPC Service Controls, refer to the
Supported products page.

**Warning:** While it may be possible to enable unsupported services to access the
data of supported products and services, we recommend that you do not. Unexpected
issues might occur when attempting to access a supported service using
an unsupported service, especially within the same project.

Unsupported services may not function at all when enabled in a project
protected by VPC Service Controls, especially when low-level storage
services like Cloud Storage or Pub/Sub are
restricted. We recommend deploying unsupported services in projects
outside perimeters. To allow these services to access data in resources
within a perimeter,
create an access level that includes the service account
for that service and
apply it to perimeters as needed.

Attempting to restrict an unsupported service using the `gcloud` command-line tool or
the Access Context Manager API will result in an error.

Cross-project access to data of supported services will be blocked by VPC Service Controls.
Additionally, the restricted VIP can be used to block the ability of workloads
to call unsupported services.

## Known limitations

There are some known limitations with certain Google Cloud services,
products, and interfaces when you use VPC Service Controls. For example,
VPC Service Controls doesn't support all Google Cloud services.
Therefore, don't enable unsupported Google Cloud services in the
perimeter. For more information, see the VPC Service Controls supported products list.
If you need to use a service that VPC Service Controls doesn't support,
enable the service in a project that is outside the perimeter.

We recommend that you review known limitations before you include
Google Cloud services in the perimeter. For more information, see the
VPC Service Controls service limitations.

## Glossary

In this topic, you have learned about several new concepts introduced by
VPC Service Controls:

VPC Service Controls
:   Technology that enables you to define a service perimeter
    around resources of Google-managed services to control communication to and
    between those services.

service perimeter
:   A service perimeter around Google-managed resources. Allows free
    communication within the perimeter but, by default, blocks all communication
    across the perimeter.

ingress rule
:   A rule that allows an API client that is outside the perimeter to access
    resources within a perimeter. For more information, see Ingress and egress rules.

egress rule
:   A rule that allows an API client or resource that is inside the perimeter to
    access Google Cloud resources outside the perimeter. The perimeter
    does not block access to any third-party API or services on the internet.

service perimeter bridge
:   A perimeter bridge allows projects in different service perimeters to
    communicate. Perimeter bridges are bidirectional, allowing projects from
    each service perimeter equal access within the scope of the bridge.

    **Note:** Instead of using a perimeter bridge, we recommend using ingress and
    egress rules that provide more granular controls.

Access Context Manager
:   A context-aware request classification service that can map a request to
    an access level based on specified attributes of the client, such as the
    source IP address. For more information, see Overview of Access Context Manager.

access level
:   A classification of requests over the internet based on several attributes,
    such as source IP range, client device, geolocation, and others. Just like
    an ingress rule, you can use an access level to configure a service
    perimeter to grant access from the internet based on the access level
    associated with a request. You can create an access level using Access Context Manager.

access policy
:   A Google Cloud resource object that defines service perimeters. You
    can create access policies that are scoped to specific folders or projects
    alongside an access policy that can apply to the entire organization. An
    organization can have only one organization-level access policy.

scoped policy
:   A scoped policy is an access policy that is scoped to specific folders or
    projects alongside an access policy that applies to the entire organization.
    For more information, see Overview of scoped policies.

restricted VIP
:   The restricted VIP provides a private network route for products and APIs
    supported by VPC Service Controls in order to make data and resources used by
    those products inaccessible from the internet. `restricted.googleapis.com`
    resolves to `199.36.153.4/30`.
    This IP address range is not announced to the internet.

## What's next

- Learn about service perimeter configuration.
- Understand how to manage VPC networks in service perimeters
- Review the known service limitations.
