---
doc_id: gce-cud
title: Committed use discounts (CUDs) for Compute Engine
url: https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview
category: cost
fetched_at: '2026-10-13T15:13:49+00:00'
license: CC BY 4.0 (Google Cloud documentation)
---

This document explains Google Cloud's committed use discounts (CUDs) and
the types of CUDs that you can receive for Compute Engine.
**Note**: This document discusses some spend-based committed use discounts (CUDs) that
automatically migrate to a new consumption model, which leverages discounts rather than credits.
The migration date is indicated by a notification in the Google Cloud console Billing Overview
page. For more information about the improvements, the affected CUDs, and any required actions on
your part, see Spend-based CUDs.

Google Cloud offers CUDs in return for purchasing committed use contracts
(also known as commitments). When you purchase a commitment, you commit either
to a minimum amount of resource usage or to a minimum spend amount for a
specified term duration of one or three years.

For Compute Engine, you receive deeply discounted prices for your
VM instances in return for your 1-year or 3-year commitments.

Depending on your
resource usage requirements, you can receive CUDs for Compute Engine
resources in one of the following ways:

- **Resource-based committed use discounts (or resource-based CUDs)**
  are CUDs that you receive when you purchase a resource-based commitment and
  commit to use a minimum amount of Compute Engine resources in a
  specific region and with a specific machine configuration. These CUDs are
  ideal for predictable and steady state *resource usage*.
- **Compute flexible committed use discounts (or compute flexible CUDs)**
  are spend-based CUDs that you receive when you purchase a compute flexible
  commitment and commit to a minimum amount of hourly spend on eligible
  services and resources. These CUDs are ideal for scenarios where you have
  more predictable *Google Cloud spend needs* across one or more of the
  following services:

  - Compute Engine
  - Google Kubernetes Engine
  - Cloud Run

The following sections of this document explain these CUD types, their
key differences, and how you receive these CUDs for your Compute Engine
resources.

## Resource-based CUDs

Resource-based commitments are ideal for predictable and steady state usage.
These commitments provide a discount in exchange for your commitment to purchase
a minimum amount of Compute Engine resources. When you purchase a
resource-based commitment, you commit to purchasing a specific type and amount
of Compute Engine resources with a commitment plan of either 1 year or
3 years. In return, you receive those resources at discounted prices. A 3-year
plan offers a higher discount rate than a 1-year plan.

### Location- and project-level scopes

Each resource-based commitment is linked to the region and project in which you
purchase that commitment. You can use a given commitment to cover resources
only in the region that was specified by the commitment.

However, depending on the Cloud Billing account's
CUD sharing
configuration, your commitment can cover resource usage either within the
purchasing project or across all projects under the same Cloud Billing
account, as follows:

- By default, all new Cloud Billing accounts that were created on or
  after June 16, 2026 have CUD sharing enabled. For those accounts,
  resource-based CUDs from any commitment are shared automatically across
  eligible usage from all projects in that Cloud Billing account.
- If a Cloud Billing account was created before June 16, 2026, then
  see
  CUD scope and default configuration
  for more information.

### Eligible resources

Resource-based commitments are available for the following resources:

- vCPUs
- Memory
- GPUs
- Local SSD disks
- Sole-tenant nodes
- Operating system (OS) licenses.

### Types of resource-based commitments

You can purchase the following categories of resource-based commitments:

- **Hardware commitments:** You can purchase hardware commitments for
  resources like vCPUs, memory, GPUs, local SSDs, and sole-tenant nodes. You
  get a discount of **up to 70%** for memory-optimized machine series and a
  discount of **up to 55%** for all other machine series.
- **Software license commitments:** You can purchase license commitments
  for applicable premium operating system (OS) licenses. You get the following
  discounts in return:

  - **Up to 79%** for SUSE Linux Enterprise Server (SLES) images
  - **Up to 63%** for SLES for SAP images
  - **Up to 20%** for Red Hat Enterprise Linux (RHEL) images

Resource-based commitments for hardware resources are separate from the ones
for licenses. You can purchase both categories of commitments for the same
VM instance, but you cannot purchase a single resource-based commitment that
covers both hardware resources and licenses.

