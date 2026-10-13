---
doc_id: gke-autopilot
title: GKE Autopilot overview
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview
category: compute
fetched_at: '2026-10-13T15:13:49+00:00'
license: CC BY 4.0 (Google Cloud documentation)
---

Autopilot

*Autopilot* is a managed mode of operation in Google Kubernetes Engine (GKE).
This page describes the benefits of Autopilot mode and provides
information about planning clusters, deploying workloads, and configuring
networking and security. Admins, Architects and Operators
can use this information to make informed decisions when evaluating how
GKE Autopilot mode aligns with the operational
requirements of their containerized workloads.

For more information about the differences between modes of operation in
GKE, see
Compare GKE Autopilot and Standard.

## What is Autopilot?

GKE Autopilot is a mode of operation in
GKE in which Google manages your infrastructure configuration,
including your nodes, scaling, security, and other preconfigured settings.
Autopilot mode is optimized to run most production workloads, and
provisions compute resources based on your Kubernetes manifests.

You can run an entire cluster in Autopilot mode, so that the cluster
and all of its workloads follow GKE best practices and
recommendations for scaling, security, upgrades, and node configuration.
You can also run specific workloads in Autopilot mode in
GKE Standard clusters. This option lets you use
Autopilot in environments where you still require manual control over
your infrastructure. For more information, see
About Autopilot mode workloads in GKE Standard.

**Best practice**:

Use Autopilot clusters for the most streamlined experience.

### Benefits

- **Focus on your apps**: Google manages the infrastructure, so you can focus
  on building and deploying your applications.
- **Security**: Autopilot clusters have a default hardened
  configuration, with many security settings enabled by default.
  GKE automatically applies security patches to your nodes
  when available, adhering to any maintenance schedules you configured.
- **Pricing**: the Autopilot pricing model simplifies billing
  forecasts and attribution.
- **Node management**: Google manages worker nodes, so you don't need to
  create new nodes to accommodate your workloads or configure automatic
  upgrades and repairs.
- **Scaling**: when your workloads experience high load and you add more Pods
  to accommodate the traffic, such as with Kubernetes Horizontal Pod
  Autoscaling, GKE automatically provisions new nodes for those
  Pods, and automatically expands the resources in your existing nodes based
  on need.
- **Scheduling**: Autopilot manages Pod bin-packing for you, so you
  don't have to think about how many Pods are running on each node. You can
  further control Pod placement by using Kubernetes mechanisms such as
  affinity and Pod spread topology.
- **Resource management**: if you deploy workloads without setting resource
  values such as CPU and memory, Autopilot automatically sets
  pre-configured default values and modifies your resource requests at the
  workload level.
- **Networking**: Autopilot enables some networking security features
  by default, such as passing all Pod network traffic through your
  Virtual Private Cloud firewall rules, even if the traffic is going to other Pods in
  the cluster.
- **Release management**: all Autopilot clusters are enrolled in a
  GKE release channel so that your control plane and nodes run
  on the latest qualified versions in that channel.
- **Managed flexibility**: if your workloads have specific hardware or
  resource requirements, such as GPUs, you can define those requirements in
  ComputeClasses.
  When you request a ComputeClass in your workload, GKE
  uses your requirements to configure nodes for your Pods. You don't need to
  manually configure hardware for nodes or for individual workloads.
- **Reduced operational complexity**: Autopilot reduces platform
  administration overhead by removing the need to continuously monitor nodes,
  scaling, and scheduling operations.

Autopilot comes with a SLA that covers both
the control plane and the compute capacity used by your Pods.

## About the Autopilot container-optimized compute platform

In GKE version 1.32.3-gke.1927002 and later,
Autopilot includes a specialized *container-optimized compute
platform* for your workloads. This platform works well for most general-purpose
workloads that don't require specific hardware, such as web servers and
medium-intensity batch jobs.

The container-optimized compute platform uses GKE
Autopilot nodes that can dynamically resize while running, designed to
scale up from fractions of a CPU with minimal disruptions. This dynamic resizing
significantly reduces the time that's needed to provision new capacity as your
workloads scale. To improve the speed of scaling and resizing,
GKE also maintains a pool of pre-provisioned compute capacity
that can be automatically allocated for workloads in response to increased
resource demands. Because the underlying machine series isn't fixed, per-CPU
performance varies depending on which machine series GKE
schedules your Pod on.

