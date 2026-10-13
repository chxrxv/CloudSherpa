---
doc_id: waf-performance
title: 'Well-Architected Framework: Performance optimization pillar'
url: https://docs.cloud.google.com/architecture/framework/performance-optimization
category: architecture
fetched_at: '2026-10-13T15:13:49+00:00'
license: CC BY 4.0 (Google Cloud documentation)
---

Last reviewed 2024-12-06 UTC

To view the content in the performance optimization pillar on a single page or to
to get a PDF output of the content, see
View on one page.

This pillar in the
Google Cloud Well-Architected Framework
provides recommendations to optimize the performance of workloads in
Google Cloud.

This document is intended for architects, developers, and administrators who
plan, design, deploy, and manage workloads in Google Cloud.

The recommendations in this pillar can help your organization to operate
efficiently, improve customer satisfaction, increase revenue, and reduce cost.
For example, when the backend processing time of an application decreases, users
experience faster response times, which can lead to higher user retention and
more revenue.

The performance optimization process can involve a trade-off between
performance and cost. However, optimizing performance can sometimes help you
reduce costs. ​​For example, when the load increases, autoscaling can help to
provide predictable performance by ensuring that the system resources aren't
overloaded. Autoscaling also helps you to reduce costs by removing unused
resources during periods of low load.

Performance optimization is a continuous process, not a one-time activity. The
following diagram shows the stages in the performance optimization process:

The performance optimization process is an ongoing cycle that includes the
following stages:

1. **Define requirements**: Define granular performance requirements for
   each layer of the application stack before you design and develop your
   applications. To plan
   resource allocation, consider the key workload characteristics and performance
   expectations.
2. **Design and deploy**: Use elastic and scalable design patterns that can
   help you meet your performance requirements.
3. **Monitor and analyze**: Monitor performance continually by using logs,
   tracing, metrics, and alerts.
4. **Optimize**: Consider potential redesigns as your applications evolve.
   Rightsize cloud resources and use new features to meet changing performance
   requirements.

   As shown in the preceding diagram, continue the cycle of monitoring,
   re-assessing requirements, and adjusting the cloud resources.

For performance optimization principles and recommendations that are specific to AI and ML workloads, see
AI and ML perspective: Performance optimization
in the Well-Architected Framework.

## Core principles

The recommendations in the performance optimization pillar of the Well-Architected Framework
are mapped to the following core principles:

- Plan resource allocation
- Take advantage of elasticity
- Promote modular design
- Continuously monitor and improve performance

## Contributors

Authors:

- Daniel Lees | Cloud Security Architect
- Gary Harmson | Principal Architect
- Luis Urena | Developer Relations Engineer
- Zach Seils | Networking Specialist

Other contributors:

- Filipe Gracio, PhD | Customer Engineer, AI/ML Specialist
- Jose Andrade | Customer Engineer, SRE Specialist
- Kumar Dhanagopal | Cross-Product Solution Developer
- Marwan Al Shawi | Partner Customer Engineer
- Nicolas Pintaux | Customer Engineer, Application Modernization Specialist
- Ryan Cox | Principal Architect
- Radhika Kanakam | Program Lead, Google Cloud Well-Architected Framework
- Samantha He | Technical Writer
- Wade Holmes | Global Solutions Director
