---
doc_id: assured-workloads
title: Overview of Assured Workloads
url: https://docs.cloud.google.com/assured-workloads/docs/overview
category: compliance
fetched_at: '2026-10-13T15:13:49+00:00'
license: CC BY 4.0 (Google Cloud documentation)
---

# Overview of Assured Workloads

Assured Workloads enables organizations in the private and public
sectors to configure a sovereign data and access boundary with residency,
access, and personnel controls for sensitive workloads in the cloud. You can use
Assured Workloads to simplify management and configuration of
regulated workloads by applying predefined control packages
to folders. Assured Workloads lets you run compliant workloads
while maintaining the scale, cost, and service availability benefits of
commercial cloud infrastructure.

## Use cases for Assured Workloads

Use Assured Workloads if your organization must ensure compliance
with specific regulatory, regional, or sovereignty requirements. For example,
Assured Workloads lets the following organizations meet their
compliance obligations:

- Organizations with strict regulations for data storage, key management, and
  access (such as financial services, healthcare, and governmental bodies).
- Organizations that must store their data within certain regions or
  countries.
- Organizations that must control Google Cloud personnel access to their data.

## Assured Workloads capabilities

Assured Workloads provides a variety of capabilities to help you
meet your compliance and regulatory requirements, including the following:

- Regional data boundaries and regulatory data boundaries for compliance
  enforcement
- Personnel data access controls
- Encryption key management controls
- Compliance updates
- Monitoring for violations

The following sections describe these capabilities.

### Control packages

Control packages are the foundation for compliance enforcement for
Assured Workloads. Assured Workloads control
packages are available for the following control types: regional data
boundaries, regulatory data boundaries, and
Sovereign Controls by Partners.
When you create an Assured Workloads folder for a specific
control package, the controls within the control package define guardrails for
all projects and resources within the folder. These controls are enforced using
organization policy constraints and other features.

Support for Google Cloud products and services varies by control package.
For more information, see
Supported products by control package.

#### Regional data boundaries

Regional data boundary control packages support data residency requirements by
restricting the geographic location where resources can be stored. Some data
boundaries also let you exercise independent control over Google's access to
your data, such as by approving access only for specific provider behaviors that
you deem appropriate and necessary.

These data boundaries let you specify a Google Cloud region where your
data must reside and prevents data storage outside of that region. For example,
if the EU Data Boundary control package is applied, data residency controls are
implemented to restrict resource usage to EU-only regions.
Assured Workloads offers various
regional data boundaries
to enforce data residency restrictions and Google personnel support access
control.

For more information on Assured Workloads and data residency, see
Data residency.

#### Regulatory data boundaries

Regulatory data boundary control packages let you deploy a set of controls to
address a specific regulatory or compliance requirement. Google Cloud
includes regulatory data boundaries for the following:

- Canada Controlled Goods Program (CGP)
- Criminal Justice Information Systems (CJIS)
- FedRAMP Moderate and FedRAMP High
- Healthcare and Life Sciences Controls (with or without US Support)
  for
  Health Insurance Portability and Accountability Act (HIPAA) and
  Health Information Trust Alliance (HITRUST)
- Impact Level 2 (IL2), Impact Level 4 (IL4), and Impact Level 5 (IL5)
- International Traffic in Arms Regulations (ITAR)
- IRS Publication 1075

For a complete list, see
Regulatory data boundaries.

#### Sovereign Controls by Partners

Assured Workloads also offers control packages that are operated and
managed by partners through
Sovereign Controls by Partners.
Sovereign Controls by Partners lets you use a local, trusted partner to
manage encryption keys, access justification, and audits. These control packages
help enforce data residency and provide security configurations that encompass
critical aspects of cloud infrastructure, such as encryption and key management.

### Control of Google personnel access to your data

You can control which Google personnel can access your data when fulfilling
support tasks. Assured Support for Assured Workloads is an
additional Google Cloud Customer Care feature available with
Enhanced Support or
Premium Support. When used, Google
support personnel must adhere to certain geographical and personnel-based
attributes requirements. Depending on the control package, personnel controls
are implemented based on criteria such as their region or fulfilling certain
background check requirements. For example, access controls that support FedRAMP
High require all first-level and second-level Google support personnel and
subprocessors to be located in the US and to meet
enhanced background check requirements.

For more information on Assured Support for Assured Workloads,
see Getting Support.

### Key management

Depending on the control package, various key management controls are available
to support regulatory compliance. For example, the Data Boundary for ITAR
control package requires the use of
customer-managed encryption keys (CMEKs). To enable separation
of duties, the Data Boundary for ITAR control package uses a key management
project that is separate from other deployed resources and creates a unique key
ring for storage within a compliance location.
Assured Workloads also offers support for
Google-owned and Google-managed encryption keys (FIPS-140-2 compliant), CMEKs,
Cloud External Key Manager (Cloud EKM), and
key import for other control packages.

For more information on key management, see
Supporting compliance with key management.

### Workload updates

