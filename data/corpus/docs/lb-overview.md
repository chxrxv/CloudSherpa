---
doc_id: lb-overview
title: Cloud Load Balancing overview
url: https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview
category: networking
fetched_at: '2026-10-13T15:13:49+00:00'
license: CC BY 4.0 (Google Cloud documentation)
---

A load balancer distributes user traffic across multiple instances of your
applications. By spreading the load, load balancing reduces the risk that your
applications experience performance issues. Google's Cloud Load Balancing
is built on reliable, high-performing technologies such as Maglev, Andromeda,
Google Front Ends, and Envoy—the same technologies that power Google's own
products.

Cloud Load Balancing offers a comprehensive portfolio of
application and network load balancers. Use our global proxy load balancers to
distribute millions of requests per second among backends in multiple regions
with our Google Front End fleet in over 80 distinct locations
worldwide—all with a single, anycast IP address. Implement strong
jurisdictional control with our regional proxy load balancers, keeping your
backends and proxies in a region of your choice without worrying about TLS/SSL
offload. Use our passthrough load balancers to quickly route multiple protocols
to backends with the high performance of direct server return (DSR).

Cloud Load Balancing overview (click to enlarge).

## Key features of Cloud Load Balancing

Cloud Load Balancing offers the following load balancer features:

- **Single anycast IP address.** With Cloud Load Balancing, a single anycast IP
  address is the frontend for all of your backend instances in regions around
  the world. It provides cross-region load balancing, including automatic
  multi-region failover, which moves traffic to failover backends if your
  primary backends become unhealthy.
  Cloud Load Balancing reacts instantaneously to changes in users, traffic,
  network, backend health, and other related conditions.
- **Seamless autoscaling.** Cloud Load Balancing can scale as your users and
  traffic grow, including easily handling huge, unexpected, and instantaneous
  spikes by diverting traffic to other regions in the world that can take
  traffic. Autoscaling does not require pre-warming: you can scale from zero to
  full traffic in a matter of seconds.

- **Software-defined load balancing.** Cloud Load Balancing is a fully
  distributed, software-defined, managed service for all your traffic. It is not
  an instance-based or device-based solution, so you won't be locked into a
  physical load-balancing infrastructure or face the high availability, scale,
  and management challenges inherent in instance-based load balancers.
- **Layer 4 and Layer 7 load balancing.** Use Layer 4-based load balancing to
  direct traffic based on data from network and transport layer protocols such
  as
  TCP, UDP, ESP, GRE, ICMP, and ICMPv6
  .
  Use Layer 7-based load balancing to add request routing decisions based on
  attributes, such as the HTTP header and the uniform resource identifier.
- **External and internal load balancing.** Defines whether the load balancer
  can be used for external or internal access. You can use an *external* load
  balancer when your clients need to reach your application from the internet.
  You can use an *internal* load balancer when your clients are inside of
  Google Cloud. To learn more, see external versus internal load
  balancing.

- **Global and regional load balancing.** Defines the scope of the load
  balancer. A *global* load balancer supports backends in multiple regions,
  whereas a *regional* load balancer supports backends in a single region. Even
  though the IP address of a regional load balancer is located in one region, a
  regional load balancer is globally accessible. You can distribute your
  backends in single or multiple regions to terminate connections
  close to your users and to meet your high availability requirements. To learn
  more, see global versus regional load balancing.
- **Routing of traffic in Premium Tier and Standard Tier.** The load balancing
  services in Google Cloud come in different flavors depending on the network
  tier you choose, that is, Premium Tier or Standard Tier, with the former being
  more expensive than the latter. The Premium Tier leverages Google's
  high-quality global backbone whereas the Standard Tier uses the public
  internet to route traffic across the network. The network tier you choose
  depends on whether you prioritize cost or performance for your enterprise
  workload. Some load balancing services are only available in Premium Tier and
  not the Standard Tier. To learn more, see Premium versus Standard Network
  Service Tiers.
- **Advanced feature support.** Cloud Load Balancing supports features such
  as IPv6 load balancing, source IP-based traffic
  steering,
  weighted load balancing,
  WebSockets, user-defined request headers, and protocol forwarding for private
  virtual IP addresses (VIPs).

  It also includes the following integrations:

  - Integration with Cloud CDN for cached content delivery.
    Cloud CDN is supported with the global external Application Load Balancer and the
    classic Application Load Balancer.
- Integration with Google Cloud Armor to protect your infrastructure
  from distributed denial-of-service (DDoS) attacks and other targeted
  application attacks. For more information about Cloud Armor
  features that are available for load balancers, see Cloud Armor
  overview.

## Types of Google Cloud load balancers

