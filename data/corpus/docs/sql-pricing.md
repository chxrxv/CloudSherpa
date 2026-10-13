---
doc_id: sql-pricing
title: Cloud SQL pricing
url: https://cloud.google.com/sql/pricing
category: pricing
fetched_at: '2026-10-13T15:13:49+00:00'
license: CC BY 4.0 (Google Cloud documentation)
---

## Cloud SQL pricing

You can create an account to evaluate how Cloud SQL performs in real-world scenarios. New customers also get $300 in free credits to spend on Cloud SQL to run, test, and deploy workloads. You won't be charged until you upgrade.

Sign up to try Cloud SQL for free.

This page contains information about pricing for Cloud SQL.

Cloud SQL offers two editions, Enterprise and Enterprise Plus. These editions provide different levels of availability, performance and data protection. The pricing for the vCPUs and memory for each edition varies. Cloud SQL Enterprise edition and Cloud SQL Enterprise Plus edition are supported by Cloud SQL for MySQL, Cloud SQL for PostgreSQL, and Cloud SQL for SQL Server.

Pricing for Cloud SQL depends on your instance type:

- MySQL and PostgreSQL
- SQL Server

## MySQL and PostgreSQL pricing

Cloud SQL pricing is composed of the following charges:

- CPU and memory pricing
- Storage and networking pricing
- Instance pricing
- Cloud DNS pricing
- Extended support pricing

### CPU and memory pricing

For dedicated-core instances, you choose the number of CPUs and the amount of memory you want, up to 96 CPUs and 624 GiB of memory for Enterprise edition and up to 128 CPUs and 864 GiB of memory for Enterprise Plus edition. For Cloud SQL Enterprise Plus edition for SQL Server instances, you can also choose from performance-optimized machines (up to 128 CPUs and 864 GiB of memory) and memory-optimized machines (up to 16 CPUs and 512 GiB of memory). Pricing for CPUs and memory depends on the region where your instance is located. Select your region in the dropdown on the pricing table.

Read replicas and failover replicas are charged at the same rate as stand-alone instances.

*HA* prices are applied for instances configured for high availability, also called regional instances. Learn more about high availability.

Cloud SQL also offers committed use discounts (CUDs) that provide deeply discounted prices in exchange for your commitment to continuously use database instances in a particular region for a one- or three-year term. In the pricing tables on this page, the prices for CUDs are listed as commitments. For more information about these commitments, see Committed use discounts.

In the following tables:

- Select your region from the dropdown menu to see the price for that region
- Use the slider to choose **Monthly** or **Hourly** pricing
- Compare pricing between per use, 1-year, and 3-year commitments

### Enterprise edition - General Purpose machine series

Iowa (us-central1)

- Johannesburg (africa-south1)
- Taiwan (asia-east1)
- Hong Kong (asia-east2)
- Tokyo (asia-northeast1)
- Osaka (asia-northeast2)
- Seoul (asia-northeast3)
- Mumbai (asia-south1)
- Delhi (asia-south2)
- Singapore (asia-southeast1)
- Jakarta (asia-southeast2)
- Bangkok (asia-southeast3)
- Sydney (australia-southeast1)
- Melbourne (australia-southeast2)
- Warsaw (europe-central2)
- Finland (europe-north1)
- Stockholm (europe-north2)
- Madrid (europe-southwest1)
- Belgium (europe-west1)
- Berlin (europe-west10)
- Turin (europe-west12)
- London (europe-west2)
- Frankfurt (europe-west3)
- Netherlands (europe-west4)
- Zurich (europe-west6)
- Milan (europe-west8)
- Paris (europe-west9)
- Doha (me-central1)
- Dammam (me-central2)
- Tel Aviv (me-west1)
- Montreal (northamerica-northeast1)
- Toronto (northamerica-northeast2)
- Mexico (northamerica-south1)
- Sao Paulo (southamerica-east1)
- Santiago (southamerica-west1)
- Iowa (us-central1)
- South Carolina (us-east1)
- Northern Virginia (us-east4)
- Columbus (us-east5)
- Alabama (us-east7)
- Dallas (us-south1)
- Oregon (us-west1)
- Los Angeles (us-west2)
- Salt Lake City (us-west3)
- Las Vegas (us-west4)
- Phoenix (us-west8)

Show discount options

|  | Price (USD) \* | Cloud SQL CUD - 1 Year\* (USD) | Cloud SQL CUD - 3 Year\* (USD) |
| --- | --- | --- | --- |
|  |  |  |  |
| --- | --- | --- | --- |
| vCPUs | $0.0413 / 1 hour | $0.030975 / 1 hour | $0.019824 / 1 hour |
| Memory | $0.007 / 1 gibibyte hour | $0.00525 / 1 gibibyte hour | $0.00336 / 1 gibibyte hour |
| HA vCPUs | $0.0826 / 1 hour | $0.06195 / 1 hour | $0.039648 / 1 hour |
| HA Memory | $0.014 / 1 gibibyte hour | $0.0105 / 1 gibibyte hour | $0.00672 / 1 gibibyte hour |

\* Each consumption model has a unique ID. You may need to opt-in to be eligible for consumption model discounts. Click here to learn more.

If you pay in a currency other than USD, the prices listed in your currency on Cloud Platform SKUs apply.

### Enterprise Edition - N4 machine series

Iowa (us-central1)

- Johannesburg (africa-south1)
- Taiwan (asia-east1)
- Hong Kong (asia-east2)
- Tokyo (asia-northeast1)
- Osaka (asia-northeast2)
- Seoul (asia-northeast3)
- Mumbai (asia-south1)
- Delhi (asia-south2)
- Singapore (asia-southeast1)
- Jakarta (asia-southeast2)
- Sydney (australia-southeast1)
- Melbourne (australia-southeast2)
- Warsaw (europe-central2)
- Finland (europe-north1)
- Stockholm (europe-north2)
- Madrid (europe-southwest1)
- Belgium (europe-west1)
- Berlin (europe-west10)
- Turin (europe-west12)
- London (europe-west2)
- Frankfurt (europe-west3)
- Netherlands (europe-west4)
- Zurich (europe-west6)
- Milan (europe-west8)
- Paris (europe-west9)
- Doha (me-central1)
- Dammam (me-central2)
- Tel Aviv (me-west1)
- Montreal (northamerica-northeast1)
- Toronto (northamerica-northeast2)
- Mexico (northamerica-south1)
- Sao Paulo (southamerica-east1)
- Santiago (southamerica-west1)
- Iowa (us-central1)
- Oklahoma (us-central2)
- South Carolina (us-east1)
- Northern Virginia (us-east4)
- Columbus (us-east5)
- Alabama (us-east7)
- Dallas (us-south1)
- Oregon (us-west1)
- Los Angeles (us-west2)
- Salt Lake City (us-west3)
- Las Vegas (us-west4)
- Phoenix (us-west8)

Show discount options

|  | Price (USD) \* | Cloud SQL CUD - 1 Year\* (USD) | Cloud SQL CUD - 3 Year\* (USD) |
| --- | --- | --- | --- |
|  |  |  |  |
| --- | --- | --- | --- |
| vCPUs | $0.0413 / 1 hour | $0.030975 / 1 hour | $0.019824 / 1 hour |
| Memory | $0.007 / 1 gibibyte hour | $0.00525 / 1 gibibyte hour | $0.00336 / 1 gibibyte hour |
| HA vCPUs | $0.0826 / 1 hour | $0.06195 / 1 hour | $0.039648 / 1 hour |
| HA Memory | $0.014 / 1 gibibyte hour | $0.0105 / 1 gibibyte hour | $0.00672 / 1 gibibyte hour |

\* Each consumption model has a unique ID. You may need to opt-in to be eligible for consumption model discounts. Click here to learn more.

If you pay in a currency other than USD, the prices listed in your currency on Cloud Platform SKUs apply.

### Enterprise Plus edition - C4 machine series

Iowa (us-central1)

- Johannesburg (africa-south1)
- Taiwan (asia-east1)
- Hong Kong (asia-east2)
- Tokyo (asia-northeast1)
- Osaka (asia-northeast2)
- Seoul (asia-northeast3)
- Mumbai (asia-south1)
- Delhi (asia-south2)
- Singapore (asia-southeast1)
- Jakarta (asia-southeast2)
- Bangkok (asia-southeast3)
- Sydney (australia-southeast1)
- Melbourne (australia-southeast2)
- Warsaw (europe-central2)
- Finland (europe-north1)
- Stockholm (europe-north2)
- Madrid (europe-southwest1)
- Belgium (europe-west1)
- Berlin (europe-west10)
- Turin (europe-west12)
- London (europe-west2)
- Frankfurt (europe-west3)
- Netherlands (europe-west4)
- Zurich (europe-west6)
- Milan (europe-west8)
- Paris (europe-west9)
- Doha (me-central1)
- Dammam (me-central2)
- Tel Aviv (me-west1)
- Montreal (northamerica-northeast1)
- Toronto (northamerica-northeast2)
- Mexico (northamerica-south1)
- Sao Paulo (southamerica-east1)
- Santiago (southamerica-west1)
- Iowa (us-central1)
- Oklahoma (us-central2)
- South Carolina (us-east1)
- Northern Virginia (us-east4)
- Columbus (us-east5)
- Alabama (us-east7)
- Dallas (us-south1)
- Oregon (us-west1)
- Los Angeles (us-west2)
- Salt Lake City (us-west3)
- Las Vegas (us-west4)
- Phoenix (us-west8)

Show discount options

|  | Price (USD) \* | Cloud SQL CUD - 1 Year\* (USD) | Cloud SQL CUD - 3 Year\* (USD) |
| --- | --- | --- | --- |
|  |  |  |  |
| --- | --- | --- | --- |
| vCPUs | $0.054 / 1 hour | $0.0405 / 1 hour | $0.02592 / 1 hour |
| Memory | $0.009 / 1 gibibyte hour | $0.00675 / 1 gibibyte hour | $0.00432 / 1 gibibyte hour |
| HA vCPUs | $0.108 / 1 hour | $0.081 / 1 hour | $0.05184 / 1 hour |
| HA Memory | $0.018 / 1 gibibyte hour | $0.0135 / 1 gibibyte hour | $0.00864 / 1 gibibyte hour |
| Data Cache Storage | $0.000287671 / 1 gibibyte hour | - | - |
| HA Data Cache Storage | $0.000575342 / 1 gibibyte hour | - | - |

\* Each consumption model has a unique ID. You may need to opt-in to be eligible for consumption model discounts. Click here to learn more.

If you pay in a currency other than USD, the prices listed in your currency on Cloud Platform SKUs apply.

### Enterprise Plus edition - N2 machine series

Iowa (us-central1)

- Johannesburg (africa-south1)
- Taiwan (asia-east1)
- Hong Kong (asia-east2)
- Tokyo (asia-northeast1)
- Osaka (asia-northeast2)
- Seoul (asia-northeast3)
- Mumbai (asia-south1)
- Delhi (asia-south2)
- Singapore (asia-southeast1)
- Jakarta (asia-southeast2)
- Bangkok (asia-southeast3)
- Sydney (australia-southeast1)
- Melbourne (australia-southeast2)
- Warsaw (europe-central2)
- Finland (europe-north1)
- Stockholm (europe-north2)
- Madrid (europe-southwest1)
- Belgium (europe-west1)
- Berlin (europe-west10)
- Turin (europe-west12)
- London (europe-west2)
- Frankfurt (europe-west3)
- Netherlands (europe-west4)
- Zurich (europe-west6)
- Milan (europe-west8)
- Paris (europe-west9)
- Doha (me-central1)
- Dammam (me-central2)
- Tel Aviv (me-west1)
- Montreal (northamerica-northeast1)
- Toronto (northamerica-northeast2)
- Mexico (northamerica-south1)
- Sao Paulo (southamerica-east1)
- Santiago (southamerica-west1)
- Iowa (us-central1)
- Oklahoma (us-central2)
- South Carolina (us-east1)
- Northern Virginia (us-east4)
- Columbus (us-east5)
- Alabama (us-east7)
- Dallas (us-south1)
- Oregon (us-west1)
- Los Angeles (us-west2)
- Salt Lake City (us-west3)
- Las Vegas (us-west4)
- Phoenix (us-west8)