Workload updates lets you evaluate and
maintain control package configurations. As improvements are made to available
control packages, you can evaluate whether your deployed
Assured Workloads folder configurations are the same as the most
recently available version. If a more recent configuration version is available,
you can apply updates to the Assured Workloads folder to upgrade
to the latest version.

### Violation monitoring

Assured Workloads monitors for organization policy constraint
violations and resource violations to provide insights into compliance for a
deployed control package. You can enable email notifications for organization
policy violations or when a violation exception was added. These notifications
include information about the Assured Workloads folder, audit
logs, and affected organization policies to enable informed review and
remediation of the causes for non-compliance.

For more information on monitoring, see
Monitor an Assured Workloads folder for violations.

## Services for access control and visibility

The following Google Cloud services provide options to control and provide
visibility into data access and encryption keys. You can use these services in
combination with Assured Workloads to help meet your
compliance-based needs.

| Google Cloud service | Description |
| --- | --- |
| Access Approval | Access Approval provides control over Google personnel access to your data. An authorized customer administrator in your organization must approve a request before a Google administrator receives access. Approved access requests are logged with Access Transparency logs that are linked to the approval request. After a request is approved, access must be properly privileged within Google before access is permitted.  When used with Assured Workloads, the Access Approval request conditions are secondary to the applied Assured Workloads personnel access assurances. For more information, see How Access Approval works with Assured Workloads. |
| Access Transparency | Access Transparency lets you view Google authorized personnel activity logs. These logs provide details for actions related to the fulfillment of a support request and actions related to service availability. |
| Key Access Justifications | Key Access Justifications enable control over viewing and approving key access requests in Cloud KMS or certain external key management partners. You can approve or deny requests based on the justification. Depending on the Assured Workloads control package, you can use Key Access Justifications with Cloud EKM keys, Cloud HSM keys, or Cloud KMS software keys. |

## Control package renaming notice

Assured Workloads uses *control packages* to refer to sets of controls
that support the baseline for a compliance framework, statute, or regulation.
Control package names in the console and APIs have changed as of June 2025.
These new names are also reflected in the
`ComplianceRegime`
enums that are used when creating a new workload using the
Assured Workloads API. Only the names have changed; the underlying
functionality has not changed.

The following table describes the new and previous for some of the control
packages.

| Upcoming name | Current name |
| --- | --- |
| Australia Data Boundary | Australia Regions |
| Australia Data Boundary and Support | Australia Regions with Assured Support |
| Brazil Data Boundary | Brazil Regions |
| Canada Data Boundary | Canada Regions |
| Canada Data Boundary and Support | Canada Regions and Support |
| Chile Data Boundary | Chile Regions |
| Data Boundary for Canada Controlled Goods | Canada Controlled Goods |
| Data Boundary for Canada Protected B | Canada Protected B |
| Data Boundary for CJIS | Criminal Justice Information Systems (CJIS) |
| Data Boundary for FedRAMP High | FedRAMP High |
| Data Boundary for FedRAMP Moderate | FedRAMP Moderate |
| Data Boundary for Impact Level 2 (IL2) | Impact Level 2 (IL2) |
| Data Boundary for Impact Level 4 (IL4) | Impact Level 4 (IL4) |
| Data Boundary for Impact Level 5 (IL5) | Impact Level 5 (IL5) |
| Data Boundary for IRS Publication 1075 | IRS Publication 1075 |
| Data Boundary for ITAR | International Traffic in Arms Regulations (ITAR) |
| EU Data Boundary | EU Regions |
| EU Data Boundary and Support | EU Regions and Support |
| EU Data Boundary with Access Justifications | Sovereign Controls for EU |
| Hong Kong Data Boundary | Hong Kong Regions |
| India Data Boundary | India Regions |
| Indonesia Data Boundary | Indonesia Regions |
| Israel Data Boundary | Israel Regions |
| Israel Data Boundary and Support | Israel Regions and Support |
| Japan Data Boundary | Japan Regions |
| Kingdom of Saudi Arabia Data Boundary with Access Justifications | Sovereign Controls for Kingdom of Saudi Arabia (KSA) |
| Qatar Data Boundary | Qatar Regions |
| Singapore Data Boundary | Singapore Regions |
| South Africa Data Boundary | South Africa Regions |
| South Korea Data Boundary | South Korea Regions |
| Switzerland Data Boundary | Switzerland Regions |
| Taiwan Data Boundary | Taiwan Regions |
| UK Data Boundary | UK Regions |
| US Data Boundary | US Regions |
| US Data Boundary and Support | US Regions and Support |
| US Data Boundary for Healthcare and Life Sciences | Healthcare and Life Sciences Controls |
| US Data Boundary for Healthcare and Life Sciences with Support | Healthcare and Life Sciences Controls with US Support |

## What's next

- For information about pricing, see Assured Workloads
  pricing.
- See available control packages
  and supported products.
- To give Assured Workloads a try, sign up for the free trial
  program.
- Audit your Google Cloud environment with
  Audit Manager.