Cloud Load Balancing offers two types of load balancers:
Application Load Balancers and Network Load Balancers. You'd choose an
Application Load Balancer when you need a Layer 7 load balancer for your
applications with HTTP(S) traffic. You'd choose a Network Load Balancer when you
need a Layer 4 load balancer that supports TLS offloading (with a proxy load
balancer) or you need support for IP protocols such as UDP, ESP, and ICMP
(with a passthrough load balancer).

The following table provides a high-level overview of the different types of
Google Cloud load balancers categorized by the OSI layer on which they operate
and whether they are used for external or internal access.

| lan Cloud Load Balancing | External (Accepts internet traffic) | Internal (Accepts internal Google Cloud traffic) |
| --- | --- | --- |
| **Application Load Balancers**   **HTTPS**  Layer 7 load balancing | - global external - regional external - classic | - cross-region internal - regional internal |
| **Network Load Balancers**   **TCP/SSL/Other**  Layer 4 load balancing |
| Proxy Network Load Balancers | |
| - global external - regional external - classic | - cross-region internal - regional internal |
| Passthrough Network Load Balancers | |
| - global external (Preview) - regional external | - regional internal |

### Application Load Balancers

Application Load Balancers are proxy-based Layer 7 load balancers that enable
you to run and scale your services behind an anycast IP address. The
Application Load Balancer distributes HTTP and HTTPS traffic to backends hosted on
a variety of Google Cloud platforms—such as Compute Engine and
Google Kubernetes Engine (GKE)—as well as external backends outside
Google Cloud.

The following diagram provides a high-level overview of the different types of Application Load Balancers that can be deployed externally or internally depending on
whether your application is internet-facing or internal.

Different types of Application Load Balancers.

**External Application Load Balancers** are implemented as
managed services either on Google Front Ends
(GFEs) or
Envoy proxies. Clients can
connect to these load balancers from anywhere on the internet. Note the
following:

- These load balancers can be deployed in the following modes: global,
  regional, or classic.
- Global external Application Load Balancers support backends in multiple regions.
- Regional external Application Load Balancers support backends in a single region only.
- Classic Application Load Balancers are global in Premium Tier.
  In Standard Tier, they can distribute traffic to backends in a single
  region only.
- Application Load Balancers use the open
  source Envoy proxy to enable advanced traffic management
  capabilities.

**Internal Application Load Balancers** are built on the
Andromeda network virtualization stack and the open source Envoy proxy. This
load balancer provides internal proxy-based load balancing of Layer 7
application data. The load balancer uses an internal IP address that is
accessible only to clients in the same VPC network or clients
connected to your VPC network. Note the following:

- These load balancers can be deployed in the following modes: regional or
  cross-region.
- Regional internal Application Load Balancers support backends only in a single region.
- Cross-region internal Application Load Balancers support backends in
  multiple regions and are always globally accessible. Clients from any
  Google Cloud region can send traffic to the load balancer.

To learn more about Application Load Balancers, see Application Load Balancer overview.

### Network Load Balancers

Network Load Balancers are Layer 4 load balancers that can handle TCP, UDP,
or other IP protocol traffic. These load balancers are available as either proxy
load balancers or passthrough load balancers. You can pick a load balancer
depending on the needs of your application and the type of traffic that it needs
to handle. Choose a proxy Network Load Balancer if you want to configure a reverse proxy
load balancer with support for advanced traffic controls and backends
on-premises and in other cloud environments. Choose a passthrough Network Load Balancer if you
want to preserve the source IP address of the client packets, you prefer direct
server return for responses, or you want to handle a variety of IP protocols
such as
TCP, UDP, ESP, GRE, ICMP, and ICMPv6
.

#### Proxy Network Load Balancers

Proxy Network Load Balancers are Layer 4 reverse proxy load balancers that distribute
TCP traffic to virtual machine (VM) instances in your Google Cloud
VPC network. Traffic is terminated at the load balancing layer
and then forwarded to the closest available backend by using TCP.

The following diagram provides a high-level overview of the different types of
proxy Network Load Balancers that can be deployed externally or internally depending on
whether your application is internet-facing or internal.

Different types of proxy Network Load Balancers.

**External proxy Network Load Balancers** are Layer 4 load
balancers that distribute traffic that comes from the internet to backends in
your Google Cloud VPC network, on-premises, or in other
cloud environments. These load balancers are built on either Google Front
Ends (GFEs) or
Envoy proxies.

These load balancers can be deployed in the following modes: global,
regional, or classic.

- Global external proxy Network Load Balancers support backends in multiple regions.
- Regional external proxy Network Load Balancers support backends in a single region.
- Classic proxy Network Load Balancers are global in Premium Tier.
  In Standard Tier, they can distribute traffic to backends in a single
  region only.

**Internal proxy Network Load Balancers** are
Envoy proxy-based regional Layer 4 load balancers that enable you to run and
scale your TCP service traffic behind an internal IP address that is
accessible only to clients in the same VPC network or clients
connected to your VPC network.