When you purchase a resource-based commitment, the commitment becomes active on
the following day at 12 AM US and Canadian Pacific Time (UTC-8, or UTC-7 during
daylight saving time). You are billed monthly for your committed resources
until the end of your commitment term, regardless of whether or not you use
those resources. You can't cancel a commitment after its purchase.

### Learn more and purchase

To learn more about resource-based CUDs for Compute Engine, see
Resource-based committed use discounts.

For purchase information, see one of the following depending on your use case:

- Purchase hardware commitments without attached reservations
- Purchase hardware commitments with attached reservations
- Purchase software commitments for OS licenses

## Compute flexible CUDs

Compute flexible CUDs add flexibility to your Google Cloud spending
capabilities by providing discounts for your spend across Compute Engine,
GKE, and Cloud Run. Specifically for Compute Engine,
compute flexible CUDs eliminate the need to restrict your commitments to a
single project, region, or machine configuration. With a compute flexible
commitment, you can receive applicable CUDs on eligible Compute Engine spend
across the commitment's Cloud Billing account, regardless of the
project or region where you use your Compute Engine resources.

To learn about how compute flexible CUDs apply to the other services, see the
following documents:

- CUDs documentation for GKE
- CUDs documentation for Cloud Run

### Eligible resources

For Compute Engine, the eligible resources include memory, vCPUs, and Local
SSD disks that are used with the following machine series. For the G2 and G4
machine series only, the attached GPUs are also eligible.

- **General purpose**: C3, C3D, C4, C4A, C4D, E2, N1, N2, N2D, N4, N4D, and
  N4A machine series
- **Compute-optimized**: H3, H4D, C2, and C2D machine series
- **Network-optimized**: C4N machine series
- **Memory-optimized**: M1, M2, M3, and M4 machine series
- **Storage-optimized**: Z3 machine series
- **Accelerator-optimized**: G2 and G4 machine series

For every listed machine series, the resource eligibility applies to all
available machine types and sole-tenant node types. For sole-tenant nodes, the
resulting sole-tenancy premium is also eligible for compute flexible CUDs.

**Note:** For memory-optimized VMs, compute flexible CUDs are available only for
3-year commitments. When you purchase a 1-year compute flexible commitment for
your memory-optimized VMs, you don't receive any discount on your usage. Your
eligible memory-optimized VM spend will burn down your otherwise unused
commitment without any discount.
To view the full list of SKUs that are eligible for compute flexible CUDs, see
SKU Groups - Compute Flexible CUD Eligible SKUs.

### Applicable discounts

Depending on your commitment's term and your Cloud Billing account's
CUD model, you receive the following compute flexible CUDs for your resources
and services:

| **Service** | **Spend eligible on** | **1-year CUDs** | **3-year CUDs** |
| --- | --- | --- | --- |
| Compute Engine | vCPUs and memory of M1, M2, M3, and M4 machine series | No discounts | 63% |
| vCPUs and memory of H3 and H4D machine series | 17% | 38% |
| vCPUs and memory of C2, C2D, C3, C3D, C4, C4A, C4D, E2, N1, N2, N2D, N4, N4D, and N4A machine series | 28% | 46% |
| C4N machine series | 28% | 54% |
| vCPUs, memory, and NVIDIA L4 GPUs of G2 machine series | 21% | 43% |
| vCPUs, memory, and NVIDIA RTX PRO 6000 GPUs of G4 machine series | 16% | 42% |
| Local SSD disks attached to supported machine series | 28% | 46% |
| Sole-tenancy premium | 28% | 46% |
| GKE | GKE Standard and GKE Autopilot | 28% | 46% |
| Cloud Run | Cloud Run services with request-based billing | 17% | 17% |
| Cloud Run functions | 17% | 17% |
| Cloud Run services with instance-based billing, Cloud Run jobs, and Cloud Run worker pools | 28% | 46% |

**Note:** The discounts that you receive may differ for Cloud Billing
accounts that have
other on-demand VM savings in effect.

### How compute flexible commitments work

This section explains how compute flexible commitments work and the manner
in which compute flexible CUDs apply to your eligible Google Cloud spend.

