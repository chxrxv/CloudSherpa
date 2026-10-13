---
doc_id: geography-regions
title: Geography and regions
url: https://docs.cloud.google.com/docs/geography-and-regions
category: architecture
fetched_at: '2026-10-13T15:13:49+00:00'
license: CC BY 4.0 (Google Cloud documentation)
---

Google Cloud products are served from specific regional failure domains
and are fully supported by Service Level Agreements to ensure you
are designing your application architecture within the structure of Google Cloud.

Google Cloud infrastructure services are available in locations across
North America, South America, Europe, Asia, the Middle East, and Australia.
These locations are divided into regions and zones. You can choose where
to locate your applications to meet your latency, availability, and durability
requirements.

## Try it for yourself

If you're new to Google Cloud, create an account to evaluate how our
products perform in real-world scenarios. New customers also get $300 in
free credits to run, test, and deploy workloads.

Get started for free

## Regions and zones

*Regions* are independent geographic areas that consist of *zones*. Zones and regions are
logical abstractions of underlying physical resources. A region consists of three or more zones
housed in three or more physical data centers. The regions Stockholm, Osaka, and Montreal
have three zones housed in one or two physical data centers. These regions are in the process of
expanding to at least three physical data centers. When you architect your solutions in
Google Cloud, consider the guidance in
Cloud locations,
Google Cloud Platform SLAs,
and the appropriate
Google Cloud product documentation.

These data centers might be owned by Google and listed on the
Google Cloud locations page,
or they might be leased from third-party data center providers. For the full
list of data center locations for Google Cloud, see our
ISO/IEC 27001 certificate.
Regardless of whether the data center is owned or leased, Google Cloud selects
data centers and designs its infrastructure to provide a uniform level of
performance, security, and reliability.

A *zone* is a deployment area for Google Cloud resources within a region.
Zones should be considered a single failure domain within a region. To
deploy fault-tolerant applications with high availability and help protect
against unexpected failures, deploy your applications across multiple zones
in a region. Google Cloud also offers specialized AI zones that provide
high-capacity GPUs and TPUs for AI and ML workloads. For more information, see
AI zones.

To protect against the loss of an entire region due to
natural disaster, have a disaster recovery plan and know how to bring
up your application in the unlikely event that your primary region is lost. See
application deployment considerations
for more information.

For more information about the specific resources available within each location
option, see our Cloud locations.

Google Cloud's services and resources can be zonal,
regional, or managed by Google across multiple
regions. For more information about what these
options mean for your data, see
geographic management of data.

Google Cloud intends to offer a minimum of three availability zones
(physically and logically distinct zones) in every general-purpose region.

Related location docs

- Compute Engine regions and zones
- Cloud Storage bucket locations
- App Engine locations

### Zonal resources

Zonal resources operate within a single zone. Zonal outages can affect some or
all of the resources in that zone. An example of a zonal resource is a
Compute Engine virtual machine (VM) instance that resides within a
specific zone.

### Regional resources

Regional resources are resources that are redundantly deployed across multiple
zones within a region, for example App Engine applications, or
regional managed instance groups.
This gives them higher availability relative to zonal resources.

### Multi-regional resources

Multiple Google Cloud services are managed by Google to be redundant and
distributed within and across regions. These services optimize availability,
performance, and resource efficiency. As a result, these services require a
trade-off between either latency or the consistency model. These trade-offs are
documented on a product specific basis.

The following services have one or more
multi-regional locations
in addition to any regional locations:

- Artifact Registry
- Assured Workloads
- Backup and DR
- BigQuery
- Cloud EKM
- Firestore
- Cloud Healthcare API
- Cloud HSM
- Cloud KMS
- Natural Language API
- Cloud Storage
- Container Registry
- Document AI
- Gemini Enterprise for Customer Experience
- GKE Enterprise
- Payment Gateway
- Security Command Center
- Sensitive Data Protection
- Spanner
- Speech-to-Text
- Storage Transfer Service

These multi-regional services are designed to be able to function following the
loss of a single region.