These load balancers can be deployed in one of the following modes: regional
or cross-region.

- Regional internal proxy Network Load Balancers support backends in a single region
  only.
- Cross-region internal proxy Network Load Balancers support backends in
  multiple regions and are always globally accessible. Clients from any
  Google Cloud region can send traffic to the load balancer.

To lean more about proxy Network Load Balancers, see proxy Network Load Balancer overview.

#### Passthrough Network Load Balancers

Passthrough Network Load Balancers are Layer 4 passthrough load balancers. These
load balancers distribute traffic among backends that are in the
same region as the load balancer or in multiple regions.
They are implemented by using Andromeda virtual networking and Google Maglev.

As the name suggests, these load balancers are not proxies. Load-balanced
packets are received by backend VMs with the packet's source and destination IP
addresses, protocol, and, if the protocol is port-based, the source and
destination ports unchanged. Load-balanced connections are terminated at the
backends. Responses from the backend VMs go directly to the clients, not back
through the load balancer. The industry term for this is direct server return
(DSR).

These load balancers, as depicted in the following image,
are deployed in two modes, depending on whether the load balancer
is internet-facing or internal.

Different types of passthrough Network Load Balancers.

- **External passthrough Network Load Balancers**
  are built on high-performance Maglev load balancers.
  Clients can connect to these load balancers from anywhere
  on the internet. The load balancer
  can also receive traffic from Google Cloud VMs with external IP
  addresses or from Google Cloud VMs that have internet access through
  Cloud NAT or instance-based NAT.

  These load balancers can be deployed in one of the following modes:
  global or regional.

  - Global external passthrough Network Load Balancers
    (Preview)
    support backends in multiple regions. Backends for global external passthrough Network Load Balancers
    can only be deployed using a backend service.
    The load balancer provides you with two
    anycast IP addresses, each served by a disjoint and isolated global load
    balancing control and data plane server infrastructure (also known as an
    availability group) to provide high availability.
  - Regional external passthrough Network Load Balancers support backends in a single region only.
    Backends for regional external passthrough Network Load Balancers can be deployed using either a backend
    service or a target
    pool. For new
    deployments, we recommend using backend services.
- **Internal passthrough Network Load Balancers** are built on the
  Andromeda network virtualization stack. An internal passthrough Network Load Balancer lets you
  load balance traffic behind an internal load-balancing IP address that
  is accessible only to systems in the same VPC network or
  systems connected to your VPC network.

To learn more about passthrough Network Load Balancers, see passthrough Network Load Balancer.

## Underlying technologies of Google Cloud load balancers

The following table lists the underlying technology upon which each
Google Cloud load balancer is built.

- Google Front Ends (GFEs)
  are software-defined, distributed systems that are located in Google points of
  presence (PoPs) and perform global load balancing in conjunction with other
  systems and control planes.
- Andromeda
  is Google Cloud's software-defined network virtualization stack.
- Maglev
  is a distributed system for Network Load Balancing.
- Envoy is an open source edge and service proxy,
  designed for cloud-native applications.

| Load balancer | Technology |
| --- | --- |
| Global external Application Load Balancer | Envoy-based Google Front-End (GFE) |
| Classic Application Load Balancer | GFE |
| Regional external Application Load Balancer | Envoy |
| Cross-region internal Application Load Balancer | Envoy |
| Regional internal Application Load Balancer | Envoy |
| Global external proxy Network Load Balancer | Envoy-based GFE |
| Classic proxy Network Load Balancer | GFE |
| Regional external proxy Network Load Balancer | Envoy |
| Regional internal proxy Network Load Balancer | Envoy |
| Cross-region internal proxy Network Load Balancer | Envoy |
| Global external passthrough Network Load Balancer (Preview) | Maglev |
| Regional external passthrough Network Load Balancer | Maglev |
| Internal passthrough Network Load Balancer | Andromeda |

## Choose a load balancer

To determine which Cloud Load Balancing product to use, you must first
determine what traffic type your load balancers must handle. As a general rule,
you'd choose an Application Load Balancer when you need a flexible feature set for
your applications with HTTP(S) traffic. And you'd choose a Network Load Balancer
when you need TLS offloading at scale or support for UDP, or if you need to expose
client IP addresses to your applications.

You can further narrow down your choices depending on your application's
requirements: whether your application is external (internet-facing) or
internal, whether you need backends deployed globally or regionally, and whether
you need Premium or Standard Network Service Tier.

The following diagram shows all of the available deployment modes for
Cloud Load Balancing. For more details, see the Choose a load
balancer guide.

Choose a load balancer (click to enlarge).

1. Global external Application Load Balancers support two modes of operation: global and classic.