#### Commitment fee

When you purchase a compute flexible commitment for your Cloud Billing
account for either a 1- or 3-year term, you commit to spending a minimum
hourly amount on eligible resources and services for the duration of the
commitment's term. This amount becomes your hourly commitment fee, which
you pay for the entire duration of the term, regardless of your actual usage.

#### Commitment activation

Your commitment becomes active shortly after purchase and you start getting
charged the commitment fee. The exact activation time depends on when you
purchased the commitment within the hour, as follows:

- **Purchased during minute 49 or earlier of a specific hour**: The
  commitment becomes active at the start of the next hour. For example,
  if you purchase the commitment between 7:00 PM and 7:49 PM in
  your timezone, then your commitment becomes active at 8:00 PM in that
  timezone.
- **Purchased during minute 50 or later of a specific hour**: The
  commitment becomes active at the start of the hour after the next one.
  For example, if you purchase the commitment between 7:50 PM and
  7:59 PM in your timezone, then your commitment becomes active at 9:00 PM
  in your timezone.

#### How CUDs apply to usage costs

After your commitment becomes active, you start receiving eligible resources
and services at discounted prices. Google Cloud applies the discounts
directly to the prices of all eligible resources and services. To summarize,
you are committing to an hourly spend that is based on the discounted resource
costs.

Every hour, until your total spend on eligible SKUs equals the commitment fee,
the following things happen:

- SKUs for eligible usage are charged at the discounted prices as determined
  by the CUD consumption model rates.
  The consumption model ID is `D97B-0795-975B` for 1-year compute flexible
  commitments and `70D7-D1AB-12A4` for 3-year compute flexible commitments.
- Your commitment fee offsets these discounted usage costs until your total
  hourly spend equals the commitment fee value. At this point, your
  compute flexible commitment is considered to be fully utilized.

#### Commitment utilization criteria

Your Cloud Billing account might have multiple spend-based
commitments that can cover usage of the same resource or service type.
Additionally, a single compute flexible commitment can cover the usage of
several types of resources and services. For a given Cloud Billing
account, Google Cloud applies spend-based commitments to any eligible
hourly usage in the following order of precedence. If you have multiple
spend-based commitments and multiple types of usage, then these rules
determine which commitment Google Cloud utilizes first and which usage
Google Cloud covers first.

1. **Service-specific commitments first**: If both a compute flexible
   commitment and a service-specific spend-based commitment can cover the
   same usage, then the service-specific commitment takes precedence. By
   first utilizing the commitment with a narrower scope,
   Google Cloud keeps the more generic and broader-scoped commitment
   available for other types of usage.

   *Example*: Suppose that you purchased a compute flexible commitment
   and a legacy Cloud Run commitment to cover eligible
   Cloud Run functions usage. In this scenario, Google Cloud
   first utilizes your service-specific Cloud Run commitment to
   cover the eligible usage.
2. **Oldest compute flexible commitment first**: If you have multiple
   compute flexible commitments that can cover the same eligible usage, then
   Google Cloud first utilizes the active commitment that you purchased
   first. After Google Cloud fully utilizes that commitment, it uses
   the next oldest commitment to cover the remaining eligible usage.

   *Example*: Suppose that you have N2 VM usage that can be covered by two
   compute flexible commitments called `compute-flexible-commitment-1` and
   `compute-flexible-commitment-2`. If you purchased
   `compute-flexible-commitment-1` four months ago and purchased
   `compute-flexible-commitment-2` only a week ago, then Google Cloud
   first utilizes `compute-flexible-commitment-1`.
3. **Higher discount rates first**: Within a single compute flexible
   commitment, if you have eligible usage from multiple resource or service
   types, then the commitment first covers the usage that receives the
   highest discount off on-demand prices.

   *Example*: Suppose that you have a 3-year compute flexible commitment to
   cover H3 VM usage (which qualifies for 38% CUDs) and
   Cloud Run functions usage (which qualifies for 17% CUDs). In
   this scenario, your compute flexible commitment first covers your H3 usage
   and then covers your Cloud Run functions usage.