**Note:** This extra compute capacity can increase IP address utilization. If you
want to avoid extra IP address consumption, you can turn off proactive capacity
provisioning by using the `--autopilot-general-profile=no-performance` flag.
Using this flag reduces the performance of Autopilot capacity
provisioning for general-purpose workloads.

The container-optimized compute platform provides the following benefits:

- **Compute capacity matches workloads**: Autopilot dynamically adjusts
  the compute capacity for the container-optimized compute platform based on
  factors like the number of Pods and resource consumption. As a result,
  the compute capacity in the cluster matches the needs of your workloads.
- **Fast scaling times**: during scale-up events, GKE can
  dynamically resize existing nodes to accommodate more Pods or increased
  resource consumption. This dynamic capacity provisioning often means that
  new Pods don't need to wait for new nodes to boot up. Node resizing isn't
  supported for Arm workloads.
- **Multi-architecture support**: the container-optimized compute platform
  supports both x86 and Arm architectures for your general-purpose workloads.
  By default, workloads use the x86 architecture. You can run workloads on the
  general-purpose Arm platform by specifying the `kubernetes.io/arch: arm64`
  node selector, or by selecting the `autopilot-arm` or
  `autopilot-arm-spot` ComputeClasses.

You can use the Autopilot container-optimized compute platform in
the following ways:

- **Autopilot clusters**: Pods that don't select specific hardware use
  this compute platform by default.
- **Standard clusters**:
  - Built-in Autopilot ComputeClasses.
  - `podFamily` priority rules in
    custom Autopilot ComputeClasses.

## Pricing

Autopilot pricing uses different models depending on the type of
hardware that your Pods use, as follows:

- **General-purpose Autopilot Pods**: the following types of Pods
  use a *Pod-based billing model* and are categorized as *general-purpose Pods*:

  - Pods that run on the container-optimized compute platform in
    Autopilot clusters or Standard clusters.
  - Pods that select the `Balanced` or `Scale-Out` built-in ComputeClasses in
    Autopilot clusters.

  For more information, the "General-purpose Autopilot workloads"
  section in
  Google Kubernetes Engine pricing.
- **Autopilot workloads that select specific hardware**: Pods that
  select specific hardware, such as Compute Engine machine series or
  hardware accelerators, use a *node-based billing model*. In this model, you
  pay for the underlying hardware and a node management premium.

  For more information, see the "Autopilot workloads that select
  specific hardware" section in
  Google Kubernetes Engine pricing.

## Autopilot clusters and workloads

GKE lets you use Autopilot mode for entire clusters or
for specific workloads in your Standard clusters. Autopilot
clusters are the recommended way to use GKE, because the entire
cluster uses Google's best practices by default.

However, some organizations have requirements for manual control or for
flexibility that require using a GKE Standard cluster.
In these cases, you can still use Autopilot for specific workloads in
your Standard clusters, which lets you benefit from many
Autopilot features at the workload level.

The following sections show you how to plan and create Autopilot
clusters. If you have a Standard cluster and you want to run some of
your workloads in Autopilot mode, see
About Autopilot mode workloads in GKE Standard.

## Plan your Autopilot clusters

Before you create a cluster, plan and design your Google Cloud architecture.
In Autopilot, you request hardware in your workload specifications.
GKE provisions and manages the corresponding infrastructure to
run those workloads. For example, if you run machine learning workloads, you
request hardware accelerators.

Plan and request quota for your Google Cloud project or organization based
on the scale of your workloads. GKE can only provision
infrastructure for your workloads if your project has enough quota for that
hardware.

Consider the following factors during planning:

- Estimated cluster size and scale
- Workload type
- Cluster layout and usage
- Networking layout and configuration
- Security configuration
- Cluster management and maintenance
- Workload deployment and management
- Logging and monitoring

The following sections provide information and useful resources for these
considerations.

### Networking

When you create an Autopilot cluster with public networking, workloads
in the cluster can communicate with each other and with the internet. This is
the default networking mode. Google Cloud and Kubernetes provide various
additional networking features and capabilities that you can use based on
your requirements, such as clusters with
private networking.

Networking in Kubernetes and in the cloud is complex. Before you start changing
the defaults that
Google Cloud sets for you, ensure that you're familiar with
the basic concepts of networking. The following table provides you with resources
to learn more about networking in GKE based on your use case:

| Use case | Resources |
| --- | --- |
| Understand how networking works in Kubernetes and GKE | - Learn the Kubernetes networking model. - Learn the GKE networking model.   After you learn the networking model, consider your organization's networking and network security requirements. Choose GKE and Google Cloud networking features that satisfy those criteria. |
| Plan your GKE networking configuration | We recommend that you understand the networking quotas for GKE, such as endpoints per Service and API request limits. The following resources will help you to plan specific aspects of your networking setup:   - To learn about networking options inside and outside the cluster,   read the GKE networking overview. - To learn our recommendations for network design, read   the Best practices for GKE networking. - To learn how to optimize your IP address management, read the   GKE address management series. - To learn what firewall rules GKE creates based on   the Kubernetes resources you create, refer to   Automatically created firewall rules. |
| Expose your workloads | - To expose your apps to the internet, use Services,   which let you expose an app running in a group of Pods as a single   network service. - To configure workloads to securely communicate with   Google Cloud APIs, use   Workload Identity Federation for GKE. |
| Run highly-available connected services in multiple clusters | Use multi-cluster Services (MCS). |
| Load balance incoming traffic | - To load balance external HTTP(S) traffic to multiple Services based on URIs   and paths, for example a complex web application, use   Ingress for external Application Load Balancers. - To load balance external traffic to a single Service, such   as a Deployment running a public email server, use a   LoadBalancer Service   to create a regional external passthrough Network Load Balancer. - To load balance internal HTTP(S) traffic to multiple Services based   on URIs and paths, such as with a web application in your company   intranet, use   Ingress for internal Application Load Balancers. - To load balance internal traffic to a single Service, such as with   a corporate email server, use an   internal passthrough Network Load Balancer. |
| Configure cluster network security | - To control or prevent access to your cluster from the public   internet, customize your network isolation   customize your network isolation. - To restrict control plane access to specific IP address ranges, use   control plane authorized networks. - To control Pod traffic, use network policies. Network policy enforcement is available with GKE Dataplane V2, which is enabled by default in Autopilot clusters. For instructions, see   network policies. |
| Observe your Kubernetes network traffic | By default, Autopilot use GKE Dataplane V2 for metrics and observability .   - To ingest the GKE Dataplane V2 metrics, configure Google Cloud Managed Service for Prometheus. By default, GKE Dataplane V2 metrics are exposed in GKE Autopilot. - To access visualizations, Network Policy verdicts, and flow dumps, configure additional troubleshooting tools using GKE Dataplane V2 observability. |

### Scaling

Operating a platform effectively at scale requires planning and careful
consideration. You must consider the *scalability* of your design, which is the
ability of your clusters to grow while remaining within service-level objectives
(SLOs). For detailed guidance for both platform administrators and developers,
refer to the
Guidelines for creating scalable clusters.

You should also consider the GKE
quotas and limits, especially if
you plan to run large clusters with potentially thousands of Pods.

In Autopilot, GKE automatically scales your nodes based
on the number of Pods in your cluster. If a cluster has no running workloads,
Autopilot can automatically scale the cluster down to zero nodes.
Following cluster scale-down, no nodes remain in the cluster and system Pods
are consequently in an unschedulable state. This is expected behavior. In most
newly created Autopilot clusters, you might notice that the first
workloads that you deploy take more time to schedule. This is because the new
Autopilot cluster starts with zero usable nodes upon creation and
waits until you deploy a workload to provision additional nodes.

**Best practice**:

To automatically scale the number of Pods
in your cluster, use a mechanism such as Kubernetes
horizontal Pod autoscaling,
which can scale Pods based on the built-in CPU and memory metrics, or based on
custom metrics from Cloud Monitoring. In addition, Autopilot enables
vertical Pod autoscaling
by default. To optimize container CPU requests while autoscaling replicas, you
can use
HPA rightsizing with VPA
(Preview). To learn how to configure horizontal scaling based on various
metrics, refer to
Configuring horizontal Pod autoscaling.

### Security

Autopilot clusters enable and apply security best practices and
settings by default, including many of the recommendations in
Harden your cluster security
and the
GKE security overview.

If you run Autopilot workloads in your Standard clusters,
GKE applies various Autopilot security measures to those
workloads on a best-effort basis. You can strictly
enforce specific Autopilot security policies in the entire Standard cluster. If you enforce all of the available
Autopilot policies, then your Standard cluster has a similar
operational environment to an Autopilot cluster.

If you want to learn more about Autopilot hardening measures and how to
implement your specific security requirements, refer to
Security measures in Autopilot.

## Create a cluster

After planning your environment and understanding your requirements,
create an Autopilot cluster.
New Autopilot clusters are regional clusters that have a publicly
accessible IP address. Each cluster has baseline hardening measures applied, as
well as automatic scaling and other features. For a full list of pre-configured
features, refer to
Compare GKE Autopilot and Standard.

