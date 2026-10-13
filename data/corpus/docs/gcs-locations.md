---
doc_id: gcs-locations
title: Bucket locations
url: https://docs.cloud.google.com/storage/docs/locations
category: storage
fetched_at: '2026-10-13T15:13:49+00:00'
license: CC BY 4.0 (Google Cloud documentation)
---

This page explains the concept of *bucket location* and the different
locations where you can create buckets. A bucket's location defines the
physical place where object data in the bucket resides.

To learn how to set the location for your bucket, see Create buckets.

## Key concepts

- You set a geographic location for storing your
  object data when you create a bucket.

  - You can relocate a bucket after it's created or
    move your data to a bucket in a different location. Note that
    bucket relocation is available only if you've configured
    Storage Intelligence.
- You can select from the following location types:

  - A *region* is a specific geographic place, such as Iowa (`US-CENTRAL1`).
  - A *zone* is a specific area within a region, such as `US-CENTRAL1-A`. This
    location type is only available with Rapid Bucket.
  - A *dual-region* is a specific pair of regions, such as Tokyo and
    Osaka (`ASIA1`).

    - Dual-region pairings can be *predefined* or *configurable*.
  - A *multi-region* is a large geographic area that contains two or more
    geographic regions, such as the United States (`US`).
- The location type determines how your data is replicated and priced.
- Cloud Storage stores object data in the selected location in
  accordance with the Service Specific Terms.
- The location information for a bucket is part of the bucket's metadata,
  which you can view if you have permission to do so.

## Location considerations

When you choose the location for a Cloud Storage bucket, consider the
differences in availability, and price, as shown in the following
table.

|  | Zone | Region | Dual-region | Multi-region |
| --- | --- | --- | --- | --- |
| Availability | - Data redundancy within one availability zone - Zonal outages might affect availability | - Data redundancy across availability zones (synchronous) - RTO(recovery time objective)=0: automated failover and failback on   zonal failure (no need to change storage paths) | - Higher availability than regions for a given storage class - Data redundancy across regions (asynchronous) - Turbo replication option for replication within 15 minutes - RTO(recovery time objective)=0: automated failover and failback on   regional failure (no need to change storage paths) | - Higher availability than regions for a given storage class - Data redundancy across regions (asynchronous) - RTO(recovery time objective)=0: automated failover and failback on   regional failure (no need to change storage paths) |
| Pricing | - Offers the highest performance in Cloud Storage for demanding   workloads at the highest storage price, out of all location types - Zonal bucket-specific data transfer charges apply. For more   information, see Cloud Storage pricing. | - Lowest storage price - No replication charges - No outbound data transfer charges when reading data inside the same   region | - Highest storage price - Replication charges apply on write - No outbound data transfer charges when reading data within either   region | - Higher storage price than regions, but lower than dual-regions - Replication charges apply on write - Outbound data transfer charges always apply when reading data |

### Location recommendations

| Requirements | Recommended bucket location | Workload examples |
| --- | --- | --- |
| - Ultra-low latency - Ultra-high bandwidth and I/O - High performance | Zone1 | - Artificial Intelligence (AI) and Machine Learning (ML) - High-performance computing - Data-intensive analytics |
| - Optimized latency and bandwidth - Lowest data storage cost - Cross-zone redundancy | Region2 | - Analytics - Backup and archive |
| - Optimized latency and bandwidth - Cross-region redundancy, with precise control of the locations where copies of data are stored | Dual-region3 | - Analytics - Backup and archive - Disaster recovery |
| - Cross-geography data access - Cross-region redundancy | Multi-region | - Content serving |

1. Zonal locations for buckets are only available through Rapid Bucket.
2. For more information about region-specific considerations, see
   Geography and regions.
3. If you need a short and predictable
   recovery point objective (RPO),
   enable the premium
   turbo replication
   feature.

- To maximize performance and lower the latency between requests and responses,
  colocate your stored data in the same zone as the compute resources accessing
  your data. To store data in zones, use
  Rapid Bucket.
- To withstand the risk of losing data within an individual zone, use regions or
  dual-regions.
- To avoid data replication charges, store short-lived datasets in regions.
- For moderate performance and ad hoc analytics workloads, multi-region storage
  can be a cost-effective choice.

  Note that the performance of workloads that use data in a multi-region bucket
  might vary over time because storage and compute aren't colocated. When a
  multi-region workload has strict performance requirements, consider enabling
  Rapid Cache.
- See the data storage pricing table for storage costs in each location.

### Compute Engine VM notes

Storing data in the same zone or region as your
Compute Engine VM instances can provide better performance. This
advantage applies to zones, regions, and dual-regions.

## Available locations

The following sections list the Cloud Storage locations available for
storing your data.

### Zones

A zone is an isolated deployment area within a region.