Show discount options

|  | Price (USD) \* | Cloud SQL CUD - 1 Year\* (USD) | Cloud SQL CUD - 3 Year\* (USD) |
| --- | --- | --- | --- |
|  |  |  |  |
| --- | --- | --- | --- |
| vCPUs | $0.0537 / 1 hour | $0.040275 / 1 hour | $0.025776 / 1 hour |
| Memory | $0.0091 / 1 gibibyte hour | $0.006825 / 1 gibibyte hour | $0.004368 / 1 gibibyte hour |
| HA vCPUs | $0.1074 / 1 hour | $0.08055 / 1 hour | $0.051552 / 1 hour |
| HA Memory | $0.0182 / 1 gibibyte hour | $0.01365 / 1 gibibyte hour | $0.008736 / 1 gibibyte hour |
| Data Cache Storage | $0.000219178 / 1 gibibyte hour | - | - |
| HA Data Cache Storage | $0.000438356 / 1 gibibyte hour | - | - |

\* Each consumption model has a unique ID. You may need to opt-in to be eligible for consumption model discounts. Click here to learn more.

If you pay in a currency other than USD, the prices listed in your currency on Cloud Platform SKUs apply.

### Enterprise Plus edition - C4A machine series

Iowa (us-central1)

- Taiwan (asia-east1)
- Hong Kong (asia-east2)
- Tokyo (asia-northeast1)
- Osaka (asia-northeast2)
- Seoul (asia-northeast3)
- Mumbai (asia-south1)
- Delhi (asia-south2)
- Singapore (asia-southeast1)
- Jakarta (asia-southeast2)
- Bangkok (asia-southeast3)
- Sydney (australia-southeast1)
- Melbourne (australia-southeast2)
- Warsaw (europe-central2)
- Finland (europe-north1)
- Stockholm (europe-north2)
- Madrid (europe-southwest1)
- Belgium (europe-west1)
- Berlin (europe-west10)
- Turin (europe-west12)
- London (europe-west2)
- Frankfurt (europe-west3)
- Netherlands (europe-west4)
- Zurich (europe-west6)
- Milan (europe-west8)
- Paris (europe-west9)
- Doha (me-central1)
- Dammam (me-central2)
- Tel Aviv (me-west1)
- Montreal (northamerica-northeast1)
- Toronto (northamerica-northeast2)
- Sao Paulo (southamerica-east1)
- Santiago (southamerica-west1)
- Iowa (us-central1)
- Oklahoma (us-central2)
- South Carolina (us-east1)
- Northern Virginia (us-east4)
- Columbus (us-east5)
- Alabama (us-east7)
- Dallas (us-south1)
- Oregon (us-west1)
- Los Angeles (us-west2)
- Salt Lake City (us-west3)
- Las Vegas (us-west4)
- Phoenix (us-west8)

Show discount options

|  | Price (USD) \* | Cloud SQL CUD - 1 Year\* (USD) | Cloud SQL CUD - 3 Year\* (USD) |
| --- | --- | --- | --- |
|  |  |  |  |
| --- | --- | --- | --- |
| vCPUs | $0.0537 / 1 hour | $0.040275 / 1 hour | $0.025776 / 1 hour |
| Memory | $0.0091 / 1 gibibyte hour | $0.006825 / 1 gibibyte hour | $0.004368 / 1 gibibyte hour |
| HA vCPUs | $0.1074 / 1 hour | $0.08055 / 1 hour | $0.051552 / 1 hour |
| HA Memory | $0.0182 / 1 gibibyte hour | $0.01365 / 1 gibibyte hour | $0.008736 / 1 gibibyte hour |
| Data Cache Storage | $0.000219178 / 1 gibibyte hour | - | - |
| HA Data Cache Storage | $0.000438356 / 1 gibibyte hour | - | - |

\* Each consumption model has a unique ID. You may need to opt-in to be eligible for consumption model discounts. Click here to learn more.

If you pay in a currency other than USD, the prices listed in your currency on Cloud Platform SKUs apply.

### Storage and networking pricing

Storage and networking prices depend on the region where the instance is located. Select your region in the dropdown on the pricing table.

*HA* prices are applied for instances configured for high availability, also called regional instances. Learn more about high availability.

With Hyperdisk Balanced you are billed for provisioned capacity, IOPS and throughput independently. You are billed for the total provisioned capacity of your Hyperdisk Balanced volumes until you delete them. You are charged per GiB per month. Hyperdisk Balanced charges a monthly rate for the provisioned IOPS and provisioned throughput (in MBps) in excess of the baseline values of 3,000 IOPS and 140 MBps throughput.

**Note:** Committed use discounts do not apply to storage or network prices.

In the following tables, Select your region from the dropdown menu to see the price for that region.

### Storage

Iowa (us-central1)

- Johannesburg (africa-south1)
- Taiwan (asia-east1)
- Hong Kong (asia-east2)
- Tokyo (asia-northeast1)
- Osaka (asia-northeast2)
- Seoul (asia-northeast3)
- Mumbai (asia-south1)
- Delhi (asia-south2)
- Singapore (asia-southeast1)
- Jakarta (asia-southeast2)
- Bangkok (asia-southeast3)
- Sydney (australia-southeast1)
- Melbourne (australia-southeast2)
- Warsaw (europe-central2)
- Finland (europe-north1)
- Madrid (europe-southwest1)
- Belgium (europe-west1)
- Berlin (europe-west10)
- Turin (europe-west12)
- London (europe-west2)
- Frankfurt (europe-west3)
- Netherlands (europe-west4)
- Zurich (europe-west6)
- Milan (europe-west8)
- Paris (europe-west9)
- Doha (me-central1)
- Dammam (me-central2)
- Tel Aviv (me-west1)
- Montreal (northamerica-northeast1)
- Toronto (northamerica-northeast2)
- Mexico (northamerica-south1)
- Sao Paulo (southamerica-east1)
- Santiago (southamerica-west1)
- Iowa (us-central1)
- South Carolina (us-east1)
- Northern Virginia (us-east4)
- Columbus (us-east5)
- Alabama (us-east7)
- Dallas (us-south1)
- Oregon (us-west1)
- Los Angeles (us-west2)
- Salt Lake City (us-west3)
- Las Vegas (us-west4)
- Phoenix (us-west8)

| Item | Price (USD) |
| --- | --- |
|  |  |
| --- | --- |
| SSD storage capacity | $0.000232877 / 1 gibibyte hour |
| HDD storage capacity | $0.000123288 / 1 gibibyte hour |
| Backups (used) | $0.000109589 / 1 gibibyte hour |
| Hyperdisk Balanced Capacity | $0.000157534 / 1 gibibyte hour |
| Hyperdisk Balanced IOPS | $0.000027397 / 1 hour |
| Hyperdisk Balanced Throughput | $0.000109589 / 1 hour |

If you pay in a currency other than USD, the prices listed in your currency on Cloud Platform SKUs apply.

### HA Storage

Iowa (us-central1)

- Johannesburg (africa-south1)
- Taiwan (asia-east1)
- Hong Kong (asia-east2)
- Tokyo (asia-northeast1)
- Osaka (asia-northeast2)
- Seoul (asia-northeast3)
- Mumbai (asia-south1)
- Delhi (asia-south2)
- Singapore (asia-southeast1)
- Jakarta (asia-southeast2)
- Bangkok (asia-southeast3)
- Sydney (australia-southeast1)
- Melbourne (australia-southeast2)
- Warsaw (europe-central2)
- Finland (europe-north1)
- Madrid (europe-southwest1)
- Belgium (europe-west1)
- Berlin (europe-west10)
- Turin (europe-west12)
- London (europe-west2)
- Frankfurt (europe-west3)
- Netherlands (europe-west4)
- Zurich (europe-west6)
- Milan (europe-west8)
- Paris (europe-west9)
- Doha (me-central1)
- Dammam (me-central2)
- Tel Aviv (me-west1)
- Montreal (northamerica-northeast1)
- Toronto (northamerica-northeast2)
- Mexico (northamerica-south1)
- Sao Paulo (southamerica-east1)
- Santiago (southamerica-west1)
- Iowa (us-central1)
- South Carolina (us-east1)
- Northern Virginia (us-east4)
- Columbus (us-east5)
- Alabama (us-east7)
- Dallas (us-south1)
- Oregon (us-west1)
- Los Angeles (us-west2)
- Salt Lake City (us-west3)
- Las Vegas (us-west4)
- Phoenix (us-west8)

| Item | Price (USD) |
| --- | --- |
|  |  |
| --- | --- |
| SSD storage capacity | $0.000465753 / 1 gibibyte hour |
| HDD storage capacity | $0.000246575 / 1 gibibyte hour |
| Backups (used) | $0.000109589 / 1 gibibyte hour |
| Hyperdisk Balanced HA Capacity | $0.000315068 / 1 gibibyte hour |
| Hyperdisk Balanced HA IOPS | $0.000054795 / 1 hour |
| Hyperdisk Balanced HA Throughput | $0.000219178 / 1 hour |

If you pay in a currency other than USD, the prices listed in your currency on Cloud Platform SKUs apply.

### Network

Iowa (us-central1)

- Johannesburg (africa-south1)
- Taiwan (asia-east1)
- Hong Kong (asia-east2)
- Tokyo (asia-northeast1)
- Osaka (asia-northeast2)
- Seoul (asia-northeast3)
- Mumbai (asia-south1)
- Delhi (asia-south2)
- Singapore (asia-southeast1)
- Jakarta (asia-southeast2)
- Bangkok (asia-southeast3)
- Sydney (australia-southeast1)
- Melbourne (australia-southeast2)
- Warsaw (europe-central2)
- Finland (europe-north1)
- Stockholm (europe-north2)
- Madrid (europe-southwest1)
- Belgium (europe-west1)
- Berlin (europe-west10)
- Turin (europe-west12)
- London (europe-west2)
- Frankfurt (europe-west3)
- Netherlands (europe-west4)
- Zurich (europe-west6)
- Milan (europe-west8)
- Paris (europe-west9)
- Doha (me-central1)
- Dammam (me-central2)
- Tel Aviv (me-west1)
- Montreal (northamerica-northeast1)
- Toronto (northamerica-northeast2)
- Mexico (northamerica-south1)
- Sao Paulo (southamerica-east1)
- Santiago (southamerica-west1)
- Iowa (us-central1)
- South Carolina (us-east1)
- Northern Virginia (us-east4)
- Columbus (us-east5)
- Alabama (us-east7)
- Dallas (us-south1)
- Oregon (us-west1)
- Los Angeles (us-west2)
- Salt Lake City (us-west3)
- Las Vegas (us-west4)
- Phoenix (us-west8)

| Item | Price (USD) |
| --- | --- |
|  |  |
| --- | --- |
| Ingress to Cloud SQL | Free  **Note**: Egress charges may apply on the source. For example, egress from Compute Engine is charged at the external IP addresses rate. |
| Egress from Cloud SQL | Egress from Cloud SQL: See Network Egress Pricing. |
| IPv4 addresses while idle | $0.01 / 1 hour |