4. **Proportional distribution**: After applying all the preceding criteria,
   if there's any remaining portion of a compute flexible commitment,
   then Google Cloud applies that across Compute Engine,
   GKE, and Cloud Run in proportion to the remaining
   eligible spend for each service. After Google Cloud fully utilizes
   the compute flexible commitment, if any eligible usage still remains, then
   Google Cloud uses these criteria again to check for another compute
   flexible commitment to cover that usage.

   *Example*: Consider a scenario where Google Cloud applied all the
   preceding criteria and you still have a portion of your compute flexible
   commitment and some eligible usage remaining. Your commitment can cover
   another US$100 worth of on-demand spend and the on-demand cost for your
   remaining eligible usage is US$150. Suppose the US$150 of on-demand spend
   is distributed as follows: US$75 for Compute Engine, US$37.50 for
   GKE, and US$37.50 for Cloud Run. The ratio
   of the on-demand spend across these services is 2:1:1. In this scenario,
   Google Cloud utilizes the remaining US$100 from your commitment to
   cover this usage in the same 2:1:1 ratio. This distribution means that
   Google Cloud utilizes your commitment in the following way:

   - covers US$50 worth of Compute Engine usage.
   - covers US$25 worth of GKE usage.
   - covers US$25 worth of Cloud Run usage.

   If your Cloud Billing account has other compute flexible
   commitments, then Google Cloud utilizes those commitments to cover
   the remaining US$50 worth of on-demand spend.

#### Usage costs on your cost data exports

For resource usage that is covered by your commitment, the resource costs
appear on your cost data exports in the following way:

- In the `SKU` column, you see the on-demand SKU name for the resource.
- In the `Effective price` column, you see the discounted price of that SKU.
- In the `Consumption model` column, you see one of these values,
  depending on your commitment's term: `Compute Flexible CUDs - 1 Year` or
  `Compute Flexible CUDs - 3 Year`.

Your hourly commitment fee appears as a charge on the cost data exports in
the following way:

- In the `SKU` column, you see the value `Commitment Fee SKU`.
- In the `cost` column, you see the hourly commitment fee value.
- In the `Credits` column, you see the resource usage costs that were
  covered by your commitment fee. This credit offsets your commitment fee
  for the used portion of your commitment. When your commitment is fully
  utilized, the credit matches the commitment fee.

Any overage usage appears on your cost data exports in the following way:

- In the `SKU` column, you see the on-demand SKU name for your resource.
- In the `Effective price` column, you see the on-demand price of that SKU.
- In the `Consumption model` column, you see `Default` as the value.

For detailed information about your cost data exports and how to interpret
charges, see
Spend-based CUDs data model updates.

### Examples of compute flexible commitments

The following examples show how you receive compute flexible CUDs based on
whether your eligible Google Cloud spend is limited to
Compute Engine or spans across Compute Engine,
GKE, and Cloud Run.

#### Spend limited to Compute Engine

Consider a scenario where your eligible Google Cloud spend is limited to
Compute Engine.
Suppose that your Cloud Billing account has
multiple projects with VM instances that belong to N2, N2D, and C2 machine
series, and are located in the `us-central1` and `us-east1` regions. The
following example explains how you receive compute flexible CUDs for this
commitment:

Suppose you purchase a compute flexible commitment for this
Cloud Billing account and commit to a US$100 per hour spend for a
3-year term. The following points explain how this example compute flexible
commitment works:

- You commit to a US$100 hourly spend. This amount becomes your hourly
  commitment fee. Because you chose a 3-year term, you receive eligible N2,
  N2D, and C2 resources at a 46% discount off on-demand prices.
- Every hour during your commitment's duration, your commitment fee covers
  up to US$100 worth of your discounted N2, N2D, and C2 usage costs.
- You get discounted prices for your hourly usage on vCPUs, memory, or
  Local SSD disks from any N2, N2D, and C2 instances across `us-central1`
  and `us-east1` regions, until you fully use your commitment.
- Essentially, your commitment fee can cover eligible N2, N2D, and C2
  resources that are worth an on-demand price of up to US$185.19 per hour
  (US$100 / (1 - 0.46)).
