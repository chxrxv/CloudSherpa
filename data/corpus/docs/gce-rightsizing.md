---
doc_id: gce-rightsizing
title: Apply machine type recommendations to VM instances
url: https://docs.cloud.google.com/compute/docs/instances/apply-machine-type-recommendations-for-instances
category: cost
fetched_at: '2026-10-13T15:13:49+00:00'
license: CC BY 4.0 (Google Cloud documentation)
---

Compute Engine provides machine type recommendations to help you
optimize the resource utilization of your virtual machine (VM) instances. These
recommendations are generated automatically based on system metrics gathered by
the Cloud Monitoring service over the previous 8 days. Use these
recommendations to resize your instance's machine type to more efficiently use
the instance's resources. This feature is also known as *rightsizing
recommendations*.

Compute Engine also lets you
customize the recommendations
that you receive about machine types and memory
(Preview).
To learn more about the available machine types for VM instances,
read the machine types documentation.

## Before you begin

- Read the Google Cloud console documentation.
- If you haven't already, set up authentication.
  Authentication verifies your identity for access to Google Cloud services and APIs. To run
  code or samples from a local development environment, you can authenticate to
  Compute Engine by selecting one of the following options:

  Select the tab for how you plan to use the samples on this page:

  ### Console

  When you use the Google Cloud console to access Google Cloud services and
  APIs, you don't need to set up authentication.

  ### gcloud

  1. Install the Google Cloud CLI.
     After installation,
     initialize the Google Cloud CLI by running the following command:

     ```
     gcloud init
     ```

     If you're using an external identity provider (IdP), you must first
     sign in to the gcloud CLI with your federated identity.

     **Note:** If you installed the gcloud CLI previously, make sure you have
     the latest version by running `gcloud components update`.
  2. Set a default region and zone.

  ### REST

  To use the REST API samples on this page in a local development environment, you use the
  credentials you provide to the gcloud CLI.

  Install the Google Cloud CLI.

  If you're using an external identity provider (IdP), you must first
  sign in to the gcloud CLI with your federated identity.

  For more information, see
  Authenticate for using REST
  in the Google Cloud authentication documentation.

## Pricing

Machine type recommendations are available at no charge. If you apply a
recommendation to resize your instance's machine type, you are charged for the
machine type that you choose.

## Limitations and use cases

Machine type recommendations are not available in the
following cases:

- VM instances created using App Engine flexible environment,
  Dataflow, Google Kubernetes Engine, or Managed Service for Apache Spark
- VM instances with ephemeral disks, GPUs, or TPUs
- VM instances in the
  memory-optimized machine family

The recommendation algorithm is suited to workloads that follow weekly
patterns, workloads that grow or shrink over weeks of time, workloads that
persistently underutilize their resources, or workloads that are persistently
throttled by insufficient resources. In such cases, 8 days of historical data is
enough to predict how a change in the size of the machine can improve resource
utilization.

The machine type recommendation algorithm is less suited to the following
workloads:

- Workloads that spike infrequently (for example, monthly spikes) because 8 days
  of data is not enough to capture or predict the CPU fluctuations.
- Workloads that have very brief CPU spikes because recommendations are based on
  average CPU utilization over 60-second intervals.
  Recommendations might not be
  generated quickly enough to capture shorter spikes. See
  How machine type recommendations work
  for more information.

For workloads where cost is more important to you than performance, such as
batch workloads, you can ignore recommendations to increase size.

In rare cases, you might see an error message when applying a recommendation.
For example, a recommended machine type might be too small for the number of
attached disks, it might not meet the resource requirements of your images or
licenses, or it might not be available in a particular zone.

We also don't show recommendations if the estimated saving is less than
$10/month.

## How machine type recommendations work

Compute Engine monitors the CPU and memory utilization of running
VMs and makes recommendations using the last 8 days of data.
Compute Engine makes recommendations like the following:

- If your instance has had low CPU utilization most of the time,
  Compute Engine recommends a machine type with fewer virtual CPUs.
- If your instance has had high CPU utilization most of the time,
  Compute Engine recommends a machine type with more virtual CPUs.
- If your instance hasn't used a large fraction of its memory,
  Compute Engine recommends a machine type with less memory.
- If your instance has actively been using a large fraction of its memory most
  of the time, Compute Engine recommends a machine type with more
  memory.

**Note:** Compute Engine uses the same CPU utilization numbers that are
reported on the
Compute Engine dashboard to
determine what recommendations to make. These numbers are based on the average
utilization of your instances over 60-second intervals, so they don't capture
short CPU spikes. Apps with short CPU spikes might need to run on a
larger machine type than the one recommended by Google, to accommodate these
spikes.

Compute Engine might make recommendations to use either a standard or
custom machine type. Note that there are some limitations in the amount of
memory and vCPU available to a machine. In particular, increasing one resource
might require increasing the other at the same time, to follow the
specifications
of a valid machine type. Also, Compute Engine only recommends
machine types that are available in the zone where the instance is running.

See
custom machine type specifications
for details.

For cost difference estimations, the cost of an instance is based on
the previous week's usage (before sustained use discount) and is extrapolated
to 30 days. This is then compared to the recommended machine type monthly cost
(before sustained use discount). For accurate pricing and details, read the
pricing documentation.

Recommendations are generated by monitoring your CPU and memory utilization
based on the metrics we have
available for your machines. To improve the accuracy of your recommendations,
consider installing the
Ops Agent.

## View machine type recommendations

Compute Engine makes recommendations available through the
Google Cloud console. Recommendations are also available through the
Recommender using the gcloud CLI or
REST.

#### Permissions required for this task

To perform this task, you must have the following
permissions:

- `recommender.computeInstanceMachineTypeRecommendations.list` on the project

### Console

1. In the Google Cloud console, go to the **VM instances** page.

   Go to the VM instances page
2. Look at the **Recommendation** column to review recommendations for
   individual instances. You can also sort the column by amount of estimated
   savings. If there are no recommendations next to your instances,
   Compute Engine doesn't have any recommendations to make.

### gcloud

Use the `gcloud recommender recommendations list`
command and specify the
VM instance rightsizing recommender.

```
gcloud recommender recommendations list \
    --recommender=google.compute.instance.MachineTypeRecommender \
    --project=PROJECT_ID \
    --location=ZONE \
    --format=[config | csv | default | diff | flattened | get | json | list | object | table | text | value | yaml]
```

Replace the following:

- `PROJECT_ID`: the ID of your project.
- `ZONE`: the zone that contains instances
  to list recommendations for.
- `FORMAT`: your preferred output format.
  - `csv`, `diff`, `get`, `table`, and `value` require non-empty
    projections.

The output of the `gcloud recommender recommendations list` command includes
the following fields:

- `name`: the name of the recommendation.
- `description`: a human-readable explanation of the recommendation.
- `operationGroups`:
  groups of operations that you can perform in serial order to
  apply the recommendation.

For more information, see
the Recommender documentation.

### REST

Use the
Recommender API
with the VM instance rightsizing Recommender ID.

```
PROJECT_ID=my-project
LOCATION=us-central1-c
RECOMMENDER_ID=google.compute.instance.MachineTypeRecommender

curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
  https://recommender.googleapis.com/v1/projects/$PROJECT_ID/locations/$LOCATION/recommenders/$RECOMMENDER_ID/recommendations
```

The response includes the following fields:

- `name`: The name of the recommendation.
- `description`: A human-readable explanation of the recommendation.
- `operationGroups`:
  Groups of operations that you can perform in serial order to
  apply the recommendation.

For more information, see
the Recommender documentation.

When you create an instance, recommendations for the instance appear
24 hours after the instance was created. If you change the machine type
of an instance, Compute Engine provides any further
recommendations within 24 hours after the change.