If you pay in a currency other than USD, the prices listed in your currency on Cloud Platform SKUs apply.

### Network Egress Pricing

When network traffic leaves a Cloud SQL instance, the charge applied depends on the destination of the traffic, and in some cases, whether a partner is involved.

Internet egress is network traffic leaving a Cloud SQL instance to a client that is not a Google product, such as using a local server to read data from Cloud SQL.

| Destination | Price (USD) |
| --- | --- |
|  |  |
| --- | --- |
| Compute Engine instances and Cloud SQL cross-region replicas | Within the same region: free  Between regions within North America: $0.12/GiB  Between regions outside of North America: $0.12/GiB |
| Google Products (except Compute Engine and traffic to Cloud SQL cross-region replicas) | Intra-continental: free  Inter-continental: $0.12/GiB |
| Internet egress using Cloud Interconnect | $0.05/GiB |
| Internet egress (not using Cloud Interconnect) | $0.19/GiB |

If you pay in a currency other than USD, the prices listed in your currency on Cloud Platform SKUs apply.

### Instance pricing

Instance pricing applies only to shared-core instances. Dedicated-core instances, which can have up to 96 vCPUs and 624 GiB of memory, are charged by the number of cores and amount of memory they have.

Instance pricing is charged for every second that the instance is running (the activation policy is set to **ALWAYS**). Cloud SQL uses seconds as the time unit multiplier for usage. This means that each second of usage counts toward a full billable minute. For more details, see Billing on partial seconds.

*HA* prices are applied for instances configured for high availability, also called regional instances. Learn more about high availability.

**Note:** Committed use discounts do not apply to instance prices.

In the following table:

- Select your region from the dropdown menu to see the price for that region
- Use the slider to choose **Monthly** or **Hourly** pricing
- Find the machine type you want to use to view pricing details

Iowa (us-central1)

- Johannesburg (africa-south1)
- Taiwan (asia-east1)
- Hong Kong (asia-east2)
- Tokyo (asia-northeast1)
- Osaka (asia-northeast2)
- Seoul (asia-northeast3)
- Mumbai (asia-south1)
- Delhi (asia-south2)
- Singapore (asia-southeast1)
- Jakarta (asia-southeast2)
- Bangkok (asia-southeast3)
- Sydney (australia-southeast1)
- Melbourne (australia-southeast2)
- Warsaw (europe-central2)
- Finland (europe-north1)
- Stockholm (europe-north2)
- Madrid (europe-southwest1)
- Belgium (europe-west1)
- Berlin (europe-west10)
- Turin (europe-west12)
- London (europe-west2)
- Frankfurt (europe-west3)
- Netherlands (europe-west4)
- Zurich (europe-west6)
- Milan (europe-west8)
- Paris (europe-west9)
- Doha (me-central1)
- Dammam (me-central2)
- Tel Aviv (me-west1)
- Montreal (northamerica-northeast1)
- Toronto (northamerica-northeast2)
- Mexico (northamerica-south1)
- Sao Paulo (southamerica-east1)
- Santiago (southamerica-west1)
- Iowa (us-central1)
- South Carolina (us-east1)
- Northern Virginia (us-east4)
- Columbus (us-east5)
- Alabama (us-east7)
- Dallas (us-south1)
- Oregon (us-west1)
- Los Angeles (us-west2)
- Salt Lake City (us-west3)
- Las Vegas (us-west4)
- Phoenix (us-west8)

| Shared-Core Machine Type | Virtual CPUs | RAM (GiB) | Maximum Storage Capacity | Price (USD) |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| db-f1-micro\* | Shared | 0.6 | 3,062 GiB | $0.0105 / 1 hour |
| db-g1-small\* | Shared | 1.7 | 3,062 GiB | $0.035 / 1 hour |
| HA db-f1-micro\* | Shared | 0.6 | 3,062 GiB | $0.021 / 1 hour |
| HA db-g1-small\* | Shared | 1.7 | 3,062 GiB | $0.07 / 1 hour |

If you pay in a currency other than USD, the prices listed in your currency on Cloud Platform SKUs apply.

\*Shared CPU machine types (db-f1-micro and db-g1-small) are not covered by the Cloud SQL SLA.

### Billing on partial seconds

Milliseconds of usage are rounded to the nearest second. If usage is under half a second, (499ms or less), it rounds down to zero and does not count toward billable usage.

For example:

- If you use an instance for 499ms, you are not billed for that second.
- If you use an instance for 500ms or 1.49 seconds, in both cases, you are billed for 1 second.
- If you use an instance for 1.5 seconds or 2.49 seconds, in both cases you are billed for 2 seconds.

### Serverless export pricing

Serverless export prices depend on the region where the instance is located. Select your region using the dropdown on the pricing table.

**Note:** Committed use discounts don't apply to serverless export prices. If you perform frequent exports of a subset of your Cloud SQL instance (for example, by using the database, table, or query parameter), then it's more cost effective for you to create a read replica for your primary instance and perform your exports from that instance. You avoid impacting your database with your exports, and lower your costs because you're paying for the read replica only, and not for each export.

In the following table, select your region from the dropdown menu to see the price for that region

Iowa (us-central1)

- Johannesburg (africa-south1)
- Taiwan (asia-east1)
- Hong Kong (asia-east2)
- Tokyo (asia-northeast1)
- Osaka (asia-northeast2)
- Seoul (asia-northeast3)
- Mumbai (asia-south1)
- Delhi (asia-south2)
- Singapore (asia-southeast1)
- Jakarta (asia-southeast2)
- Bangkok (asia-southeast3)
- Sydney (australia-southeast1)
- Melbourne (australia-southeast2)
- Warsaw (europe-central2)
- Finland (europe-north1)
- Stockholm (europe-north2)
- Madrid (europe-southwest1)
- Belgium (europe-west1)
- Berlin (europe-west10)
- Turin (europe-west12)
- London (europe-west2)
- Frankfurt (europe-west3)
- Netherlands (europe-west4)
- Zurich (europe-west6)
- Milan (europe-west8)
- Paris (europe-west9)
- Doha (me-central1)
- Dammam (me-central2)
- Tel Aviv (me-west1)
- Montreal (northamerica-northeast1)
- Toronto (northamerica-northeast2)
- Mexico (northamerica-south1)
- Sao Paulo (southamerica-east1)
- Santiago (southamerica-west1)
- Iowa (us-central1)
- South Carolina (us-east1)
- Northern Virginia (us-east4)
- Columbus (us-east5)
- Alabama (us-east7)
- Dallas (us-south1)
- Oregon (us-west1)
- Los Angeles (us-west2)
- Salt Lake City (us-west3)
- Las Vegas (us-west4)
- Phoenix (us-west8)

| Item | Price (USD) |
| --- | --- |
|  |  |
| --- | --- |
| Serverless export pricing | $0.01 / 1 gibibyte |

**Note:** The price per GiB is calculated based on the disk size of the offload instance, which is the same as the disk size of the primary instance. This price isn't based on the amount of data exported.

### Cloud DNS pricing

With Cloud DNS pricing, the charge is per zone per month (regardless of whether you use your zone), and you also pay for queries against your zones. For more information, see Cloud DNS pricing.

### Extended support pricing

**Note:** From February 1, 2025 through April 30, 2025, Google has waived charges for extended support. Starting on May 1, 2025, all instances running on major versions that have reached end of life (EOL) will be charged for extended support.

Extended support pricing applies to Cloud SQL instances that are running major versions in extended support. Refer to the Database version policies documentation for the extended support timelines of Cloud SQL major versions.

For dedicated-core instances, extended support is priced per vCPU per hour and charged for every second that the instance is running. For shared-core instances, extended support is priced per instance per hour and charged for every second that the instance is running. Extended support is charged in addition to regular instance pricing. For more details, see Billing on partial seconds. Pricing depends on the region where your instance is located. Select your region in the dropdown on the pricing table.

Read replicas are charged at the same rate as stand-alone instances.

HA prices are applied for instances configured for high availability, also called regional instances. Learn more about high availability.

**Note:** Committed use discounts don't apply to extended support prices.

In the following table, select your region from the dropdown menu to see the price for that region.

Iowa (us-central1)

- Johannesburg (africa-south1)
- Taiwan (asia-east1)
- Hong Kong (asia-east2)
- Tokyo (asia-northeast1)
- Osaka (asia-northeast2)
- Seoul (asia-northeast3)
- Mumbai (asia-south1)
- Delhi (asia-south2)
- Singapore (asia-southeast1)
- Jakarta (asia-southeast2)
- Bangkok (asia-southeast3)
- Sydney (australia-southeast1)
- Melbourne (australia-southeast2)
- Warsaw (europe-central2)
- Finland (europe-north1)
- Stockholm (europe-north2)
- Madrid (europe-southwest1)
- Belgium (europe-west1)
- Berlin (europe-west10)
- Turin (europe-west12)
- London (europe-west2)
- Frankfurt (europe-west3)
- Netherlands (europe-west4)
- Zurich (europe-west6)
- Milan (europe-west8)
- Paris (europe-west9)
- Doha (me-central1)
- Dammam (me-central2)
- Tel Aviv (me-west1)
- Montreal (northamerica-northeast1)
- Toronto (northamerica-northeast2)
- Mexico (northamerica-south1)
- Sao Paulo (southamerica-east1)
- Santiago (southamerica-west1)
- Iowa (us-central1)
- Oklahoma (us-central2)
- South Carolina (us-east1)
- Northern Virginia (us-east4)
- Columbus (us-east5)
- Alabama (us-east7)
- Dallas (us-south1)
- Oregon (us-west1)
- Los Angeles (us-west2)
- Salt Lake City (us-west3)
- Las Vegas (us-west4)
- Phoenix (us-west8)

| Extended support price | Year 1 & Year 2 Price (USD) | Year 3 Price (USD) |
| --- | --- | --- |
|  |  |  |
| --- | --- | --- |
| vCPUs | $0.07 / 1 hour | $0.14 / 1 hour |
| HA vCPUs | $0.14 / 1 hour | $0.28 / 1 hour |
| db-f1-micro | $0.018 / 1 hour | $0.035 / 1 hour |
| HA db-f1-micro | $0.035 / 1 hour | $0.07 / 1 hour |
| db-g1-small | $0.035 / 1 hour | $0.07 / 1 hour |
| HA db-g1-small | $0.07 / 1 hour | $0.14 / 1 hour |

Extended support pricing

### Cloud SQL free trial

Cloud SQL free trial let you evaluate how Cloud SQL performs in real-world scenarios and try Cloud SQL features and capabilities at no cost for a trial period. For more details, see Cloud SQL free trial documentation page. You can upgrade from a free trial instance to a paid instance to continue using your resources beyond the free trial period and remove any free trial restrictions. If you choose to upgrade your free trial to a paid instance, you will be charged according to the pricing on this page.

## SQL Server pricing

Cloud SQL for SQL Server is composed of the following charges:

- CPU and memory pricing
- Storage and networking pricing
- Licensing
- Cloud DNS pricing

### CPU and memory pricing

For dedicated-core instances, you choose the number of CPUs and the amount of memory you want, up to 96 CPUs and 624 GiB of memory. For Cloud SQL Enterprise Plus edition instances, you can choose from Performance-optimized machines (up to 128 CPUs and 864 GiB of memory) and Memory-optimized machines (up to 16 CPUs and 512 GiB of memory). Pricing for CPUs and memory depends on the region where your instance is located. Select your region in the dropdown on the pricing table.

Read replicas and failover replicas are charged at the same rate as stand-alone instances.