- If you use hourly resources with an on-demand price of US$50, then the
  discounted cost of these resources is US$27 (US$50 \* (1 - 0.46)). This
  usage is covered by your commitment fee. You still pay the US$100 fee, and
  the unused portion of your commitment (US$73) is not rolled over.
- If you use hourly resources with an on-demand price of US$200, then the
  first US$185.19 of usage is covered by your commitment. The discounted
  cost is US$100, which is offset by your commitment fee. The remaining
  US$14.81 of usage is considered overage and is billed at on-demand rates.
  Your total hourly cost is US$100 (commitment amount) + US$14.81 (overage)
  = US$114.81.

#### Spend beyond Compute Engine

Consider a scenario where your eligible Google Cloud spend spans across
Compute Engine,
GKE, and Cloud Run.

Suppose that you purchase a compute flexible commitment for your
Cloud Billing account where you commit to spending US$100 per hour on
Google Cloud services, on a 3-year term. Suppose that your usage spans the
following resources and services:

- **Compute Engine**: N2
  machine series vCPUs and memory
- **GKE**: Google Kubernetes Engine (GKE) Standard edition
- **Cloud Run**: Cloud Run services with instance-based
  billing

The following example explains how you receive compute flexible CUDs for this
commitment:

In return for your commitment, you receive a 46% discount off on-demand prices
for your eligible usage across Compute Engine, GKE, and
Cloud Run. Your US$100/hour commitment fee covers eligible
usage with an on-demand price of up to US$185.19 per hour (US$100 / (1 - 0.46)).

Now suppose that during a given hour, your resource usage is equivalent to the
following on-demand spend:

- **Compute Engine**: US$200 on
  N2
  vCPUs and memory
- **GKE**: US$100 on Google Kubernetes Engine (GKE) Standard edition
- **Cloud Run**: US$100 on Cloud Run services with
  instance-based billing

  Without the commitment, your total on-demand spend would have been US$400.
  The commitment covers US$185.19 of this spend. To distribute the discount,
  Google Cloud uses the ratio of eligible spend across the three services
  (2:1:1). The covered on-demand spend is distributed as follows:
- **Compute Engine**: US$92.60 (which is half of US$185.19)
- **GKE**: US$46.30 (which is a quarter of US$185.19)
- **Cloud Run**: US$46.30 (which is a quarter of US$185.19)

  The discounted cost for this covered usage is US$100, which is paid for by
  your commitment fee. The remaining usage is considered overage and is billed
  at on-demand rates, which is as follows:
- **Compute Engine**: US$107.40 (US$200 - US$92.60)
- **GKE**: US$53.70 (US$100 - US$46.30)
- **Cloud Run**: US$53.70 (US$100 - US$46.30)

  Your total hourly cost is US$100 (commitment fee) + US$214.80 (total overage)
  = US$314.80.

### Capacity reservations for GPUs

Unlike resource-based commitments, compute flexible commitments don't support
attached reservations and don't offer the assured capacity that comes with
attached reservations.

If you want to reserve capacity for G2 or G4 GPUs, then you must create a
standalone reservation for those resources. If your project has access to any
shared reservations from the same Cloud Billing account, then you can
also consume capacity from those reservations. Your compute flexible commitments
still apply to usage that consumes those reservations,
provided that the spend is eligible.

If resources of a specific type are unavailable in a specific location,
then Google Cloud provides you with the flexibility to use your compute
flexible commitment to cover any of the following:

- Resources of the same type that are located in other zones and regions
- Other resources and services that are supported by compute flexible CUDs

This flexibility maximizes the utilization of your compute flexible commitments.
For G2 and G4 GPUs instances, this flexibility lets you do the following:

- **Change locations**: If capacity is unavailable in your preferred zone or
  region, then you can deploy your compute instances in another available
  location and still receive applicable compute flexible CUDs.
- **Switch GPU machine types**: You can apply the same compute flexible
  commitment to either G2 or G4 instances. If capacity for one GPU machine
  type (for example, G2) isn't available, then you can use the commitment
  to cover the other GPU machine type.