If you want to create the cluster with no access to external IP addresses,
configure your network isolation.

## Deploy workloads in Autopilot mode

You can run compatible Kubernetes workloads in Autopilot mode so that
GKE manages scaling, efficient scheduling, and the underlying
infrastructure. You can use the container-optimized compute platform for your
general-purpose workloads, or you can select specific hardware for your
workloads by using a
ComputeClass.

You can run these Autopilot workloads in one of the following ways:

- Deploy the workloads to an Autopilot cluster.
- Select an Autopilot ComputeClass
  when you deploy the workloads to a Standard cluster.

For an interactive guide in the Google Cloud console for deploying and
exposing an app in an Autopilot cluster, click
**Guide me**:

Guide me

The following table shows some common requirements and provides recommendations
for what you should do:

| Use case | Resources |
| --- | --- |
| Control individual node properties when scaling a cluster | Create a custom ComputeClass and request it in your workload manifest. For more information, see About custom ComputeClasses. |
| Run Autopilot workloads in a Standard cluster | Use an Autopilot ComputeClass in the Standard cluster. For more information, see About Autopilot mode workloads in GKE Standard. |
| Run Arm workloads | For general-purpose workloads, request the Arm architecture and the `autopilot-arm` or `autopilot-arm-spot` built-in ComputeClass. For specific hardware requirements, request a machine series that has Arm CPUs in a custom ComputeClass. For more information, see About custom ComputeClasses. |
| Run accelerated AI/ML workloads | Request GPUs in a ComputeClass or in your workload manifest. For more information about requesting GPUs in your workload manifest, see Deploy GPU workloads in Autopilot. |
| Run fault-tolerant workloads such as batch jobs at lower costs. | - Use the `autopilot-spot` built-in ComputeClass. - Configure Spot VMs in a custom ComputeClass. - Select Spot Pods in your workload manifest.   You can use any ComputeClass or hardware configuration with Spot Pods. |
| Run workloads that require minimal disruptions, such as game servers or work queues | In Autopilot clusters only, specify the `cluster-autoscaler.kubernetes.io/safe-to-evict=false` annotation in the Pod specification. Pods are protected from eviction caused by node auto-upgrades or scale-down events for up to seven days. For more information, see Extend the run time of Autopilot Pods. |
| Let workloads burst beyond their requests if there are available, unused resources in the sum of Pod resource requests on the node. | Set your resource `limits` higher than your `requests` or don't set resource limits. For more information, see Configure Pod bursting in GKE. |

Autopilot lets you request CPU, memory, and ephemeral storage resources
for your workloads. The allowed ranges depend on whether you want to run your
Pods on the Autopilot container-optimized compute platform, or on
specific hardware. For information about the default container resource requests
and the allowed resource ranges, see
Resource requests in Autopilot.

### Workload separation

Autopilot clusters support using node selectors and node affinity to
configure *workload separation*. Workload separation is useful when you need to
tell GKE to place workloads on nodes that meet specific criteria,
such as custom node labels. For example, you can tell GKE to
schedule game server Pods on nodes with the `game-server` label and avoid
scheduling any other Pods on those nodes.

To learn more, refer to
Configure workload separation in GKE.

### Schedule Pods in specific zones using zonal topology

If you need to place Pods in a specific Google Cloud zone, for example
to access information on a zonal Compute Engine persistent disk, see
Place GKE Pods in specific zones.

### Pod affinity and anti-affinity

Use Pod affinity and anti-affinity to colocate Pods on a single node or to make
some Pods avoid other Pods. Pod affinity and anti-affinity tell Kubernetes to
make a scheduling decision based on the labels of Pods running on nodes in a
specific topology domain, such as a specific region or zone. For example, you
could tell GKE to avoid scheduling frontend Pods alongside other
frontend Pods on the same nodes to improve availability in case of an outage.

For instructions and more details, refer to
Pod affinity and anti-affinity.

In GKE, you can use Pod affinity and anti-affinity with the
following labels in `topologyKey`:

- `topology.kubernetes.io/zone`
- `kubernetes.io/hostname`

### Pod topology spread constraints

To improve the availability of your workloads as Kubernetes scales the
number of Pods up and down, you can set *Pod topology spread constraints*. This
controls how Kubernetes spreads your Pods across nodes within a topology domain,
such as a region. For example, you could tell Kubernetes to place a specific
number of game server session Pods in each of three Google Cloud zones in
the `us-central1` region.