2. Global external proxy Network Load Balancers
support two  modes of operation: global
and classic.

3. Passthrough Network Load Balancers preserve client source IP addresses.
Passthrough Network Load Balancers also support additional protocols like UDP, ESP, and
ICMP.

## Summary of types of Google Cloud load balancers

The following table provides details, such as the network service tier on which
each load balancer operates, along with its load balancing scheme.

| Load balancer | Deployment mode | Traffic type | Network service tier | Load-balancing scheme1 |
| --- | --- | --- | --- | --- |
| **Application Load Balancers** | **Global external** | HTTP or HTTPS | Premium Tier | EXTERNAL\_MANAGED |
| **Regional external** | HTTP or HTTPS | Premium or Standard Tier | EXTERNAL\_MANAGED |
| **Classic** | HTTP or HTTPS | Global in Premium Tier  Regional in Standard Tier | EXTERNAL2 |
| **Regional internal**3 | HTTP or HTTPS | Premium Tier | INTERNAL\_MANAGED |
| **Cross-region internal** | HTTP or HTTPS | Premium Tier | INTERNAL\_MANAGED |
| **Proxy Network Load Balancers** | **Global external** | TCP with optional SSL offload | Premium Tier | EXTERNAL\_MANAGED |
| **Regional external** | TCP | Premium or Standard Tier | EXTERNAL\_MANAGED |
| **Classic** | TCP with optional SSL offload | Global in Premium Tier  Regional in Standard Tier | EXTERNAL |
| **Regional internal**3 | TCP without SSL offload | Premium Tier | INTERNAL\_MANAGED |
| **Cross-region internal** | TCP without SSL offload | Premium Tier | INTERNAL\_MANAGED |
| **Passthrough Network Load Balancers** | **Global external** (Preview) | TCP, UDP, ESP, GRE, ICMP, and ICMPv6 | Premium Tier | EXTERNAL\_PASSTHROUGH |
| **Regional external** | TCP, UDP, ESP, GRE, ICMP, and ICMPv6 | Premium or Standard Tier | EXTERNAL |
| **Internal**3  Always regional | TCP, UDP, ICMP, ICMPv6, SCTP, ESP, AH, and GRE | Premium Tier | INTERNAL |

1 The load-balancing scheme is an attribute on the forwarding rule and
the backend service of a
load balancer and indicates whether the load balancer can be used for internal
or external traffic.

The term *managed* in `EXTERNAL_MANAGED`
or `INTERNAL_MANAGED` indicates
that the load balancer is implemented as a managed service either on a Google Front
End (GFE) or on the open source Envoy
proxy. In a load-balancing scheme that is *managed*, requests are
routed either to the GFE or to the Envoy proxy.

2
It is possible to attach `EXTERNAL_MANAGED` backend services to
`EXTERNAL` forwarding rules. However, `EXTERNAL` backend
services cannot be attached to `EXTERNAL_MANAGED` forwarding rules.
To take advantage of new features available
only with the global external Application Load Balancer, we
recommend that you migrate your existing `EXTERNAL` resources to
`EXTERNAL_MANAGED` by using the migration process described at
Migrate
resources from classic to global external Application Load Balancer.

3 By default, regional internal load balancers only allow traffic
from clients in the same region as the load balancer. However, you can allow
traffic from clients in other regions by enabling *global access* on the
forwarding rule.

## Interfaces

You can configure and update your load balancers by using the
following interfaces:

- The **Google Cloud CLI**: A command-line tool included in the
  Google Cloud CLI; the documentation calls
  on this tool frequently to accomplish tasks. For a complete overview of
  the tool, see the gcloud CLI guide. You can
  find commands related to load balancing in the
  `gcloud compute` command group.

  You can also get detailed help for any `gcloud` command by using the
  `--help` flag.

  ```
  gcloud compute http-health-checks create --help
  ```
- The **Google Cloud console**: Load-balancing tasks can be accomplished
  by using the
  Google Cloud console.
- The **REST API**: All load-balancing tasks can be accomplished by using the
  Cloud Load Balancing API. The
  API reference docs describe the
  resources and methods available to you.
- **Terraform**: You can provision, update, and delete the Google Cloud
  load-balancing infrastructure by using an open source infrastructure-as-code
  tool such as
  Terraform.

## What's next

- To help you determine which Google Cloud load balancer best meets your
  needs, see Choose a load balancer.
- To understand the components of different types of Google Cloud load
  balancers, see
  Cloud Load Balancing resource model.
- To see a comparative overview of the load-balancing features offered by
  Cloud Load Balancing, see Load balancer feature
  comparison.
- To use prebuilt Terraform templates to streamline the setup and management of Google Cloud's networking infrastructure, explore the Simplified Cloud Networking Configuration Solutions GitHub repository.