*HA* prices are applied for instances configured for high availability, also called regional instances. Learn more about high availability.

Cloud SQL also offers committed use discounts (CUDs) that provide deeply discounted prices in exchange for your commitment to continuously use database instances in a particular region for a one- or three-year term. In the pricing tables on this page, the prices for CUDs are listed as commitments. For more information about these commitments, see Committed use discounts.

In the following tables:

- Select your region from the dropdown menu to see the price for that region
- Use the slider to choose **Monthly** or **Hourly** pricing
- Compare pricing between per use, 1-year, and 3-year commitments

### Enterprise edition General Purpose machine series

Iowa (us-central1)

- Johannesburg (africa-south1)
- Taiwan (asia-east1)
- Hong Kong (asia-east2)
- Tokyo (asia-northeast1)
- Osaka (asia-northeast2)
- Seoul (asia-northeast3)
- Mumbai (asia-south1)
- Delhi (asia-south2)
- Singapore (asia-southeast1)
- Jakarta (asia-southeast2)
- Sydney (australia-southeast1)
- Melbourne (australia-southeast2)
- Warsaw (europe-central2)
- Finland (europe-north1)
- Stockholm (europe-north2)
- Madrid (europe-southwest1)
- Belgium (europe-west1)
- Berlin (europe-west10)
- Turin (europe-west12)
- London (europe-west2)
- Frankfurt (europe-west3)
- Netherlands (europe-west4)
- Zurich (europe-west6)
- Milan (europe-west8)
- Paris (europe-west9)
- Doha (me-central1)
- Dammam (me-central2)
- Tel Aviv (me-west1)
- Montreal (northamerica-northeast1)
- Toronto (northamerica-northeast2)
- Mexico (northamerica-south1)
- Sao Paulo (southamerica-east1)
- Santiago (southamerica-west1)
- Iowa (us-central1)
- South Carolina (us-east1)
- Northern Virginia (us-east4)
- Columbus (us-east5)
- Alabama (us-east7)
- Dallas (us-south1)
- Oregon (us-west1)
- Los Angeles (us-west2)
- Salt Lake City (us-west3)
- Las Vegas (us-west4)
- Phoenix (us-west8)

Show discount options

|  | Price (USD) \* | Cloud SQL CUD - 1 Year\* (USD) | Cloud SQL CUD - 3 Year\* (USD) |
| --- | --- | --- | --- |
|  |  |  |  |
| --- | --- | --- | --- |
| vCPUs | $0.0413 / 1 hour | $0.030975 / 1 hour | $0.019824 / 1 hour |
| Memory | $0.007 / 1 gibibyte hour | $0.00525 / 1 gibibyte hour | $0.00336 / 1 gibibyte hour |
| HA vCPUs | $0.0826 / 1 hour | $0.06195 / 1 hour | $0.039648 / 1 hour |
| HA Memory | $0.014 / 1 gibibyte hour | $0.0105 / 1 gibibyte hour | $0.00672 / 1 gibibyte hour |

\* Each consumption model has a unique ID. You may need to opt-in to be eligible for consumption model discounts. Click here to learn more.

If you pay in a currency other than USD, the prices listed in your currency on Cloud Platform SKUs apply.

### Enterprise Edition - N4 machine series

Iowa (us-central1)

- Johannesburg (africa-south1)
- Taiwan (asia-east1)
- Hong Kong (asia-east2)
- Tokyo (asia-northeast1)
- Osaka (asia-northeast2)
- Seoul (asia-northeast3)
- Mumbai (asia-south1)
- Delhi (asia-south2)
- Singapore (asia-southeast1)
- Jakarta (asia-southeast2)
- Sydney (australia-southeast1)
- Melbourne (australia-southeast2)
- Warsaw (europe-central2)
- Finland (europe-north1)
- Stockholm (europe-north2)
- Madrid (europe-southwest1)
- Belgium (europe-west1)
- Berlin (europe-west10)
- Turin (europe-west12)
- London (europe-west2)
- Frankfurt (europe-west3)
- Netherlands (europe-west4)
- Zurich (europe-west6)
- Milan (europe-west8)
- Paris (europe-west9)
- Doha (me-central1)
- Dammam (me-central2)
- Tel Aviv (me-west1)
- Montreal (northamerica-northeast1)
- Toronto (northamerica-northeast2)
- Mexico (northamerica-south1)
- Sao Paulo (southamerica-east1)
- Santiago (southamerica-west1)
- Iowa (us-central1)
- Oklahoma (us-central2)
- South Carolina (us-east1)
- Northern Virginia (us-east4)
- Columbus (us-east5)
- Alabama (us-east7)
- Dallas (us-south1)
- Oregon (us-west1)
- Los Angeles (us-west2)
- Salt Lake City (us-west3)
- Las Vegas (us-west4)
- Phoenix (us-west8)

Show discount options

|  | Price (USD) \* | Cloud SQL CUD - 1 Year\* (USD) | Cloud SQL CUD - 3 Year\* (USD) |
| --- | --- | --- | --- |
|  |  |  |  |
| --- | --- | --- | --- |
| vCPUs | $0.0413 / 1 hour | $0.030975 / 1 hour | $0.019824 / 1 hour |
| Memory | $0.007 / 1 gibibyte hour | $0.00525 / 1 gibibyte hour | $0.00336 / 1 gibibyte hour |
| HA vCPUs | $0.0826 / 1 hour | $0.06195 / 1 hour | $0.039648 / 1 hour |
| HA Memory | $0.014 / 1 gibibyte hour | $0.0105 / 1 gibibyte hour | $0.00672 / 1 gibibyte hour |

\* Each consumption model has a unique ID. You may need to opt-in to be eligible for consumption model discounts. Click here to learn more.

If you pay in a currency other than USD, the prices listed in your currency on Cloud Platform SKUs apply.

### Enterprise Plus edition - C4 machine series

Iowa (us-central1)

- Johannesburg (africa-south1)
- Taiwan (asia-east1)
- Hong Kong (asia-east2)
- Tokyo (asia-northeast1)
- Osaka (asia-northeast2)
- Seoul (asia-northeast3)
- Mumbai (asia-south1)
- Delhi (asia-south2)
- Singapore (asia-southeast1)
- Jakarta (asia-southeast2)
- Bangkok (asia-southeast3)
- Sydney (australia-southeast1)
- Melbourne (australia-southeast2)
- Warsaw (europe-central2)
- Finland (europe-north1)
- Stockholm (europe-north2)
- Madrid (europe-southwest1)
- Belgium (europe-west1)
- Berlin (europe-west10)
- Turin (europe-west12)
- London (europe-west2)
- Frankfurt (europe-west3)
- Netherlands (europe-west4)
- Zurich (europe-west6)
- Milan (europe-west8)
- Paris (europe-west9)
- Doha (me-central1)
- Dammam (me-central2)
- Tel Aviv (me-west1)
- Montreal (northamerica-northeast1)
- Toronto (northamerica-northeast2)
- Mexico (northamerica-south1)
- Sao Paulo (southamerica-east1)
- Santiago (southamerica-west1)
- Iowa (us-central1)
- Oklahoma (us-central2)
- South Carolina (us-east1)
- Northern Virginia (us-east4)
- Columbus (us-east5)
- Alabama (us-east7)
- Dallas (us-south1)
- Oregon (us-west1)
- Los Angeles (us-west2)
- Salt Lake City (us-west3)
- Las Vegas (us-west4)
- Phoenix (us-west8)

Show discount options

|  | Price (USD) \* | Cloud SQL CUD - 1 Year\* (USD) | Cloud SQL CUD - 3 Year\* (USD) |
| --- | --- | --- | --- |
|  |  |  |  |
| --- | --- | --- | --- |
| vCPUs | $0.054 / 1 hour | $0.0405 / 1 hour | $0.02592 / 1 hour |
| Memory | $0.009 / 1 gibibyte hour | $0.00675 / 1 gibibyte hour | $0.00432 / 1 gibibyte hour |
| HA vCPUs | $0.108 / 1 hour | $0.081 / 1 hour | $0.05184 / 1 hour |
| HA Memory | $0.018 / 1 gibibyte hour | $0.0135 / 1 gibibyte hour | $0.00864 / 1 gibibyte hour |
| Data Cache Storage | $0.000287671 / 1 gibibyte hour | - | - |
| HA Data Cache Storage | $0.000575342 / 1 gibibyte hour | - | - |

\* Each consumption model has a unique ID. You may need to opt-in to be eligible for consumption model discounts. Click here to learn more.

If you pay in a currency other than USD, the prices listed in your currency on Cloud Platform SKUs apply.

### Enterprise Plus edition - N2 machine series

Iowa (us-central1)

- Johannesburg (africa-south1)
- Taiwan (asia-east1)
- Hong Kong (asia-east2)
- Tokyo (asia-northeast1)
- Osaka (asia-northeast2)
- Seoul (asia-northeast3)
- Mumbai (asia-south1)
- Delhi (asia-south2)
- Singapore (asia-southeast1)
- Jakarta (asia-southeast2)
- Bangkok (asia-southeast3)
- Sydney (australia-southeast1)
- Melbourne (australia-southeast2)
- Warsaw (europe-central2)
- Finland (europe-north1)
- Stockholm (europe-north2)
- Madrid (europe-southwest1)
- Belgium (europe-west1)
- Berlin (europe-west10)
- Turin (europe-west12)
- London (europe-west2)
- Frankfurt (europe-west3)
- Netherlands (europe-west4)
- Zurich (europe-west6)
- Milan (europe-west8)
- Paris (europe-west9)
- Doha (me-central1)
- Dammam (me-central2)
- Tel Aviv (me-west1)
- Montreal (northamerica-northeast1)
- Toronto (northamerica-northeast2)
- Mexico (northamerica-south1)
- Sao Paulo (southamerica-east1)
- Santiago (southamerica-west1)
- Iowa (us-central1)
- Oklahoma (us-central2)
- South Carolina (us-east1)
- Northern Virginia (us-east4)
- Columbus (us-east5)
- Alabama (us-east7)
- Dallas (us-south1)
- Oregon (us-west1)
- Los Angeles (us-west2)
- Salt Lake City (us-west3)
- Las Vegas (us-west4)
- Phoenix (us-west8)

Show discount options

|  | Price (USD) \* | Cloud SQL CUD - 1 Year\* (USD) | Cloud SQL CUD - 3 Year\* (USD) |
| --- | --- | --- | --- |
|  |  |  |  |
| --- | --- | --- | --- |
| vCPUs | $0.0537 / 1 hour | $0.040275 / 1 hour | $0.025776 / 1 hour |
| Memory | $0.0091 / 1 gibibyte hour | $0.006825 / 1 gibibyte hour | $0.004368 / 1 gibibyte hour |
| HA vCPUs | $0.1074 / 1 hour | $0.08055 / 1 hour | $0.051552 / 1 hour |
| HA Memory | $0.0182 / 1 gibibyte hour | $0.01365 / 1 gibibyte hour | $0.008736 / 1 gibibyte hour |
| Data Cache Storage | $0.000219178 / 1 gibibyte hour | - | - |
| HA Data Cache Storage | $0.000438356 / 1 gibibyte hour | - | - |

\* Each consumption model has a unique ID. You may need to opt-in to be eligible for consumption model discounts. Click here to learn more.

If you pay in a currency other than USD, the prices listed in your currency on Cloud Platform SKUs apply.

### Enterprise Plus edition - Memory optimized N2 machine series

Iowa (us-central1)

