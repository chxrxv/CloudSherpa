---
doc_id: sql-overprovisioned-recommender
title: Reduce overprovisioned Cloud SQL instances
url: https://docs.cloud.google.com/sql/docs/postgres/recommender-sql-overprovisioned
category: cost
fetched_at: '2026-10-13T15:13:49+00:00'
license: CC BY 4.0 (Google Cloud documentation)
---

MySQL
  |  PostgreSQL
  |  SQL Server

The Cloud SQL overprovisioned instance recommender
helps you detect instances that are unnecessarily large for a given workload.
It then provides recommendations on how to resize such instances and reduce
cost. This page describes how this recommender works and how to use it.

## How it works

The Cloud SQL overprovisioned recommender analyzes the usage metrics
of primary instances that are older than 30 days. For each instance, the
recommender considers the CPU and memory utilization based on the values of
certain metrics within the last 30 days.
The recommender does not analyze read replicas or instances configured for high availability (HA).

If the peak utilization of either or both the CPU and the memory within the
observation period is low, the instance is estimated to be overprovisioned.
Recommendations are generated every 24 hours for rightsizing such instances when
the estimated monthly cost savings are greater than or equal to $10.

The recommender uses conservative thresholds to ensure that it flags only
instances that are significantly overprovisioned, which is usually a good
indicator of waste. The recommender suggests a machine type that has at least
8 vCPUs and 32 GB.

**Warning:** It's highly recommended that you evaluate the insights
and in-context charts. Consult with the appropriate team to determine whether the
flagged instance is inadvertently overprovisioned and a smaller instance might
meet the needs of your application.

## Pricing

The Cloud SQL overprovisioned instance recommender is in the *Standard*
Recommender pricing tier.

## Before you begin

Before you can view recommendations and insights, do the following:

- To get the permissions to view and work with insights and recommendations,
  ensure that you have the required roles.

  | Tasks | Roles |
  | --- | --- |
  | View recommendations | One of these roles: `recommender.cloudsqlViewer` or `cloudsql.viewer`. |
  | Apply recommendations | One of these roles: `recommender.cloudsqlAdmin`, `cloudsql.editor`, or `cloudsql.admin`. |

  For more information about roles, see
  understanding roles and
  granting IAM permissions.- Enable the Recommender API, if it is not already enabled.

    **Roles required to enable APIs**

    To enable APIs, you need the `serviceusage.services.enable` permission. If you
    created the project, then you likely already have this permission through the
    Owner role (`roles/owner`). Otherwise, you can get this permission through the
    Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`).
    Learn how to grant roles.

    Enable the API

## List overprovisioned Cloud SQL instance recommendations

You can list overprovisioned instance recommendations by
using the Google Cloud console, `gcloud`, or the Recommender API.

### Console

To list recommendations about overprovisioned instances by using the
Google Cloud console, follow these steps:

1. Go to the **Cloud SQL Instances** page.

   Go to Cloud SQL Instances
2. Click **View all** on the overprovisioned instance recommendations banner.

Alternatively, follow these steps:

1. Go to the **Active Assist**.

   Go to the Active Assist

   For more information, see
   Getting started with Recommendation Hub.
2. In the **Reduce Cloud SQL instance cost** card, click **View all**.
3. Click the **Reduce instance** tab.

### gcloud

To list recommendations about overprovisioned instances by using `gcloud`, run the
`gcloud recommender recommendations list`
command as follows:

```
gcloud recommender recommendations list \
--project=PROJECT_ID \
--location=LOCATION \
--recommender=google.cloudsql.instance.RECOMMENDER
```

Replace the following:

- `PROJECT_ID`: Your project ID.
- `LOCATION`: A region, such as `us-central1`.
- `RECOMMENDER`: The ID of the recommender as `OverprovisionedRecommender`.

### API

To list recommendations about overprovisioned instances by using the
Recommendations API, call the
`recommendations.list`
method as follows:

```
GET https://recommender.googleapis.com/v1beta1/projects/PROJECT-ID/locations/LOCATION/recommenders/google.cloudsql.instance.RECOMMENDER/recommendations
```

Replace the following:

- `PROJECT_ID`: Your project ID.
- `LOCATION`: A region, such as `us-central1`.
- `RECOMMENDER`: The ID of the recommender as `OverprovisionedRecommender`.

If the recommender detects overprovisioned instances, it lists them in a
table. Each row shows the instance name, a brief recommendation, the current machine type,
the recommended machine type, the location, and the last refresh date.

## View insights and detailed recommendations

You can view insights and detailed recommendations about overprovisioned instances by
using the Google Cloud console, `gcloud`, or the Recommender API.

### Console

To view insights and detailed recommendations about an overprovisioned instance by using the
Google Cloud console, click the recommendation button in the list of instances.

### gcloud

To view insights and detailed recommendations about overprovisioned instances by using `gcloud`, run the
`gcloud recommender insights list`
command as follows:

```
gcloud recommender insights list \
--project=PROJECT_ID \
--location=LOCATION \
--insight-type=google.cloudsql.instance.INSIGHT_TYPE
```

Replace the following:

- `PROJECT_ID`: Your project ID.
- `LOCATION`: A region, such as `us-central1`.
- `INSIGHT_TYPE`: The ID of the insight type as
  `CpuUsageInsight` or `MemoryUsageInsight`, which provide insights
  about CPU usage and memory, respectively.

### API

To view insights and detailed recommendations about overprovisioned instances by using the
Recommendations API, call the
`insights.list`
method as follows:

```
GET https://recommender.googleapis.com/v1beta1/projects/PROJECT-ID/locations/LOCATION/insightTypes/google.cloudsql.instance.INSIGHT_TYPE/insights
```

Replace the following:

- `PROJECT_ID`: Your project ID.
- `LOCATION`: A region, such as `us-central1`.
- `INSIGHT_TYPE`: The ID of the insight type as `CpuUsageInsight`.
  or `MemoryUsageInsight`, which provide insights about CPU usage and memory,
  respectively.

A panel appears showing insights about the current memory and CPU utilization
of the instance. The following categories of information are provided
along with some supporting charts.

| Fields | Descriptions and related metrics |
| --- | --- |
| **Max CPU utilization** | The maximum CPU utilization as a percentage.   Pertains to `database/cpu/utilization`. |
| **Max memory utilization** | The maximum memory utilization as a percentage.   Pertains to `database/memory/utilization`. |

The following table lists the insights and recommendations that the Cloud SQL
overprovisioned instance recommender might generate to help you reduce costs.
The subtypes are visible in the `gcloud` and API results.

| Insights | Recommendations |
| --- | --- |
| Based on the current CPU utilization trends, the instance is flagged as overprovisioned.   Subtype: `LOW_CPU_UTILIZATION` Reduce the number of vCPUs or switch to a machine with fewer vCPUs.  Subtype: `CHANGE_INSTANCE_SIZE` | |
| Based on the current memory utilization trends, the instance is flagged as overprovisioned.  Subtype: `LOW_MEMORY_UTILIZATION`. Reduce the memory requirement or switch to a machine with less memory.  Subtype: `CHANGE_INSTANCE_SIZE` | |

## Apply recommendations

Evaluate the recommendations carefully and do any of the following:

- To examine the recommendation, click **View instance**.

  A banner appears at the top of the page providing a recommendation.

  Edit the instance, if required, to
  reduce the vCPUs or memory. Alternatively, switch to a machine type with fewer
  vCPUs and less memory.
  You don't need to rightsize the instance exactly as recommended. Use your
  judgement about instance size based on how you intend to provision the instance.
  Keep in mind that the bigger the size, the greater the operational latency.
- To dismiss the recommendation so that it's de-emphasized and appears dimmed,
  click **Dismiss**.
- To close the panel without applying or dismissing the recommendation, click
  **Cancel**.

You can also export these recommendations to BigQuery
and then examine them using Data Studio or Looker.

## What's next

- Monitor disk availability
- Reduce idle Cloud SQL instances
- Blog: Maximize your Cloud ROI
- Blog: Do more with less
- Google Cloud recommenders
