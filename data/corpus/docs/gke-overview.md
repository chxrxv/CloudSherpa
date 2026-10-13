---
doc_id: gke-overview
title: GKE overview
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview
category: compute
fetched_at: '2026-10-13T15:13:49+00:00'
license: CC BY 4.0 (Google Cloud documentation)
---

Autopilot

Standard

This page provides an overview of Google Kubernetes Engine (GKE). GKE
is a managed implementation of the Kubernetes open
source container orchestration platform. Kubernetes was developed by Google,
drawing on years of experience operating production workloads at scale on
Borg, Google's in-house cluster
management system. With GKE, you can deploy and operate your own
containerized applications at scale using
Google Cloud's infrastructure.

This page is for Operators and Developers who are
looking for a scalable, automated, managed Kubernetes solution. To learn more about
common roles, see
Common GKE user roles and tasks.

## Get started with GKE

You can start exploring GKE in minutes.
You can use GKE's
free tier,
which lets you get started with Kubernetes without incurring costs for cluster
management.

1. Get started in Google Cloud console
2. Try the quickstart to deploy a
   containerized web application.
3. Read the
   Autopilot overview,
   which has guidance and resources for planning and operating your platform.

## When to use GKE

GKE is ideal if you need a platform that lets you configure the
infrastructure that runs your containerized apps, such as networking, scaling,
hardware, and security. GKE provides the operational power of
Kubernetes while managing many of the underlying components, such as the
control plane and nodes, for you.

### Benefits of GKE

The following table describes some of the benefits of using GKE
as your managed Kubernetes platform:

| GKE benefits | |
| --- | --- |
| Platform management | - Fully-managed nodes in GKE   Autopilot mode   with built-in hardening and best practice configurations automatically   applied. - Managed upgrade experience with   release channels   to improve security, reliability, and compliance. - Flexible   maintenance windows and exclusions   that let you configure upgrade type and scope   to meet business needs and architecture constraints. - In GKE Standard mode, flexible   node upgrade strategies   to optimize availability and manage disruptions. - Automatic scaling of nodes based on the number of Pods in the   cluster with Autopilot mode or with node auto-provisioning   in Standard mode. - Node auto-repair   to maintain node health and availability. - Fleet-based team management. - Connect gateway. - Manage GKE cluster configuration with Config Sync. - Built-in logging and monitoring. - Google Cloud integrated CI/CD options with   Cloud Build and Cloud Deploy. |
| Improved security posture | - Hardened node operating system for apps: Container-Optimized OS. - Built-in security measures. - Policy Controller. - Automatic upgrades   to new GKE versions. - Integrated security posture monitoring tooling with the   security posture dashboard. - Google Cloud logging and monitoring integrations with   Google Cloud Observability. |
| Cost optimization | - In Autopilot mode, pay only for the compute resources   your running Pods request.  In GKE Standard mode, you pay for all   resources on nodes, regardless of Pod requests. - Save costs by running fault-tolerant workloads, such as batch jobs, on   Spot Pods. - Minimized operational overhead in Autopilot mode because   Google Cloud manages both the   nodes and the control plane. |
| Reliability and availability | - >99% monthly   uptime SLO. - Pod-level SLA in Autopilot clusters because Google manages   the nodes. - Highly-available control plane and worker nodes in   Autopilot mode   and in   regional Standard clusters. - Proactive monitoring and recommendations   to mitigate potential workload disruptions caused by upcoming   deprecations. - Multi-cluster Service capabilities. |

**Best practice**:

Configure the application CI/CD pipeline to use Cloud Build,
Cloud Deploy, and Artifact Registry.
By using managed build and deployment services,
you can optimize for security, scale, and simplicity.

### Use cases for GKE

GKE and Kubernetes are used in a variety of industries, including
robotics, healthcare, retail, education, gaming, and financial services. Examples of workloads you can run include:

- AI and ML operations
- Data processing at scale
- Scalable online games platforms
- Reliable applications under heavy load

For case studies by industry and application, refer to
Google Cloud customers.

## How GKE works

A GKE environment consists of *nodes*, which are Compute Engine
virtual machines (VMs), that are grouped together to form a *cluster*. You
package your apps (also called *workloads*) into containers. You deploy sets
of containers as *Pods* to your nodes. You use the Kubernetes API to interact
with your workloads, including administering, scaling, and monitoring.

Kubernetes clusters have a set of management nodes called the *control plane*,
which run system components such as the Kubernetes API server. In
GKE, Google Cloud manages the
control plane and system components for you. In Autopilot mode, which
is the recommended way to run GKE,
Google Cloud also manages your worker nodes.
Google Cloud automatically upgrades
component versions for improved stability and security, which helps ensure high availability and the integrity of data stored in the cluster's
persistent storage.

For more information, refer to
GKE cluster architecture.

**Best practice**:

If you run your workloads in VMs, consider using
Migrate for GKE to
containerize the workloads without having to rewrite apps or modify source code.

### Kubernetes versions and features

GKE automatically upgrades the control plane and worker nodes of clusters to new Kubernetes versions so that the clusters receives new features, bug fixes, and security patches. GKE provides various capabilities to manage these upgrades to minimize disruption to your workloads while keeping them performant, reliable, and secure.

For more information, see About GKE cluster upgrades.

**Best practice**:

To try less stable Kubernetes features in the *alpha* and *beta*
stages or to test upcoming Kubernetes minor versions, use
alpha clusters.
You can also selectively use Kubernetes beta APIs with GKE clusters.
Before you enable beta APIs in production clusters, review the
implications.

### Modes of operation

GKE has the Autopilot and Standard *modes of
operation*, which offer you different levels of flexibility, responsibility, and
control. If you want more information before you choose a mode, refer to
Choose a GKE mode of operation.

**Best practice**:

Use the fully
managed Autopilot
mode, in which Google Cloud manages your
nodes for you and provides a workload-focused, cost-optimized, production-ready
experience. Only use Standard mode if you know you have a specific need
to manually manage the node pools and clusters.

## What's next

- Start learning about GKE.
- Learn how to deploy a containerized application in GKE.
- Learn more about types of clusters.
- Learn more about Kubernetes.
- Explore the GKE documentation.
- Design and optimize GKE clusters with Compute Advisor.