- Johannesburg (africa-south1)
- Taiwan (asia-east1)
- Hong Kong (asia-east2)
- Tokyo (asia-northeast1)
- Osaka (asia-northeast2)
- Seoul (asia-northeast3)
- Mumbai (asia-south1)
- Delhi (asia-south2)
- Singapore (asia-southeast1)
- Jakarta (asia-southeast2)
- Bangkok (asia-southeast3)
- Sydney (australia-southeast1)
- Melbourne (australia-southeast2)
- Warsaw (europe-central2)
- Finland (europe-north1)
- Stockholm (europe-north2)
- Madrid (europe-southwest1)
- Belgium (europe-west1)
- Berlin (europe-west10)
- Turin (europe-west12)
- London (europe-west2)
- Frankfurt (europe-west3)
- Netherlands (europe-west4)
- Zurich (europe-west6)
- Milan (europe-west8)
- Paris (europe-west9)
- Doha (me-central1)
- Dammam (me-central2)
- Tel Aviv (me-west1)
- Montreal (northamerica-northeast1)
- Toronto (northamerica-northeast2)
- Mexico (northamerica-south1)
- Sao Paulo (southamerica-east1)
- Santiago (southamerica-west1)
- Iowa (us-central1)
- Oklahoma (us-central2)
- South Carolina (us-east1)
- Northern Virginia (us-east4)
- Columbus (us-east5)
- Alabama (us-east7)
- Dallas (us-south1)
- Oregon (us-west1)
- Los Angeles (us-west2)
- Salt Lake City (us-west3)
- Las Vegas (us-west4)
- Phoenix (us-west8)

Show discount options

|  | Price (USD) \* | Cloud SQL CUD - 1 Year\* (USD) | Cloud SQL CUD - 3 Year\* (USD) |
| --- | --- | --- | --- |
|  |  |  |  |
| --- | --- | --- | --- |
| vCPUs | $0.0537 / 1 hour | $0.040275 / 1 hour | $0.025776 / 1 hour |
| Memory | $0.0161 / 1 gibibyte hour | $0.012075 / 1 gibibyte hour | $0.007728 / 1 gibibyte hour |
| HA vCPUs | $0.1074 / 1 hour | $0.08055 / 1 hour | $0.051552 / 1 hour |
| HA Memory | $0.0322 / 1 gibibyte hour | $0.02415 / 1 gibibyte hour | $0.015456 / 1 gibibyte hour |
| Data Cache Storage | $0.000219178 / 1 gibibyte hour | - | - |
| HA Data Cache Storage | $0.000438356 / 1 gibibyte hour | - | - |

\* Each consumption model has a unique ID. You may need to opt-in to be eligible for consumption model discounts. Click here to learn more.

If you pay in a currency other than USD, the prices listed in your currency on Cloud Platform SKUs apply.

### Storage and networking pricing

Storage and networking prices depend on the region where the instance is located. Select your region in the dropdown on the pricing table.

*HA* prices are applied for instances configured for high availability, also called regional instances. Learn more about high availability.

With Hyperdisk Balanced you are billed for provisioned capacity, IOPS and throughput independently. You are billed for the total provisioned capacity of your Hyperdisk Balanced volumes until you delete them. You are charged per GiB per month. Hyperdisk Balanced charges a monthly rate for the provisioned IOPS and provisioned throughput (in MBps) in excess of the baseline values of 3,000 IOPS and 140 MBps throughput.

**Note:** Committed use discounts do not apply to storage or network prices.

In the following tables, Select your region from the dropdown menu to see the price for that region.

### Storage

Iowa (us-central1)

- Johannesburg (africa-south1)
- Taiwan (asia-east1)
- Hong Kong (asia-east2)
- Tokyo (asia-northeast1)
- Osaka (asia-northeast2)
- Seoul (asia-northeast3)
- Mumbai (asia-south1)
- Delhi (asia-south2)
- Singapore (asia-southeast1)
- Jakarta (asia-southeast2)
- Sydney (australia-southeast1)
- Melbourne (australia-southeast2)
- Warsaw (europe-central2)
- Finland (europe-north1)
- Madrid (europe-southwest1)
- Belgium (europe-west1)
- Berlin (europe-west10)
- Turin (europe-west12)
- London (europe-west2)
- Frankfurt (europe-west3)
- Netherlands (europe-west4)
- Zurich (europe-west6)
- Milan (europe-west8)
- Paris (europe-west9)
- Doha (me-central1)
- Dammam (me-central2)
- Tel Aviv (me-west1)
- Montreal (northamerica-northeast1)
- Toronto (northamerica-northeast2)
- Mexico (northamerica-south1)
- Sao Paulo (southamerica-east1)
- Santiago (southamerica-west1)
- Iowa (us-central1)
- South Carolina (us-east1)
- Northern Virginia (us-east4)
- Columbus (us-east5)
- Alabama (us-east7)
- Dallas (us-south1)
- Oregon (us-west1)
- Los Angeles (us-west2)
- Salt Lake City (us-west3)
- Las Vegas (us-west4)
- Phoenix (us-west8)

| Item | Price (USD) |
| --- | --- |
|  |  |
| --- | --- |
| SSD storage capacity | $0.000465753 / 1 gibibyte hour |
| Backups (used) | $0.000109589 / 1 gibibyte hour |
| Hyperdisk Balanced Capacity | $0.000157534 / 1 gibibyte hour |
| Hyperdisk Balanced IOPS | $0.000027397 / 1 hour |
| Hyperdisk Balanced Throughput | $0.000109589 / 1 hour |

If you pay in a currency other than USD, the prices listed in your currency on Cloud Platform SKUs apply.

### HA Storage

Iowa (us-central1)

- Johannesburg (africa-south1)
- Taiwan (asia-east1)
- Hong Kong (asia-east2)
- Tokyo (asia-northeast1)
- Osaka (asia-northeast2)
- Seoul (asia-northeast3)
- Mumbai (asia-south1)
- Delhi (asia-south2)
- Singapore (asia-southeast1)
- Jakarta (asia-southeast2)
- Sydney (australia-southeast1)
- Melbourne (australia-southeast2)
- Warsaw (europe-central2)
- Finland (europe-north1)
- Stockholm (europe-north2)
- Madrid (europe-southwest1)
- Belgium (europe-west1)
- Berlin (europe-west10)
- Turin (europe-west12)
- London (europe-west2)
- Frankfurt (europe-west3)
- Netherlands (europe-west4)
- Zurich (europe-west6)
- Milan (europe-west8)
- Paris (europe-west9)
- Doha (me-central1)
- Dammam (me-central2)
- Tel Aviv (me-west1)
- Montreal (northamerica-northeast1)
- Toronto (northamerica-northeast2)
- Mexico (northamerica-south1)
- Sao Paulo (southamerica-east1)
- Santiago (southamerica-west1)
- Iowa (us-central1)
- South Carolina (us-east1)
- Northern Virginia (us-east4)
- Columbus (us-east5)
- Alabama (us-east7)
- Dallas (us-south1)
- Oregon (us-west1)
- Los Angeles (us-west2)
- Salt Lake City (us-west3)
- Las Vegas (us-west4)
- Phoenix (us-west8)

| Item | Price (USD) |
| --- | --- |
|  |  |
| --- | --- |
| SSD storage capacity | $0.000465753 / 1 gibibyte hour |
| Backups (used) | $0.000109589 / 1 gibibyte hour |
| Hyperdisk Balanced HA Capacity | $0.000315068 / 1 gibibyte hour |
| Hyperdisk Balanced HA IOPS | $0.000054795 / 1 hour |
| Hyperdisk Balanced HA Throughput | $0.000219178 / 1 hour |

If you pay in a currency other than USD, the prices listed in your currency on Cloud Platform SKUs apply.

### Network

Iowa (us-central1)

- Johannesburg (africa-south1)
- Taiwan (asia-east1)
- Hong Kong (asia-east2)
- Tokyo (asia-northeast1)
- Osaka (asia-northeast2)
- Seoul (asia-northeast3)
- Mumbai (asia-south1)
- Delhi (asia-south2)
- Singapore (asia-southeast1)
- Jakarta (asia-southeast2)
- Bangkok (asia-southeast3)
- Sydney (australia-southeast1)
- Melbourne (australia-southeast2)
- Warsaw (europe-central2)
- Finland (europe-north1)
- Stockholm (europe-north2)
- Madrid (europe-southwest1)
- Belgium (europe-west1)
- Berlin (europe-west10)
- Turin (europe-west12)
- London (europe-west2)
- Frankfurt (europe-west3)
- Netherlands (europe-west4)
- Zurich (europe-west6)
- Milan (europe-west8)
- Paris (europe-west9)
- Doha (me-central1)
- Dammam (me-central2)
- Tel Aviv (me-west1)
- Montreal (northamerica-northeast1)
- Toronto (northamerica-northeast2)
- Mexico (northamerica-south1)
- Sao Paulo (southamerica-east1)
- Santiago (southamerica-west1)
- Iowa (us-central1)
- South Carolina (us-east1)
- Northern Virginia (us-east4)
- Columbus (us-east5)
- Alabama (us-east7)
- Dallas (us-south1)
- Oregon (us-west1)
- Los Angeles (us-west2)
- Salt Lake City (us-west3)
- Las Vegas (us-west4)
- Phoenix (us-west8)

| Item | Price (USD) |
| --- | --- |
|  |  |
| --- | --- |
| Ingress to Cloud SQL | Free  **Note**: Egress charges may apply on the source. For example, egress from Compute Engine is charged at the external IP addresses rate. |
| Egress from Cloud SQL | Egress from Cloud SQL: See Network Egress Pricing. |
| IPv4 addresses while idle | $0.01 / 1 hour |

If you pay in a currency other than USD, the prices listed in your currency on Cloud Platform SKUs apply.

### Network Egress Pricing

When network traffic leaves a Cloud SQL instance, the charge applied depends on the destination of the traffic, and in some cases, whether a partner is involved.

Internet egress is network traffic leaving a Cloud SQL instance to a client that is not a Google product, such as using a local server to read data from Cloud SQL.

| Destination | Price (USD) |
| --- | --- |
|  |  |
| --- | --- |
| Compute Engine instances | Within the same region: free  Between regions within North America: $0.12/GiB  Between regions outside of North America: $0.12/GiB |
| Google Products (except Compute Engine) | Intra-continental: free  Inter-continental: $0.12/GiB |
| Internet egress using Cloud Interconnect | $0.05/GiB |
| Internet egress (not using Cloud Interconnect) | $0.19/GiB |

If you pay in a currency other than USD, the prices listed in your currency on Cloud Platform SKUs apply.

### Licensing

In addition to instance and resource pricing, SQL Server also has a licensing component. High availability, or regional instances, will only incur the cost for a single license for the active resource.

**Note:** As a managed service, Cloud SQL does not support BYOL (Bring your own license).

You can learn more about instance creation here.

**Note:** Committed Use Discounts do not apply to licenses.

| License | Price per Core Hour (USD) |
| --- | --- |
|  |  |
| --- | --- |
| **Enterprise** | $0.47 |
| **Standard** | $0.13 |
| **Web** | $0.01134 |
| **Express** | $0 |

Microsoft SQL Server licensing requires a core license to be assigned to each virtual CPU on your instance, with a four core minimum for each instance. Instances with fewer than 4 vCPUs will be charged for SQL Server at 4 times the license rate to comply with these requirements. For instances with 4 or more vCPUs, you will be charged for the number of SQL Server licenses that is equal to the number of vCPUs.

Disabling simultaneous multithreading (SMT) reduces the number of virtual CPUs (vCPUs) per core from 2 to 1, which in turn might reduce your SQL Server licensing costs. Disabling SMT doesn't change the compute engine price for SQL Server. You are billed for the number of vCPUs defined in the SQL Server CPU configuration. The following examples show how disabling SMT affects your billing:

| User | SMT: enabled or disabled | Number of vCPUs on the instance | Number of vCPUs the SQL Server licensing fees are calculated for | Number of vCPUs the compute charges are calculated for |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| User1 | Enabled | 8 | 8 | 8 |
| User2 | Disabled | 8 | 4 | 8 |
| User3 | Disabled | 6 | 4 | 6 |

Note that despite disabling SMT, User3's SQL Server license fees are calculated for 4 vCPUs because SQL Server licensing requires a core license to be assigned to each virtual CPU on your instance, with a minimum of four cores for each instance.

SQL Server instance licenses are charged a **1 minute minimum.** After 1 minute, SQL Server instance licenses are charged in **1 second increments**.

### Cloud DNS pricing

With Cloud DNS pricing, the charge is per zone per month (regardless of whether you use your zone), and you also pay for queries against your zones. For more information, see Cloud DNS pricing.

## What's next

- Refer to the Pricing Overview documentation.
- Try the Pricing Calculator.
- Learn more about instance settings.
- Learn more about the high availability configuration.

## Request a custom quote

With Google Cloud's pay-as-you-go pricing, you only pay for the services you use. Connect with our sales team to get a custom quote for your organization.

*send*

DocsSupport

Console

Sign in

- Accelerate your digital transformation
- Whether your business is early in its journey or well on its way to digital transformation, Google Cloud can help solve your toughest challenges.
- Learn more

- Key benefits
- Why Google Cloud

  Top reasons businesses choose us.
- AI and Agents

  Get enterprise-ready AI.
- Multicloud

  Run your apps wherever you need them.
- Global infrastructure

  Build on the same infrastructure as Google.

- Data Cloud

  Make smarter decisions with unified data.
- Modern Infrastructure Cloud

  Next generation of cloud infrastructure.
- Security

  Protect your users, data, and apps.
- Productivity and collaboration

  Connect your teams with AI-powered apps.

- Reports and insights
- Executive insights

  Curated C-suite perspectives.
- Analyst reports

  Read what industry analysts say about us.
- Whitepapers

  Browse and download popular whitepapers.
- Customer stories

  Explore case studies and videos.

- Industry Solutions
- Application Modernization
- Artificial Intelligence
- APIs and Applications
- Data Analytics
- Databases
- Infrastructure Modernization
- Productivity and Collaboration
- Security
- Startups and SMB

- Industry Solutions

  Reduce cost, increase operational agility, and capture new market opportunities.

- Retail

  Analytics and collaboration tools for the retail value chain.

- Consumer Packaged Goods

  Solutions for CPG digital transformation and brand growth.

- Financial Services

  Computing, data management, and analytics tools for financial services.

- Healthcare and Life Sciences

  Advance research at scale and empower healthcare innovation.

- Media and Entertainment

  Solutions for content production and distribution operations.

- Telecommunications

  Hybrid and multi-cloud services to deploy and monetize 5G.

- Games

  AI-driven solutions to build and scale games faster.

- Manufacturing

  Migration and AI tools to optimize the manufacturing value chain.

- Supply Chain and Logistics

  Enable sustainable, efficient, and resilient data-driven operations across supply chain and logistics operations.

- Government

  Data storage, AI, and analytics solutions for government agencies.

- Education

  Teaching tools to provide more engaging learning experiences.

- Not seeing what you're looking for?
- See all industry solutions

- Application Modernization

  Modernize, automate, and scale your application and data portfolio using enterprise AI, intelligent engineering practices, and cloud-native infrastructure.

- Google Cloud Modernize

  Unified program and AI-powered tools for end-to-end cloud migration and modernization.

- Application Modernization with AI

  AI-assisted code refactoring, assessment, and transformation for legacy applications.

- Gemini for business

  Enterprise-ready generative AI and agents to accelerate innovation across your organization.

- AI Hypercomputer

  Integrated supercomputing architecture to train, tune, and serve AI workloads.

- Mainframe Modernization

  Automated tools and AI-driven guidance for moving your mainframe apps to the cloud.

- Database Modernization

  Fully managed database services to migrate, manage, and modernize enterprise data.

- Data Lake Modernization

  Unify and govern multimodal data on an open, high-performance cloud data lake.

- Data Warehouse Modernization

  Migrate and modernize your enterprise data warehouse for serverless analytics and AI.

- APIs

  Unlock legacy applications and build new digital channels using APIs and automation.

- Platform Eng

  Managed services and golden paths to build, manage, and scale internal developer platforms.

- DevOps Best Practices

  Processes and resources for implementing DevOps in your org.

- SRE Principles

  Tools and resources for adopting SRE in your org.

- Artificial Intelligence

  Add intelligence and efficiency to your business with AI and machine learning.

- Gemini for customer experience

  Build and manage agents that live across the entire customer lifecycle.

- Gemini for enterprise

  Unified agentic portfolio for your entire organization.

- AI Commerce Search

  Google-quality search and product recommendations for retailers.

- Google Cloud with Gemini

  AI assistants for application development, coding, and more.

- Physical AI

  Simulate, train, and operate the next generation of robots, autonomous vehicles, industrial devices, and machines.

- APIs and Applications

  Speed up the pace of innovation without coding, using APIs, apps, and automation.

- New Business Channels Using APIs

  Attract and empower an ecosystem of developers and partners.

- Unlocking Legacy Applications Using APIs

  Cloud services for extending and modernizing legacy apps.

- Open Banking APIx

  Simplify and accelerate secure delivery of open banking compliant APIs.

- Data Analytics

  Generate instant insights from data at any scale with a serverless, fully managed analytics platform that significantly simplifies analytics.

- Data Migration

  Migrate and modernize your data warehouse and data lakes with AI-powered migration services.

- Data Lakehouse

  Unify and govern your multimodal data with a high-performance and open data lakehouse.

- Real-time Analytics

  Insights from ingesting, processing, and analyzing event streams.

- Marketing Analytics

  Solutions for collecting, analyzing, and activating customer data.

- Datasets

  Data from Google, public, and commercial providers to enrich your analytics and AI initiatives.

- Business Intelligence

  Solutions for modernizing your BI stack and creating rich data experiences.

- Data Analytics Agents

  Built-in agents for data lifecycle and tools to build your own agents.

- Geospatial Analytics

  A comprehensive platform to solve for geospatial use cases at scale.

- Data Science

  Managed services and integrated workflows to build, manage, and scale data science.

- Databases

  Migrate and manage enterprise data with security, reliability, high availability, and fully managed data services.

- Database Migration

  Guides and tools to simplify your database migration life cycle.

- Database Modernization

  Upgrades to modernize your operational database infrastructure.

- Databases for Games

  Build global, live games with Google Cloud databases.

- Google Cloud Databases

  Database services to migrate, manage, and modernize data.

- Migrate Oracle workloads to Google Cloud

  Rehost, replatform, rewrite your Oracle workloads.

- Open Source Databases

  Fully managed open source databases with enterprise-grade support.

- SQL Server on Google Cloud

  Options for running SQL Server virtual machines on Google Cloud.

- Gemini for Databases

  Supercharge database development and management with AI.

- Infrastructure Modernization

  Migrate core systems rapidly and modernize enterprise workloads with AI-powered infrastructure and automated cloud solutions.

- Google Cloud Modernize

  Unified program and AI-powered tools for end-to-end cloud migration and modernization.

- Gemini for business

  Enterprise-ready generative AI and agents to accelerate innovation across your organization.

- AI Hypercomputer

  Integrated supercomputing architecture to train, tune, and serve AI workloads.

- Rapid Migration and Modernization Program (RaMP)

  End-to-end migration program to simplify and accelerate your path to the cloud.

- Data Center Exits

  Migration solutions for moving VMs, apps, databases, and workloads out of data centers.

- Application Modernization & Migration

  Discovery, assessment, and migration tools for moving and modernizing applications.

- Database Modernization & Migration

  Fully managed database services to migrate, manage, and modernize enterprise data.

- Cross-Cloud Networking

  Simplify hybrid and multicloud networking, and secure your workloads, data, and users.

- High Performance Computing (HPC)

  Compute, storage, and networking options to support any high-performance workload.

- VMware

  Fully managed, native VMware Cloud Foundation software stack on Google Cloud.

- SAP

  Certified infrastructure and AI solutions for running SAP applications and SAP HANA.

- Windows

  Tools, licenses, and partner solutions for running enterprise Windows workloads.

- Productivity and Collaboration

  Change the way teams work with solutions designed for humans and built for impact.

- Google Workspace

  Collaboration and productivity tools for enterprises.

- Google Workspace Essentials

  Secure video meetings and modern collaboration for teams.

- Cloud Identity

  Unified platform for IT admins to manage user devices and apps.

- Chrome Enterprise

  ChromeOS, Chrome Browser, and Chrome devices built for business.

- Security

  Detect, investigate, and respond to online threats to help protect your business.

- Agentic SOC

  Delivering better security outcomes with AI agents.

- Web App and API Protection

  Threat and fraud protection for your web applications and APIs.

- Security and Resilience Framework

  Solutions for each phase of the security and resilience life cycle.

- Risk and compliance as code (RCaC)

  Solution to modernize your governance, risk, and compliance function with automation.

- Software Supply Chain Security

  Solution for improving end-to-end software supply chain security.

- Security Foundation

  Recommended products to help achieve a strong security posture.

- Google Cloud Cybershield™

  Strengthen nationwide cyber defense.

- Startups and SMB

  Accelerate startup and SMB growth with tailored solutions and programs.

- Startup Program

  Get financial, business, and technical support to take your startup to the next level.

- Small and Medium Business

  Explore solutions for web hosting, app development, AI, and analytics.

- Software as a Service

  Build better SaaS products, scale efficiently, and grow your business.

- Featured Products
- AI and Machine Learning
- Business Intelligence
- Compute
- Containers
- Data Analytics
- Databases
- Developer Tools
- Distributed Cloud
- Hybrid and Multicloud
- Industry Specific
- Integration Services
- Management Tools
- Maps and Geospatial
- Media Services
- Migration
- Networking
- Operations
- Productivity and Collaboration
- Security and Identity
- Serverless
- Storage
- Web3

- Featured Products

- Gemini for business

  Secure platform to discover, create, run, and govern AI agents for employees.

- Gemini platform

  Unified platform for ML models, generative AI, and agent building.

- Compute Engine

  Virtual machines running in Google’s data center.

- Cloud Storage

  Object storage that’s secure, durable, and scalable.

- BigQuery

  Autonomous data to AI platform for analytics and data science.

- Cloud Run

  Fully managed environment for running containerized apps.

- Google Kubernetes Engine

  Managed environment for running containerized apps.

- Looker

  Platform for BI, data applications, and embedded analytics.

- Apigee API Management

  Manage the full life cycle of APIs anywhere with visibility and control.

- Cloud SQL

  Relational database services for MySQL, PostgreSQL and SQL Server.

- Cloud CDN

  Content delivery network for delivering web and video.

- Not seeing what you're looking for?
- See all products (100+)

- AI and Machine Learning

- Gemini platform

  Unified platform for ML models, generative AI, and agent building.

- Gemini for business

  Secure platform to discover, create, run, and govern AI agents for employees.

- Gemini for customer experience

  Build and manage agents that live across the entire customer lifecycle.

- Model Garden

  Single place to discover over 200 models from Google and Google partners.

- Customer Experience Agent Studio

  Build conversational AI with both deterministic and gen AI functionality.

- Agent Search

  Build Google-quality search for your enterprise apps and experiences.

- Speech-to-Text

  Speech recognition and transcription across 125 languages.