- **Cover other services**: If no GPU capacity is available, then your commitment
  can still cover eligible spend on other supported resources (like vCPUs and memory)
  or services (such as GKE and Cloud Run).

### Purchase compute flexible commitments

You can purchase compute flexible commitments only at a Cloud Billing
account level.

For more information about how to
purchase a compute flexible commitment, see
Purchasing spend-based commitments.

Before you purchase a commitment, read the
Service Specific Terms.

After you purchase a commitment, you can't cancel it. For more information, see
Cancel commitments.

## Order of discount application

You can purchase both resource-based and compute flexible commitments to cover
Compute Engine resources for projects within your Cloud Billing
account. You can use your resource-based commitments to cover your predictable
and stable resource usage that is specific to a project, region, and machine
configuration. If CUD sharing is enabled, then your resource-based commitments
also cover eligible usage for that region and machine configuration across other
projects in that Cloud Billing account. You can use compute flexible
commitments to cover any resource usage that isn't specific to any one region,
project, or machine configuration.

However, the discount types that Google Cloud offers on your
Compute Engine resources are mutually exclusive and can't be combined.
At any given point, a resource is eligible for only one kind of discount. If
you're receiving a specific type of discount for a portion of your resource
usage, then that portion of usage doesn't qualify for any other type of discount.

If you purchase both resource-based and compute flexible commitments for your
Compute Engine resources, then Google Cloud applies your
commitments, on an hourly basis, according to the following order:

1. Google Cloud first utilizes your resource-based commitments and
   applies all the resulting resource-based CUDs to any eligible hourly usage.
   For detailed information about how resource-based CUDs apply to your usage,
   see the
   Resource-based CUDs document.
2. Google Cloud then utilizes your compute flexible commitments to
   cover any eligible usage that wasn't already covered by resource-based
   commitments. Note that portions of your compute flexible commitment might
   also cover eligible usage across GKE and Cloud Run.
   For detailed information about how compute flexible commitments cover your
   usage, see
   Commitment utilization criteria.
3. After utilizing all of your commitments, Google Cloud uses the
   on-demand rates to charge any additional hourly usage. This overage hourly
   usage might be eligible for any applicable
   sustained use discounts (SUDs).

## Limitations

- Resource-based CUDs are available only for resources that are
  deployed using Compute Engine SKUs, which include VMs that are used
  by Compute Engine, Google Kubernetes Engine, Managed Service for Apache Spark,
  Managed Service for Apache Airflow 1, or Vertex AI.
- Compute flexible CUDs are available only for
  Compute Engine, Google Kubernetes Engine,
  and Cloud Run. For the full list of eligible SKUs, see
  SKU Groups - Compute Flexible CUD Eligible
  SKUs.
- If you use your Compute Engine
  reservations with
  Managed Service for Apache Spark, then those reserved resources aren't eligible
  for resource-based CUDs.
- If you use your reservations with Dataflow, then you can
  receive resource-based CUDs only for usage from
  specifically targeted reservations
  that specify accelerators (GPUs or TPUs).
- You can purchase compute flexible commitments only at a
  Cloud Billing account level.
- For GPUs, you can purchase compute flexible commitments only for GPUs that
  are used with G2 and G4 machine series. For all other machine series, only
  memory, vCPUs, and Local SSD resources are eligible for compute flexible
  CUDs. If you use these eligible resources with any sole-tenant nodes, then
  the resulting sole-tenancy premium is also eligible.
- You can't use your compute flexible commitments for
  Spot VMs or
  preemptible VMs.
- For memory-optimized VMs, compute flexible CUDs are available only for
  3-year commitments. If you purchase a 1-year compute flexible commitment,
  then you don't receive any discounts for your spend on memory-optimized VMs.

## What's next

- Learn more about
  Compute Engine resource-based commitments.
- Browse the
  pricing tables for Compute Engine machine families
  for information about their on-demand prices, resource-based commitment
  prices, and compute flexible CUD consumption rates.
- Learn about CUD analysis reports.
- Learn how to
  analyze the cost effectiveness of your CUDs.
- Learn more about
  CUDs for other Google Cloud services.
