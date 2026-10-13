---
doc_id: sql-idle-recommender
title: Identify idle Cloud SQL instances
url: https://docs.cloud.google.com/sql/docs/postgres/recommender-sql-idle
category: cost
fetched_at: '2026-10-13T15:13:49+00:00'
license: CC BY 4.0 (Google Cloud documentation)
---

MySQL
  |  PostgreSQL
  |  SQL Server

The Cloud SQL idle instance recommender helps
you detect instances that might be idle and provides you
insights and recommendations to help you reduce costs. This page describes how
this recommender works and how to use it.

## How it works

The Cloud SQL idle instance recommender analyzes the usage metrics of primary
instances that are older than 30 days. For each instance, the recommender
considers the values of certain metrics
within an observation period spanning the last 30 days. The recommender does not
analyze read replicas.

If the activity level within the observation period is below a certain
threshold, the recommender estimates that the instance is idle. Recommendations are
generated every 24 hours for shutting down such instances.

**Warning:** It's highly recommended
that you evaluate the insights and in-context charts. Consult with the
appropriate team to determine whether the flagged instance is inadvertently idle
and can be deleted.

## Pricing

The Cloud SQL idle instance recommender is in the *Standard* Recommender pricing tier.

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

## List idle Cloud SQL instance recommendations

You can list idle instance recommendations by
using the Google Cloud console, `gcloud`, or the Recommender API.

### Console

To list recommendations about idle instances by using the
Google Cloud console, follow these steps:

1. Go to the **Cloud SQL Instances** page.

   Go to Cloud SQL Instances
2. Click **View all** on the idle instance recommendations banner.

Alternatively, follow these steps:

1. Go to the **Active Assist**.

   Go to the Active Assist

   For more information, see
   Getting started with Recommendation Hub.
2. In the **Reduce Cloud SQL instance cost** card, click **View all**.
3. Click the **Shut down instance** tab.

### gcloud

To list recommendations about idle instances by using `gcloud`, run the
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
- `RECOMMENDER`: The ID of the recommender as `IdleRecommender`.

### API

To list recommendations about idle instances by using the
Recommendations API, call the
`recommendations.list`
method as follows.

```
GET https://recommender.googleapis.com/v1beta1/projects/PROJECT-ID/locations/LOCATION/recommenders/google.cloudsql.instance.RECOMMENDER/recommendations
```

Replace the following:

- `PROJECT_ID`: Your project ID.
- `LOCATION`: A region, such as `us-central1`.
- `RECOMMENDER`: The ID of the recommender as `IdleRecommender`.

If the recommender detects idle instances, it lists them in a
table. Each row shows the instance name, a brief recommendation, the location,
and the last refresh date.

## View insights and detailed recommendations

You can view insights and detailed recommendations about idle instances by
using the Google Cloud console, `gcloud`, or the Recommender API.

### Console

To view insights about an idle instance by using the
Google Cloud console, click the recommendation button in the list of instances.

### gcloud

To view insights and detailed recommendations about idle instances by using `gcloud`, run the
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
- `INSIGHT_TYPE`: The ID of the insight type as `ActivityInsight`.

### API

To view insights and detailed recommendations about idle instances by using the
Recommendations API, call the
`insights.list`
method as follows:

```
GET https://recommender.googleapis.com/v1beta1/projects/PROJECT-ID/locations/LOCATION/insightTypes/google.cloudsql.instance.INSIGHT_TYPE/insights
```

Replace the following:

- `PROJECT_ID`: Your project ID.
- `LOCATION`: A region, such as `us-central1`.
- `INSIGHT_TYPE`: The ID of the insight type as `ActivityInsight`.

A panel appears showing insights about the idle instance. The following
categories of information are provided along with some supporting charts.

| Fields | Descriptions and related metrics |
| --- | --- |
| **Disk usage (bytes change)** | Data utilization in bytes. Sampled every 60 seconds.   Pertains to `database/disk/bytes_used`. |
| **Max CPU utilization** | The maximum CPU utilization as a percentage.   Pertains to `database/cpu/utilization`. |
| **Max memory utilization** | The maximum memory utilization as a percentage.   Pertains to `database/memory/utilization`. |
| **Max disk read ops count** | The maximum number of read operations.   Pertains to `database/disk/read_ops_count`. |
| **Max disk write ops count** | The maximum number of write operations.   Pertains to `database/disk/write_ops_count`. |
| **Observation start and end dates** | The start and end dates of the 30-day observation period. |

The following table lists the insight and recommendation that the Cloud SQL
idle instance recommender might generate to help you reduce costs. The subtypes
are visible in the `gcloud` and API results.

| Insight | Recommendation |
| --- | --- |
| The instance has shown low levels of activity during the observation period.   Subtype: `LOW_ACTIVITY` Investigate to check if the instance can be shut down to reduce costs.  Subtype: `SHUTDOWN_INSTANCE` | |

## Apply recommendations

Evaluate the recommendations carefully and do any of the following:

- To examine the recommendation, click **View instance**.

  A banner appears at the top of the page providing a recommendation.

  You might find that the instance is intentionally idle and you don't need to shut
  it down. If it's inadvertently idle, you can stop
  and delete the instance. Stopping an
  instance suspends instance charges. The instance data is unaffected,
  and charges for storage and IP addresses continue to apply.

  Exercise caution when stopping
  or deleting an instance. To avoid
  the loss of data, create a backup first.
- To dismiss the recommendation so that it's de-emphasized and appears dimmed,
  click **Dismiss**.
- To close the panel without applying or dismissing the recommendation, click
  **Cancel**.

You can also export these recommendations to BigQuery
and examine them by using Data Studio or Looker.

## What's next

- Monitor disk availability
- Reduce overprovisioned Cloud SQL instances
- Blog: Maximize your Cloud ROI
- Blog: Do more with less
- Google Cloud recommenders