- Text-to-Speech

  Speech synthesis in 220+ voices and 40+ languages.

- Translation AI

  Language detection, translation, and glossary support.

- Vision AI

  Custom and pre-trained models to detect emotion, text, and more.

- Contact Center as a Service

  Omnichannel contact center solution that is native to the cloud.

- Not seeing what you're looking for?
- See all AI and machine learning products

- Business Intelligence

- Looker

  Platform for BI, data applications, and embedded analytics.

- Data Studio

  Interactive data suite for dashboarding, reporting, and analytics.

- Compute

- Compute Engine

  Virtual machines running in Google’s data center.

- App Engine

  Serverless application platform for apps and back ends.

- Cloud GPUs

  GPUs for ML, scientific computing, and 3D visualization.

- Migrate to Virtual Machines

  Server and virtual machine migration to Compute Engine.

- Spot VMs

  Compute instances for batch jobs and fault-tolerant workloads.

- Batch

  Fully managed service for scheduling batch jobs.

- Sole-Tenant Nodes

  Dedicated hardware for compliance, licensing, and management.

- Bare Metal

  Infrastructure to run specialized workloads on Google Cloud.

- Recommender

  Usage recommendations for Google Cloud products and services.

- VMware Engine

  Fully managed, native VMware Cloud Foundation software stack.

- Cloud Run

  Fully managed environment for running containerized apps.

- Not seeing what you're looking for?
- See all compute products

- Containers

- Google Kubernetes Engine

  Managed environment for running containerized apps.

- Cloud Run

  Fully managed environment for running containerized apps.

- Cloud Build

  Solution for running build steps in a Docker container.

- Artifact Registry

  Package manager for build artifacts and dependencies.

- Cloud Code

  IDE support to write, run, and debug Kubernetes applications.

- Cloud Deploy

  Fully managed continuous delivery to GKE and Cloud Run.

- Migrate to Containers

  Components for migrating VMs into system containers on GKE.

- Deep Learning Containers

  Containers with data science frameworks, libraries, and tools.

- Knative

  Components to create Kubernetes-native cloud-based software.

- Data Analytics

- BigQuery

  Autonomous data to AI platform for analytics and data science.

- Managed Service for Apache Spark

  Zero-ops serverless or managed clusters, accelerated by Lightning Engine.

- Dataflow

  Real-time analytics for stream and batch processing.

- Looker

  Platform for BI, data applications, and embedded analytics.

- Lakehouse

  Open lakehouse platform with enterprise storage and performance capabilities.

- Pub/Sub

  Messaging service for event ingestion and delivery.

- Managed Service for Apache Airflow

  Workflow orchestration service built on Apache Airflow.

- Knowledge Catalog

  Always-on catalog for AI that provides universal context for agents.

- Data Analytics Agents

  Built-in agents for data lifecycle and tools to build your own agents.

- Data Analytics Migration Services

  Free-to-use, cloud-native and AI-powered data migration services.

- Managed Service for Apache Kafka

  Managed Kafka service to operate highly available Apache Kafka clusters.

- Not seeing what you're looking for?
- See all data analytics products

- Databases

- AlloyDB for PostgreSQL

  Fully managed, PostgreSQL-compatible database for enterprise workloads.

- Cloud SQL

  Fully managed database for MySQL, PostgreSQL, and SQL Server.

- Firestore

  Highly scalable and serverless NoSQL document database, with MongoDB compatibility.

- Spanner

  Cloud-native relational database with unlimited scale and 99.999% availability.

- Bigtable

  Cloud-native wide-column database for large-scale, low-latency workloads.

- Datastream

  Serverless change data capture and replication service.

- Database Migration Service

  Serverless, minimal downtime migrations to Cloud SQL.

- Bare Metal Solution

  Fully managed infrastructure for your Oracle workloads.

- Memorystore

  Fully managed Redis and Memcached for sub-millisecond data access.

- Developer Tools

- Artifact Registry

  Universal package manager for build artifacts and dependencies.

- Cloud Code

  IDE support to write, run, and debug Kubernetes applications.

- Cloud Build

  Continuous integration and continuous delivery platform.

- Cloud Deploy

  Fully managed continuous delivery to GKE and Cloud Run.

- Cloud Deployment Manager

  Service for creating and managing Google Cloud resources.

- Cloud SDK

  Command-line tools and libraries for Google Cloud.

- Cloud Scheduler

  Cron job scheduler for task automation and management.

- Cloud Source Repositories

  Private Git repository to store, manage, and track code.

- Infrastructure Manager

  Automate infrastructure management with Terraform.

- Cloud Workstations

  Managed and secure development environments in the cloud.

- Gemini Code Assist

  AI-powered assistant available across Google Cloud and your IDE.

- Not seeing what you're looking for?
- See all developer tools

- Distributed Cloud

- Google Distributed Cloud Connected

  Distributed cloud services for edge workloads.

- Google Distributed Cloud Air-gapped

  Distributed cloud for air-gapped workloads.

- Hybrid and Multicloud

- Google Kubernetes Engine

  Managed environment for running containerized apps.

- Apigee API Management

  API management, development, and security platform.

- Migrate to Containers

  Tool to move workloads and existing applications to GKE.

- Cloud Build

  Service for executing builds on Google Cloud infrastructure.

- Observability

  Monitoring, logging, and application performance suite.

- Cloud Service Mesh

  Fully managed service mesh based on Envoy and Istio.

- Google Distributed Cloud

  Fully managed solutions for the edge and data centers.

- Industry Specific

- Anti Money Laundering AI

  Detect suspicious, potential money laundering activity with AI.

- Cloud Healthcare API

  Solution for bridging existing care systems and apps on Google Cloud.

- Device Connect for Fitbit

  Gain a 360-degree patient view with connected Fitbit data on Google Cloud.

- Telecom Network Automation

  Ready to use cloud-native automation for telecom networks.

- Telecom Data Fabric

  Telecom data management and analytics with an automated approach.

- Telecom Subscriber Insights

  Ingests data to improve subscriber acquisition and retention.

- Spectrum Access System (SAS)

  Controls fundamental access to the Citizens Broadband Radio Service (CBRS).

- Integration Services

- Application Integration

  Connect to 3rd party apps and enable data consistency without code.

- Workflows

  Workflow orchestration for serverless products and API services.

- Apigee API Management

  Manage the full life cycle of APIs anywhere with visibility and control.

- Cloud Tasks

  Task management service for asynchronous task execution.

- Cloud Scheduler

  Cron job scheduler for task automation and management.

- Managed Service for Apache Spark

  Zero-ops serverless or managed clusters, accelerated by Lightning Engine.

- Cloud Data Fusion

  Data integration for building and managing data pipelines.

- Managed Service for Apache Airflow

  Workflow orchestration service built on Apache Airflow.

- Pub/Sub

  Messaging service for event ingestion and delivery.

- Eventarc

  Build an event-driven architecture that can connect any service.

- Management Tools

- Cloud Shell

  Interactive shell environment with a built-in command line.

- Cloud console

  Web-based interface for managing and monitoring cloud apps.

- Cloud Endpoints

  Deployment and development management for APIs on Google Cloud.

- Cloud IAM

  Permissions management system for Google Cloud resources.

- Cloud APIs

  Programmatic interfaces for Google Cloud services.

- Service Catalog

  Service catalog for admins managing internal enterprise solutions.

- Cost Management

  Tools for monitoring, controlling, and optimizing your costs.

- Observability

  Monitoring, logging, and application performance suite.

- Carbon Footprint

  Dashboard to view and export Google Cloud carbon emissions reports.

- Config Connector

  Kubernetes add-on for managing Google Cloud resources.

- Active Assist

  Tools for easily managing performance, security, and cost.

- Not seeing what you're looking for?
- See all management tools

- Maps and Geospatial

- Earth Engine

  Geospatial platform for Earth observation data and analysis.

- Google Maps Platform

  Create immersive location experiences and improve business operations.

- Media Services

- Cloud CDN

  Content delivery network for serving web and video content.

- Live Stream API

  Service to convert live video and package for streaming.

- OpenCue

  Open source render manager for visual effects and animation.

- Transcoder API

  Convert video files and package them for optimized delivery.

- Video Stitcher API

  Service for dynamic or server side ad insertion.

- Migration

- Migration Center

  Unified platform for migrating and modernizing with Google Cloud.

- Application Migration

  App migration to the cloud for low-cost refresh cycles.

- Migrate to Virtual Machines

  Components for migrating VMs and physical servers to Compute Engine.

- Cloud Foundation Toolkit

  Reference templates for Deployment Manager and Terraform.

- Database Migration Service

  Serverless, minimal downtime migrations to Cloud SQL.

- Migrate to Containers

  Components for migrating VMs into system containers on GKE.

- Data Analytics Migration Services

  Streamlined data warehouse and data lake migration tooling and incentives.

- Rapid Migration and Modernization Program

  End-to-end migration program to simplify your path to the cloud.

- Transfer Appliance

  Storage server for moving large volumes of data to Google Cloud.

- Storage Transfer Service

  Data transfers from online and on-premises sources to Cloud Storage.

- VMware Engine

  Migrate and run your VMware workloads natively on Google Cloud.

- Networking

- Cloud Armor

  Security policies and defense against web and DDoS attacks.

- Cloud CDN and Media CDN

  Content delivery network for serving web and video content.

- Cloud DNS

  Domain name system for reliable and low-latency name lookups.

- Cloud Load Balancing

  Service for distributing traffic across applications and regions.

- Cloud NAT

  NAT service for giving private instances internet access.

- Cloud Connectivity

  Connectivity options for VPN, peering, and enterprise needs.

- Network Connectivity Center

  Connectivity management to help simplify and scale networks.

- Network Intelligence Center

  Network monitoring, verification, and optimization platform.

- Network Service Tiers

  Cloud network options based on performance, availability, and cost.

- Virtual Private Cloud

  Single VPC for an entire organization, isolated within projects.

- Private Service Connect

  Secure connection between your VPC and services.

- Not seeing what you're looking for?
- See all networking products

- Operations

- Cloud Logging

  Google Cloud audit, platform, and application logs management.

- Cloud Monitoring

  Infrastructure and application health with rich metrics.

- Error Reporting

  Application error identification and analysis.

- Managed Service for Prometheus

  Fully-managed Prometheus on Google Cloud.

- Cloud Trace

  Tracing system collecting latency data from applications.

- Cloud Profiler

  CPU and heap profiler for analyzing application performance.

- Cloud Quotas

  Manage quotas for all Google Cloud services.

- Productivity and Collaboration

- AppSheet

  No-code development platform to build and extend applications.

- AppSheet Automation

  Build automations and applications on a unified platform.

- Gemini for business

  Secure platform to discover, create, run, and govern AI agents for employees.

- Google Workspace

  Collaboration and productivity tools for individuals and organizations.

- Google Workspace Essentials

  Secure video meetings and modern collaboration for teams.

- Cloud Identity

  Unified platform for IT admins to manage user devices and apps.

- Chrome Enterprise

  ChromeOS, Chrome browser, and Chrome devices built for business.

- Security and Identity

- Cloud IAM

  Permissions management system for Google Cloud resources.

- Sensitive Data Protection

  Discover, classify, and protect your valuable data assets.

- Mandiant Managed Defense

  Find and eliminate threats with confidence 24x7.

- Google Threat Intelligence

  Know who’s targeting you.

- Security Command Center

  Platform for defending against threats to your Google Cloud assets.

- Cloud Key Management

  Manage encryption keys on Google Cloud.

- Mandiant Incident Response

  Minimize the impact of a breach.

- Chrome Enterprise Premium

  Get secure enterprise browsing with extensive endpoint visibility.