For more information, see
Products available by location,
and the documentation for each product.

## Global services

Google Cloud has been designed to operate globally
from the ground up and continually conducts maintenance and upgrades 24/7/365
without inconveniencing you. Our global backbone provides
tremendous flexibility for load-balancing, and reduces end-user latency by
having interconnects close to you. Our global cloud management plane simplifies
managing multi-region developments.

## Internal services

Underpinning and supporting many customer facing Google Cloud services
are a set of proven internal services like Spanner, Colossus, Borg, and
Chubby.

These internal services are either globally load-balanced across multiple
regions, or dedicated to each region in which they are available. Where
services are load-balanced across multiple regions, we deploy updates
progressively region-by-region, allowing us to detect and address problems
without affecting your service usage. None of these internal services are
limited to a single logical data center or to a single region.

Global Internal Services can run in or be replicated in the following cloud
regions:

**Americas**

- southamerica-west1
- us-central1
- us-east1
- us-east4
- us-west1
- us-west4

**Europe**

- europe-north1
- europe-west1
- europe-west4

**Asia**

- asia-east1
- asia-southeast1

## Service dependencies

In general, for Google Cloud services, if a single region fails, only
customers solely in that region are impacted; customers who have multi-region
products are not impacted. Google Cloud has significant architecture
in place with a goal to prevent correlated failures across regions.

All Google Cloud services rely upon core internal tools to provide
fundamental services such as networking (in and out of data centers), access to
data centers, and identity authorization systems. These tools are resilient to
regional outages, with the goal of one region not being impacted if other
regions become unavailable.

Google Cloud provides clear direction on how customers can architect
their applications for the desired level of resilience on our
public website,
especially for commonly-used Google Cloud products such as
Compute Engine, BigQuery, Pub/Sub, and
other services.

Our major dependencies are listed below, starting with dependencies common to
all services, with the proviso that lower level implementation details are
subject to change.

### Common dependencies for all services

- Identity data plane for authentication and authorization
- Internal services that provide logging, metadata storage, and workflow
  management
- Access to Google Cloud APIs depends on DNS, globally-distributed
  load balancers, and points of presence (PoPs).
- The configuration of global resources: For example, IAM
  policies, global firewall rules, global load balancer configurations, and
  Pub/Sub topics are stored in replicated databases.
- When Google Cloud services makes requests to customer-controlled
  endpoints, for example, Cloud EKM fetching customer keys, or
  Pub/Sub delivering messages, those requests depend on our
  global network infrastructure to access those customer-controlled endpoints.

### Services with additional dependencies

- Compute Engine services
  - The Google Cloud VM and Persistent Disk data planes depend on
    lower-level Compute Engine and Cloud Storage services
    such as Borg and Colossus.
- Google Cloud and infrastructure storage services like Spanner,
  Bigtable, and Cloud Storage depend on:
  - Encryption and key management infrastructure for customer
    (Cloud KMS / Cloud EKM) and internal infrastructure for
    Google-owned keys
  - Internal services to provide logging and auditing of data access
  - Internal data replication services, where data is expected to be available
    across multiple regions
  - Explicitly-configured backups and replication to other regions depends
    on cross-region networking
- Messaging services
  - Pub/Sub depends on our global network infrastructure to access
    customer-controlled endpoints
- Networking services
  - Global load balancing, DNS, and failover between regions all depend on
    physical networking infrastructure.
  - Preventing DDos attacks, and the like, depends on lower-level
    Compute Engine infrastructure.
- Managed and hosted services like GKE and Cloud SQL
  - Depend on Compute Engine and either Container Registry or
    Artifact Registry for VM images.
- Self-contained lower-level infrastructure
  - Our internal cluster-level control plane including Borg and network fabrics
  - Cluster-level storage, such as Colossus
  - Encryption and key management infrastructure

## Maintaining and improving availability and resilience

Site Reliability Engineering (SRE) is Google's internal organization dedicated to
working on availability, latency, performance, and capacity. Outages and service
unavailability are correlated to the deployment of new code or changes to the
environment. By using industry best practices, SRE balances the need to release
new software and keeps the environment secure with the understanding that those
necessary changes might cause downtime.