The following zones are available for zonal buckets:

| Region | Zone Name | Zone Description |  |
| --- | --- | --- | --- |
| `ASIA-SOUTH1` |  |  |  |
|  | `ASIA-SOUTH1-B` | Mumbai, India, APAC |  |
| `ASIA-SOUTHEAST1` |  |  |  |
|  | `ASIA-SOUTHEAST1-A` | Jurong West, Singapore, APAC |  |
|  | `ASIA-SOUTHEAST1-B` | Jurong West, Singapore, APAC |  |
|  | `ASIA-SOUTHEAST1-C` | Jurong West, Singapore, APAC |  |
| `EUROPE-WEST1` |  |  |  |
|  | `EUROPE-WEST1-B` | St. Ghislain, Belgium, Europe |  |
|  | `EUROPE-WEST1-C` | St. Ghislain, Belgium, Europe |  |
|  | `EUROPE-WEST1-D` | St. Ghislain, Belgium, Europe |  |
| `EUROPE-WEST4` |  |  |  |
|  | `EUROPE-WEST4-A` | Eemshaven, Netherlands, Europe |  |
| `US-CENTRAL1` |  |  |  |
|  | `US-CENTRAL1-A` | Council Bluffs, Iowa, North America |  |
|  | `US-CENTRAL1-AI1A` | Lincoln, Nebraska, North America (AI zone) |  |
|  | `US-CENTRAL1-B` | Council Bluffs, Iowa, North America |  |
|  | `US-CENTRAL1-C` | Council Bluffs, Iowa, North America |  |
|  | `US-CENTRAL1-F` | Council Bluffs, Iowa, North America |  |
| `US-EAST1` |  |  |  |
|  | `US-EAST1-B` | Moncks Corner, South Carolina, North America |  |
|  | `US-EAST1-D` | Moncks Corner, South Carolina, North America |  |
| `US-EAST4` |  |  |  |
|  | `US-EAST4-A` | Ashburn, Virginia, North America |  |
|  | `US-EAST4-B` | Ashburn, Virginia, North America |  |
|  | `US-EAST4-C` | Ashburn, Virginia, North America |  |
| `US-EAST5` |  |  |  |
|  | `US-EAST5-A` | Columbus, Ohio, North America |  |
|  | `US-EAST5-B` | Columbus, Ohio, North America |  |
|  | `US-EAST5-C` | Columbus, Ohio, North America |  |
| `US-SOUTH1` |  |  |  |
|  | `US-SOUTH1-A` | Dallas, Texas, North America |  |
|  | `US-SOUTH1-B` | Dallas, Texas, North America |  |
|  | `US-SOUTH1-C` | Dallas, Texas, North America |  |
| `US-WEST1` |  |  |  |
|  | `US-WEST1-A` | The Dalles, Oregon, North America |  |
|  | `US-WEST1-B` | The Dalles, Oregon, North America |  |
|  | `US-WEST1-C` | The Dalles, Oregon, North America |  |
| `US-WEST4` |  |  |  |
|  | `US-WEST4-A` | Las Vegas, Nevada, North America |  |
|  | `US-WEST4-B` | Las Vegas, Nevada, North America |  |
|  | `US-WEST4-C` | Las Vegas, Nevada, North America |  |

### Regions

A region is a specific geographic place, such as Seoul (`ASIA-NORTHEAST3`). Data
stored in regions are redundant across multiple zones within the region.

The following regions are available:

| Geographic Area | Region Name | Region Description |  |
| --- | --- | --- | --- |
| **North America** |  |  |  |
|  | `NORTHAMERICA-NORTHEAST1` 1 | Montréal | Low CO2 |
|  | `NORTHAMERICA-NORTHEAST2` | Toronto | Low CO2 |
|  | `NORTHAMERICA-SOUTH1` 1 | Querétaro |  |
|  | `US-CENTRAL1` | Iowa | Low CO2 |
|  | `US-EAST1` | South Carolina |  |
|  | `US-EAST4` | Northern Virginia |  |
|  | `US-EAST5` | Columbus |  |
|  | `US-SOUTH1` | Dallas | Low CO2 |
|  | `US-WEST1` | Oregon | Low CO2 |
|  | `US-WEST2` | Los Angeles |  |
|  | `US-WEST3` | Salt Lake City |  |
|  | `US-WEST4` | Las Vegas |  |
| **South America** |  |  |  |
|  | `SOUTHAMERICA-EAST1` | São Paulo | Low CO2 |
|  | `SOUTHAMERICA-WEST1` | Santiago | Low CO2 |
| **Europe** |  |  |  |
|  | `EUROPE-CENTRAL2` | Warsaw | Low CO2 |
|  | `EUROPE-NORTH1` | Finland | Low CO2 |
|  | `EUROPE-NORTH2` 1 | Stockholm | Low CO2 |
|  | `EUROPE-SOUTHWEST1` | Madrid | Low CO2 |
|  | `EUROPE-WEST1` | Belgium | Low CO2 |
|  | `EUROPE-WEST2` | London | Low CO2 |
|  | `EUROPE-WEST3` | Frankfurt |  |
|  | `EUROPE-WEST4` | Netherlands | Low CO2 |
|  | `EUROPE-WEST6` | Zürich | Low CO2 |
|  | `EUROPE-WEST8` | Milan | Low CO2 |
|  | `EUROPE-WEST9` | Paris | Low CO2 |
|  | `EUROPE-WEST10` | Berlin |  |
|  | `EUROPE-WEST12` | Turin | Low CO2 |
| **Asia** |  |  |  |
|  | `ASIA-EAST1` | Taiwan |  |
|  | `ASIA-EAST2` | Hong Kong |  |
|  | `ASIA-NORTHEAST1` | Tokyo |  |
|  | `ASIA-NORTHEAST2` 1 | Osaka |  |
|  | `ASIA-NORTHEAST3` | Seoul |  |
|  | `ASIA-SOUTH1` | Mumbai |  |
|  | `ASIA-SOUTH2` | Delhi |  |
|  | `ASIA-SOUTHEAST1` | Singapore |  |
|  | `ASIA-SOUTHEAST2` | Jakarta |  |
|  | `ASIA-SOUTHEAST3` | Bangkok |  |
| **Middle East** |  |  |  |
|  | `ME-CENTRAL1` | Doha |  |
|  | `ME-CENTRAL2` | Dammam, Saudi Arabia |  |
|  | `ME-WEST1` | Tel Aviv |  |
| **Australia** |  |  |  |
|  | `AUSTRALIA-SOUTHEAST1` | Sydney |  |
|  | `AUSTRALIA-SOUTHEAST2` | Melbourne |  |
| **Africa** |  |  |  |
|  | `AFRICA-SOUTH1` | Johannesburg |  |

1Montréal, Osaka, Querétaro, and Stockholm each have three zones
housed in one or two physical data centers. In the rare event of a disaster,
data stored in these regions can be lost. To avoid this, you might want to
consider using a dual-region or backing up business-critical
data to a second region using Storage Transfer Service for increased data
protection.

### Dual-regions

Objects stored in dual-region buckets are replicated so that they are stored in
each region that make up the dual-region. The time it takes an object to be
replicated between the two regions is determined by the bucket's
replication setting.

The following types of dual-regions are supported in Cloud Storage:

- A *predefined dual-region* is identified by a unique location code and
  represents two specific regions. For example, `NAM4` is the location code for
  the predefined dual-region consisting of `US-CENTRAL1` and `US-EAST1`.
- A *configurable dual-region* is identified by the location code of the
  geographical area in which the dual-region resides and a placement
  configuration in which you specify a pair of regions. For example, you could
  create a configurable dual-region that has a location code of `EU` and
  a placement configuration consisting of `EU-CENTRAL2` and `EU-WEST1`.

If the regions you want to pair are not available as a dual-region, consider
creating a separate bucket in each region and using Storage Transfer Service
Event-driven transfers to keep the buckets in sync.

#### Configurable dual-regions

When creating a bucket in a configurable dual-region, the pair of regions
that you use to make the dual-region must use the same location code. This code
is set for the `LOCATION` of the bucket and is also the location you specify
when using customer-managed encryption keys or the
resource locations constraint with such dual-region buckets.

**Note:** Unlike buckets in other locations, which bill storage usage against
the SKUs associated with their location code, buckets in configurable
dual-regions bill storage usage against SKUs in both of their underlying
regions.

The following regions are available when creating a configurable dual-region
bucket:

| Location code | Region Name | Region Description |
| --- | --- | --- |
| `ASIA` |  |  |
|  | `ASIA-EAST1` | Taiwan |
|  | `ASIA-SOUTHEAST1` | Singapore |
| `AU` |  |  |
|  | `AUSTRALIA-SOUTHEAST1` | Sydney |
|  | `AUSTRALIA-SOUTHEAST2` | Melbourne |
| `CA` |  |  |
|  | `NORTHAMERICA-NORTHEAST1` | Montréal |
|  | `NORTHAMERICA-NORTHEAST2` | Toronto |
| `DE` |  |  |
|  | `EUROPE-WEST3` | Frankfurt |
|  | `EUROPE-WEST10` | Berlin |
| `EU` |  |  |
|  | `EUROPE-CENTRAL2` | Warsaw |
|  | `EUROPE-NORTH1`1 | Finland |
|  | `EUROPE-SOUTHWEST1` | Madrid |
|  | `EUROPE-WEST1` | Belgium |
|  | `EUROPE-WEST3`5 | Frankfurt |
|  | `EUROPE-WEST4`1 | Netherlands |
|  | `EUROPE-WEST8`4 | Milan |
|  | `EUROPE-WEST9` | Paris |
|  | `EUROPE-WEST10`5 | Berlin |
|  | `EUROPE-WEST12`4 | Turin |
| `IN` |  |  |
|  | `ASIA-SOUTH1` | Mumbai |
|  | `ASIA-SOUTH2` | Delhi |
| `IT` |  |  |
|  | `EUROPE-WEST8` | Milan |
|  | `EUROPE-WEST12` | Turin |
| `US` |  |  |
|  | `US-CENTRAL1`2 | Iowa |
|  | `US-EAST1` 2 | South Carolina |
|  | `US-EAST4` | Northern Virginia |
|  | `US-EAST5`3 | Columbus |
|  | `US-SOUTH1` | Dallas |
|  | `US-WEST1` | Oregon |
|  | `US-WEST2` | Los Angeles |
|  | `US-WEST3` | Salt Lake City |
|  | `US-WEST4` | Las Vegas |

1The `EUROPE-NORTH1` and `EUROPE-WEST4` dual-region pairing is only
available as a predefined dual-region.

2The `US-CENTRAL1` and `US-EAST1` dual-region pairing is only
available as a predefined dual-region.

3`US-EAST5` must be paired with either `US-CENTRAL1` or `US-EAST1`.

4 When pairing `EUROPE-WEST8` and `EUROPE-WEST12`,
use the `IT` multi-region code.

5 When pairing `EUROPE-WEST3` and `EUROPE-WEST10`, use the `DE`
multi-region code.

Attempting to create a bucket using an invalid pairing, such as regions with
different location codes, returns an error.

#### Predefined dual-regions

When creating a bucket in a predefined dual-region, you use a
location code that uniquely identifies the pair of regions, in the same way you
create buckets in regions and multi-regions. This location code is what you
specify when using customer-managed encryption keys or the
resource locations constraint with such dual-region buckets.

**Note:** Some tools present all dual-regions as if they were configurable
dual-regions during bucket creation. For example, when creating a bucket in
a dual-region using the Google Cloud console, you always select the individual
regions that are part of the dual-region. If a predefined dual-region exists for
that pair, that predefined dual-region is used. Otherwise, a configurable
dual-region is created. Once a bucket is created, the Google Cloud console
displays the correct location for that bucket, making it clear if a predefined
dual-region was used.

The following options are available when creating a bucket in a predefined
dual-region:

| Predefined dual-region name | Region Name | Region Description |
| --- | --- | --- |
| `ASIA1` | `ASIA-NORTHEAST1` + `ASIA-NORTHEAST2` | Tokyo + Osaka |
| `EUR4` | `EUROPE-NORTH1` + `EUROPE-WEST4` | Finland + Netherlands |
| `EUR5` | `EUROPE-WEST1` + `EUROPE-WEST2` | Belgium + London |
| `EUR7` | `EUROPE-WEST2` + `EUROPE-WEST3` | London + Frankfurt |
| `EUR8` | `EUROPE-WEST3` + `EUROPE-WEST6` | Frankfurt + Zürich |
| `NAM4` | `US-CENTRAL1` + `US-EAST1` | Iowa + South Carolina |

#### Request routing for dual-region buckets

When you access data in a dual-region bucket from a resource that's located in
one of the regions of the dual-region, the request is routed to that same region
to provide the best performance. For example, if you have a dual-region bucket
in the `NAM4` dual-region (which consists of the `us-central1` and `us-east1`
regions) and you make a request from a VM in `us-east1`, the request will be
served by `us-east1`. In the event of a regional outage, requests are
automatically failed over to the other region.

### Multi-regions

| Multi-Region Name | Multi-Region Description |
| --- | --- |
| `ASIA` | Data centers in Asia, excluding Hong Kong and Indonesia |
| `EU` | Data centers within member states of the European Union\* |
| `US` | Data centers in the United States |

\* Object data added to a bucket in the `EU` multi-region is not
stored in the `EUROPE-WEST2` (London) or `EUROPE-WEST6` (Zürich) regions.

## What's next

- Learn about specialized AI zones for AI and machine learning training.
- Create a bucket.
- Get the location for an existing bucket by viewing the bucket's metadata.
- Learn more about availability and durability in Cloud Storage.
- View all the Google Cloud services available in locations worldwide.
- Explore additional location-based concepts, such as zones, that apply
  to other Google Cloud services.

## Try it for yourself

If you're new to Google Cloud, create an account to evaluate how
Cloud Storage performs in real-world
scenarios. New customers also get $300 in free credits to run, test, and
deploy workloads.

Try Cloud Storage free