- Assured Workloads

  Compliance and security controls for sensitive workloads.

- Google Security Operations

  Detect, investigate, and respond to cyber threats.

- Mandiant Consulting

  Get expert guidance before, during, and after an incident.

- Not seeing what you're looking for?
- See all security and identity products

- Serverless

- Cloud Run

  Fully managed environment for running containerized apps.

- Cloud Functions

  Platform for creating functions that respond to cloud events.

- App Engine

  Serverless application platform for apps and back ends.

- Workflows

  Workflow orchestration for serverless products and API services.

- API Gateway

  Develop, deploy, secure, and manage APIs with a fully managed gateway.

- Storage

- Cloud Storage

  Object storage that’s secure, durable, and scalable.

- Block Storage

  High-performance storage for AI, analytics, databases, and enterprise applications.

- Filestore

  File storage that is highly scalable and secure.

- Persistent Disk

  Block storage for virtual machine instances running on Google Cloud.

- Cloud Storage for Firebase

  Object storage for storing and serving user-generated content.

- Local SSD

  Block storage that is locally attached for high-performance needs.

- Storage Transfer Service

  Data transfers from online and on-premises sources to Cloud Storage.

- Google Cloud Managed Lustre

  High performance managed parallel file service.

- Google Cloud NetApp Volumes

  File storage service for NFS, SMB, and multi-protocol environments.

- Backup and DR Service

  Service for centralized, application-consistent data protection.

- Web3

- Blockchain Node Engine

  Fully managed node hosting for developing on the blockchain.

- Blockchain RPC

  Enterprise-grade RPC for building on the blockchain.

- Save money with our transparent approach to pricing
- Google Cloud's pay-as-you-go pricing offers automatic savings based on monthly usage and discounted rates for prepaid resources. Contact us today to get a quote.
- Request a quote

- Pricing overview and tools
- Google Cloud pricing

  Pay only for what you use with no lock-in.
- Pricing calculator

  Calculate your cloud savings.
- Google Cloud free tier

  Explore products with free monthly usage.

- Cost optimization framework

  Get best practices to optimize workload costs.
- Cost management tools

  Tools to monitor and control your costs.

- Product-specific Pricing
- Compute Engine
- Cloud SQL
- Google Kubernetes Engine
- Cloud Storage
- BigQuery
- See full price list with 100+ products

- Learn & build
- Google Cloud Free Program

  $300 in free credits and 20+ free products.
- Solution Generator

  Get AI generated solution recommendations.
- Quickstarts

  Get tutorials and walkthroughs.
- Blog

  Read our latest product news and stories.

- Learning Hub

  Grow your career with role-based training.
- Google Cloud certification

  Prepare and register for certifications.
- Cloud computing basics

  Learn more about cloud computing basics.
- Cloud Architecture Center

  Get reference architectures and best practices.

- Connect
- Innovators

  Join Google Cloud's developer program.
- Developer Center

  Stay in the know and stay connected.
- Events and webinars

  Browse upcoming and on demand events.
- Google Cloud Community

  Ask questions, find answers, and connect.

- Consulting and Partners
- Google Cloud Consulting

  Work with our experts on cloud projects.
- Google Cloud Marketplace

  Deploy ready-to-go solutions in a few clicks.
- Find a partner

  Explore the benefits of working with a partner.
- Google Cloud partners

  Learn about the ecosystem and resources.

- Overview
- Solutions
- Products
- Pricing
- Resources
- Docs
- Support
- Console

- Accelerate your digital transformation
- Learn more
- Key benefits
- Why Google Cloud
- AI and Agents
- Multicloud
- Global infrastructure
- Data Cloud
- Modern Infrastructure Cloud
- Security
- Productivity and collaboration
- Reports and insights
- Executive insights
- Analyst reports
- Whitepapers
- Customer stories

- Industry Solutions
- Retail
- Consumer Packaged Goods
- Financial Services
- Healthcare and Life Sciences
- Media and Entertainment
- Telecommunications
- Games
- Manufacturing
- Supply Chain and Logistics
- Government
- Education
- See all industry solutions
- See all solutions
- Application Modernization
- Google Cloud Modernize
- Application Modernization with AI
- Gemini for business
- AI Hypercomputer
- Mainframe Modernization
- Database Modernization
- Data Lake Modernization
- Data Warehouse Modernization
- APIs
- Platform Eng
- DevOps Best Practices
- SRE Principles
- Artificial Intelligence
- Gemini for customer experience
- Gemini for enterprise
- AI Commerce Search
- Google Cloud with Gemini
- Physical AI
- APIs and Applications
- New Business Channels Using APIs
- Unlocking Legacy Applications Using APIs
- Open Banking APIx
- Data Analytics
- Data Migration
- Data Lakehouse
- Real-time Analytics
- Marketing Analytics
- Datasets
- Business Intelligence
- Data Analytics Agents
- Geospatial Analytics
- Data Science
- Databases
- Database Migration
- Database Modernization
- Databases for Games
- Google Cloud Databases
- Migrate Oracle workloads to Google Cloud
- Open Source Databases
- SQL Server on Google Cloud
- Gemini for Databases
- Infrastructure Modernization
- Google Cloud Modernize
- Gemini for business
- AI Hypercomputer
- Rapid Migration and Modernization Program (RaMP)
- Data Center Exits
- Application Modernization & Migration
- Database Modernization & Migration
- Cross-Cloud Networking
- High Performance Computing (HPC)
- VMware
- SAP
- Windows
- Productivity and Collaboration
- Google Workspace
- Google Workspace Essentials
- Cloud Identity
- Chrome Enterprise
- Security
- Agentic SOC
- Web App and API Protection
- Security and Resilience Framework
- Risk and compliance as code (RCaC)
- Software Supply Chain Security
- Security Foundation
- Google Cloud Cybershield™
- Startups and SMB
- Startup Program
- Small and Medium Business
- Software as a Service

- Featured Products
- Gemini for business
- Gemini platform
- Compute Engine
- Cloud Storage
- BigQuery
- Cloud Run
- Google Kubernetes Engine
- Looker
- Apigee API Management
- Cloud SQL
- Cloud CDN
- See all products (100+)
- AI and Machine Learning
- Gemini platform
- Gemini for business
- Gemini for customer experience
- Model Garden
- Customer Experience Agent Studio
- Agent Search
- Speech-to-Text
- Text-to-Speech
- Translation AI
- Vision AI
- Contact Center as a Service
- See all AI and machine learning products
- Business Intelligence
- Looker
- Data Studio
- Compute
- Compute Engine
- App Engine
- Cloud GPUs
- Migrate to Virtual Machines
- Spot VMs
- Batch
- Sole-Tenant Nodes
- Bare Metal
- Recommender
- VMware Engine
- Cloud Run
- See all compute products
- Containers
- Google Kubernetes Engine
- Cloud Run
- Cloud Build
- Artifact Registry
- Cloud Code
- Cloud Deploy
- Migrate to Containers
- Deep Learning Containers
- Knative
- Data Analytics
- BigQuery
- Managed Service for Apache Spark
- Dataflow
- Looker
- Lakehouse
- Pub/Sub
- Managed Service for Apache Airflow
- Knowledge Catalog
- Data Analytics Agents
- Data Analytics Migration Services
- Managed Service for Apache Kafka
- See all data analytics products
- Databases
- AlloyDB for PostgreSQL
- Cloud SQL
- Firestore
- Spanner
- Bigtable
- Datastream
- Database Migration Service
- Bare Metal Solution
- Memorystore
- Developer Tools
- Artifact Registry
- Cloud Code
- Cloud Build
- Cloud Deploy
- Cloud Deployment Manager
- Cloud SDK
- Cloud Scheduler
- Cloud Source Repositories
- Infrastructure Manager
- Cloud Workstations
- Gemini Code Assist
- See all developer tools
- Distributed Cloud
- Google Distributed Cloud Connected
- Google Distributed Cloud Air-gapped
- Hybrid and Multicloud
- Google Kubernetes Engine
- Apigee API Management
- Migrate to Containers
- Cloud Build
- Observability
- Cloud Service Mesh
- Google Distributed Cloud
- Industry Specific
- Anti Money Laundering AI
- Cloud Healthcare API
- Device Connect for Fitbit
- Telecom Network Automation
- Telecom Data Fabric
- Telecom Subscriber Insights
- Spectrum Access System (SAS)
- Integration Services
- Application Integration
- Workflows
- Apigee API Management
- Cloud Tasks
- Cloud Scheduler
- Managed Service for Apache Spark
- Cloud Data Fusion
- Managed Service for Apache Airflow
- Pub/Sub
- Eventarc
- Management Tools
- Cloud Shell
- Cloud console
- Cloud Endpoints
- Cloud IAM
- Cloud APIs
- Service Catalog
- Cost Management
- Observability
- Carbon Footprint
- Config Connector
- Active Assist
- See all management tools
- Maps and Geospatial
- Earth Engine
- Google Maps Platform
- Media Services
- Cloud CDN
- Live Stream API
- OpenCue
- Transcoder API
- Video Stitcher API
- Migration
- Migration Center
- Application Migration
- Migrate to Virtual Machines
- Cloud Foundation Toolkit
- Database Migration Service
- Migrate to Containers
- Data Analytics Migration Services
- Rapid Migration and Modernization Program
- Transfer Appliance
- Storage Transfer Service
- VMware Engine
- Networking
- Cloud Armor
- Cloud CDN and Media CDN
- Cloud DNS
- Cloud Load Balancing
- Cloud NAT
- Cloud Connectivity
- Network Connectivity Center
- Network Intelligence Center
- Network Service Tiers
- Virtual Private Cloud
- Private Service Connect
- See all networking products
- Operations
- Cloud Logging
- Cloud Monitoring
- Error Reporting
- Managed Service for Prometheus
- Cloud Trace
- Cloud Profiler
- Cloud Quotas
- Productivity and Collaboration
- AppSheet
- AppSheet Automation
- Gemini for business
- Google Workspace
- Google Workspace Essentials
- Cloud Identity
- Chrome Enterprise
- Security and Identity
- Cloud IAM
- Sensitive Data Protection
- Mandiant Managed Defense
- Google Threat Intelligence
- Security Command Center
- Cloud Key Management
- Mandiant Incident Response
- Chrome Enterprise Premium
- Assured Workloads
- Google Security Operations
- Mandiant Consulting
- See all security and identity products
- Serverless
- Cloud Run
- Cloud Functions
- App Engine
- Workflows
- API Gateway
- Storage
- Cloud Storage
- Block Storage
- Filestore
- Persistent Disk
- Cloud Storage for Firebase
- Local SSD
- Storage Transfer Service
- Google Cloud Managed Lustre
- Google Cloud NetApp Volumes
- Backup and DR Service
- Web3
- Blockchain Node Engine
- Blockchain RPC

- Save money with our transparent approach to pricing
- Request a quote
- Pricing overview and tools
- Google Cloud pricing
- Pricing calculator
- Google Cloud free tier
- Cost optimization framework
- Cost management tools
- Product-specific Pricing
- Compute Engine
- Cloud SQL
- Google Kubernetes Engine
- Cloud Storage
- BigQuery
- See full price list with 100+ products

- Learn & build
- Google Cloud Free Program
- Solution Generator
- Quickstarts
- Blog
- Learning Hub
- Google Cloud certification
- Cloud computing basics
- Cloud Architecture Center
- Connect
- Innovators
- Developer Center
- Events and webinars
- Google Cloud Community
- Consulting and Partners
- Google Cloud Consulting
- Google Cloud Marketplace
- Find a partner
- Google Cloud partners