After that, VM instance recommendations are refreshed at regular intervals
throughout the day.

## Change machine types according to recommendations

**Note:** You might have valid reasons for running a particular instance at very low
or very high utilization. Machine type recommendations are suggestions to help
you more efficiently use your instances, but they might not be appropriate
for every situation.

If you determine that you want to apply the recommendations made by
Compute Engine, you can change the instance's machine type directly
from the recommendations screen, or manually step through the operations
that are returned when
viewing machine type recommendations.

#### Permissions required for this task

To perform this task, you must have the following
permissions:

- `compute.instances.setMachineType` on the instance
- `compute.instances.start` on the instance
- `compute.instances.stop` on the instance
- `recommender.computeInstanceMachineTypeRecommendations.update`
  on the project

### Console

1. In the Google Cloud console, go to the **VM instances** page.

   Go to the VM instances page

   If a recommendation exists for an instance, it appears in the
   **Recommendation** column.
2. Click the recommendation text for the instance you want to resize.
3. A dialog opens with information about the recommendation.
   To apply the recommendation and change the VM machine type, click
   **Apply**.
   Compute Engine stops the instance, changes its machine type,
   and restarts the instance.
4. Optionally, you can also click the **Customize** link to customize the
   instance as you prefer.
5. Click the **Apply** button to apply the changes.

### gcloud

See Changing a machine type
for information.

### REST

See Changing a machine type
for information.

## Dismiss and restoring recommendations

When you have finished using a recommendation, you can dismiss it
from the console.
Within the console, dismissing removes a recommendation from the total savings
estimate and also minimizes the appearance of the recommendation so that it
appears dimmed.

Acting on a recommendation through the console does not affect
the list of or states of recommendations that are returned by the
Recommender API. To manage the state of
recommendations returned by the Recommender API, see
Using the API.

#### Permissions required for this task

To perform this task, you must have the following
permissions:

- `recommender.computeInstanceMachineTypeRecommendations.update`
  on the project

To dismiss a single recommendation from the console:

1. In the Google Cloud console, go to the **VM instances** page.

   Go to the VM instances page

   If a recommendation exists for an instance, it appears in the
   **Recommendation** column.
2. Click the recommendation text for the recommendation you want to dismiss.
3. A dialog opens with more detail and a **Dismiss recommendation**
   button.
4. Click **Dismiss recommendation**.

To dismiss all recommendations from the console:

1. In the Google Cloud console, go to the **VM instances** page.

   Go to the VM instances page
2. Click the **Dismiss all** button.

**Note:** Dismissing a recommendation de-emphasizes it in the table but does not
hide it.

To restore a recommendation:

1. In the Google Cloud console, on the **VM instances** page, click the
   dimmed recommendation text you want to restore.
2. A dialog opens with more detail and a **Restore recommendation**
   button.
3. Click **Restore recommendation**.

## Use the Ops Agent for more precise recommendations

Cloud Monitoring offers a
Ops Agent that
collects additional disk, CPU, network, and process metrics from your VM
instances. To collect this data, install the Ops Agent on
your VM instances so it can access system resources and app services.

If the Ops Agent is installed and running on a VM
instance, the CPU and memory metrics collected by the agent are automatically
used to compute machine type recommendations. The
agent metrics provided by
the Ops Agent give better insights into resource
utilization of the instance than the default Compute Engine metrics.
This allows the recommendation engine to estimate resource requirements better
and make more precise recommendations.

To install the agent, see
Install the Ops Agent.

**Note:** Metric data from the Ops Agent is priced by volume
on a sliding scale. For details, see
Cloud Monitoring pricing.

## What's next

- Learn how to
  configure machine type recommendations.
- Learn more about
  changing the machine type
  of an instance.
- Read up on what happens when you
  stop an instance.
- Review the Google Cloud console documentation.
- Learn more about the Recommender and
  its API.
- Learn more about
  insights for machine type recommendation.