## Partnering with customers to build resilient services

If you have mission-critical needs and need to architect for resilience and
disaster recovery, our SRE/CRE and PSO teams
can work with you to architect your applications to bridge multiple regions and
zones and can further assist you with designing High Availability (HA) systems.

If you have heightened availability requirements around specific dates,
such as Black Friday and Cyber Monday, Google Cloud has a program to
partner with you to check and validate your specific application running on
Google Cloud and identify any unexpected service dependencies between your
application and our services.

## Points of presence (POPs)

Google operates a global network of peering points of presence, which means that
customer traffic can travel within the Google network until it's close to its
destination, providing users with a better experience and better security. For
more information, see
Network edge locations.

## Geographic management of data

Data locality for Google Cloud services are governed by the
terms of service, including
service specific terms. Google understands that each
customer might have unique security and compliance needs. The
Google Cloud sales team can help you work towards meeting
your requirements.

When using regional or zonal storage resources, we strongly recommend that
you replicate data to another region or snapshot it to a multi-regional storage
resource for disaster recovery purposes.

## Application deployment considerations

To build highly available services and applications that can withstand zones becoming unavailable
:   Use the following:

    - Regional resources, such as App Engine
      applications,
      regional managed instance groups,
      or managed multi-regional resources such as
      Cloud Storage, Datastore, Firestore, or Spanner.
    - Zonal resources, such as Compute Engine virtual machines, but manage your
      own compute and storage redundancy across zones or across regions.

To build disaster recovery capable applications that can withstand the extended loss of entire regions
:   For data, use one or more of the following strategies:

    - Use managed, multi-regional storage services such as Cloud Storage,
      Datastore, Firestore, or Spanner.
    - Use zonal or regional resources, but snapshot data to a multi-regional
      resource such as Cloud Storage, Datastore,
      Firestore, or Spanner.
    - Use zonal or regional resources, but manage your own data replication to
      one or more other regions.

    For compute, use the following strategy:

    - Use zonal or regional resources, such as Compute Engine or
      App Engine, but manually or automatically bring up your
      application in another region (on regional failure) referring to copies of
      your primary data if the data is not already in a managed, multi-regional
      resource.

For more information about service dependencies,
contact sales.

#### Zone and region disconnect testing in production

To aim for the highest levels of service continuity, Google Cloud conducts rigorous resilience testing in a dedicated, production-equivalent environment. Unlike standard simulations, this testing uses an internal-only Google Cloud region that is architecturally identical to our customer-facing regions. The region's network connectivity is then physically disconnected to validate precisely how our products behave during a total zonal or regional failure.

The goal is to ensure that while local services within the affected area might go offline as expected, control planes and services that operate in other zones and regions remain unaffected.

Validation occurs on a consistent, periodic schedule, ensuring a repeatable feedback loop. This ongoing validation ensures our global infrastructure remains resilient against large-scale outages.

For guidance on how to implement testing for your services running on Google Cloud, refer to our documentation on Fault Injection Testing and how to Simulate failure scenarios.

## Additional solutions and tutorials

The following solutions and tutorials provide guidance for ensuring your
application is highly available and can withstand outages:

#### Patterns for scalable and resilient apps

Learn how to use Google Cloud to build scalable and resilient
application architectures using patterns and practices that apply broadly
to any web application.

#### Creating an HTTPS load balancer

Configure Compute Engine instances in different regions and use HTTP
load balancing to distribute traffic across the regions to increase
availability across regions and provide failover in the case of a service
outage.

#### Designing robust systems

Design your application on the Compute Engine
service to be robust against failures, network interruptions, and
unexpected disasters.

#### Cassandra Backup and Restore with Cloud Storage

Learn how to add basic disaster recovery to your Cassandra installation
by backing up your data into, and restoring your data from,
Cloud Storage.

#### Disaster recovery planning guide

General principles for designing and testing a disaster
recovery plan with Google Cloud.