For examples, more details, and instructions, refer to
Pod Topology Spread Constraints.

**Best practice**:

If you use `topologySpreadConstraints` with cluster autoscaling,
we recommend setting `nodeTaintsPolicy: Honor`. This setting helps
ensure that the cluster autoscaler correctly simulates Pod migration during
scale-down events, preventing potential scaling loops. Without this setting,
the autoscaler might scale down nodes in a way that violates topology spread
constraints, leading to immediate scale-up events and workload disruption.

The `whenUnsatisfiable: ScheduleAnyway` setting also helps to
prevent Pods from becoming unschedulable in case of temporary topology imbalances,
for example, during a zone failure.

## Manage and monitor your Autopilot clusters

In Autopilot, GKE automatically manages cluster upgrades
and maintenance for both the control plane and worker nodes. Autopilot
clusters also have built-in functionality for you to monitor your clusters and
workloads.

### GKE version upgrades

All Autopilot clusters are enrolled in a GKE
*release channel*. In release channels, GKE manages the
Kubernetes version of the cluster, balancing between feature availability and
version stability depending on the channel.
By default, Autopilot clusters are enrolled in the Regular release
channel, but you can select a different channel that meets your stability and
functionality needs. For more information about release channels, see
About release channels.

GKE automatically starts upgrades, monitors progress, and pauses
the operation if problems occur. You can manually control the upgrade process in
the following ways:

- To control when GKE *can* perform automatic upgrades,
  create
  maintenance windows.
  For example, you can set the maintenance window to the night before your
  multiplayer game's weekly reset, so that players can sign in at reset without
  disruptions.
- To control when GKE *can't* start automatic upgrades during a
  specific time range, use
  maintenance exclusions.
  For example, you can set a maintenance exclusion for the duration of your
  Black Friday and Cyber Monday sales event so that your customers can shop
  without issues.
- To get a new version before auto-upgrades start,
  manually upgrade the control plane.
  GKE reconciles the node version with the control plane
  version over time.
- To get a patch version that's only available in a newer release channel,
  see Run patch versions from a newer channel.
  For example, you might need a specific patch version to mitigate a recent
  vulnerability disclosure.

### Monitor your Autopilot clusters

Autopilot clusters already have Cloud Logging, Cloud Monitoring,
and Google Cloud Managed Service for Prometheus enabled.

Autopilot clusters collect the following types of logs and metrics
automatically, adhering to Google's best practices for telemetry collection:

**Logs for Cloud Logging**

- System logs
- Workload logs
- Admin Activity audit logs
- Data Access audit logs

**Metrics for Cloud Monitoring**

- System metrics
- Workload metrics (from Google Cloud Managed Service for Prometheus)

No additional configuration is required to enable logging and monitoring.
The following table shows you how to interact with the collected telemetry
based on your requirements:

| Use case | Resources |
| --- | --- |
| Understand and access your GKE logs | - To learn about the types of logs that we automatically   collect, see   What logs are collected. - To access the logs and to use the Cloud Logging user interface   in the Google Cloud console, see   Viewing your GKE logs. - For sample queries that you can use to filter Kubernetes system   and workload logs, see   Kubernetes-related queries. - For sample queries that you can use to filter Admin Activity and   Data Access audit logs, see   GKE audit logging information. - To configure logs for multi-tenant environments, for example when   teams have specific namespaces in a single GKE cluster   but each team has its own Google Cloud project, see   Multi-tenant logging on GKE. |
| Observe the performance of your GKE clusters | Effective monitoring of your cluster performance can help you to optimize the operating costs of your clusters and workloads.   - Use the GKE dashboard in Monitoring   to visualize the status of your clusters. To learn more, see   Observing your GKE clusters. - GKE also provides an **Observability**   dashboard in the Google Cloud console. For details, see   View observability metrics. |
| Monitor the security posture of your clusters | Use the security posture dashboard to audit your running workloads against GKE best practices, scan for vulnerabilities in your container operating systems and language packages, and get actionable mitigation recommendations. To learn more, see About the security posture dashboard. |

## Troubleshooting

For troubleshooting steps, refer to
Troubleshooting Autopilot clusters.

## What's next

- Learn how to compare features in Autopilot and Standard clusters.
- Create an Autopilot cluster.
- Learn more about Autopilot resource requests.
- Learn how to create a zonal cluster.
- Read an overview of Autopilot compute classes.
