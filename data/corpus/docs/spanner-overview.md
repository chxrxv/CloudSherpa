---
doc_id: spanner-overview
title: 'Spanner: Always-on, virtually unlimited scale database'
url: https://cloud.google.com/spanner
category: database
fetched_at: '2026-10-13T15:13:49+00:00'
license: CC BY 4.0 (Google Cloud documentation)
---

Deliver deep context for agentic AI with Spanner multi-model capabilities. Register for the upcoming webinar.

# Spanner

## Always-on database with virtually unlimited scale

Build intelligent, mission-critical apps on a single database that unifies relational, graph, key-value, and search. Run anywhere with Spanner Omni.

Get started with a 90 day free trial instance.

### Product highlights

- Start small and scale without limits or re-architecture
- Built-in graph processing, full-text search and vector search
- Develop apps with the familiar PostgreSQL interface on Spanner

---

- What is Spanner?

  5-minute video explainer

Features

### Multi-model: One database, many possibilities

Spanner's multi-model capabilities empower you to build intelligent, AI-enabled applications on top of your operational relational and NoSQL data by leveraging native integration with Gemini Enterprise Agent Platform, Spanner Graph for querying complex relationships, vector search for semantic search, built-in full-text search, —all with "true ZeroETL" interoperability. This unified approach eliminates data silos, saves costs, reduces operational and security touchpoints, and ensures data consistency across all models.

Enterprise-scale AI, search, graph, and analytics

43:41

### Foundation for agentic AI applications

Seamlessly integrate with Gemini Enterprise Agent Platform to harness the latest Gemini models. Maximize AI developer productivity to build autonomous agents that reason over real-time operational state using Agent Development Kit (ADK). Have natural language conversations with your data in Spanner with vibe coding platforms such as Gemini CLI using remote MCP servers. Leverage AI functions in Spanner allowing you to perform complex semantic operations directly in SQL bringing intelligence closer to your data. Chat with agents about your database data using natural language with conversational analytics for Spanner. The Data Agent Kit streamlines your workflows by bundling secure Model Context Protocol (MCP) tools, native IDE plugins, and pre-codified data engineering, data science, and data app developer skills into a single, open-source package.

How Palo Alto Networks Is Securing AI at Scale with Spanner

3:09

### Run anywhere

Spanner Omni is a downloadable version of Spanner, Google Cloud’s globally distributed, multi-model database. It extends Spanner's industry-leading scale, high availability, and strong global consistency to your infrastructure— on-premises, across clouds, or on your laptop. Spanner Omni is the ideal solution where you need cross-cloud resilience or a scale-out database that operates outside Google Cloud to power your agentic AI applications.

To infinity & beyond: Spanner Omni for deployments beyond Google Cloud

40:03

### Real-time insights at the speed of business

Break down the silos between operational and analytical data. Spanner’s built-in columnar engine allows you to perform high-performance, ad hoc analytics on live data without impacting transactional throughput. For deeper analysis, Spanner integrates seamlessly with data lakehouses like BigQuery leveraging federated queries to analyze data across Spanner and BigQuery in real-time, or utilizing one-click reverse ETL to flow insights from your lakehouse back into Spanner.

What is Spanner Data Boost?

5:52

### Effortless scalability

Dream big, start small, and scale effortlessly as your needs grow. Spanner seamlessly handles growing datasets and demanding workloads with its horizontal read and "write" scalability. Automatic database sharding ensures optimal data distribution, while geo-partitioning brings data closer to your users for lower latency. Experience consistently high performance with workload-isolated query processing with Spanner Data Boost, even during peak demand.

VIDEO

How Spanner Transactions Work at Planet Scale

8:17

### Always On availability

Ensure your applications are always on, ready to serve your users. Spanner delivers up to 99.999% availability with automated maintenance and flexible deployment options. Choose from single-region, dual-region, or multi-region configurations to match your specific availability and fault-tolerance requirements.

VIDEO

How Cloud Spanner delivers high availability at scale

6:43

### Guaranteed consistent transactions

Say goodbye to data inconsistencies and the complexities of managing them. Spanner guarantees strong transactional consistency, meaning every read reflects the most recent updates, regardless of the size or distribution of your data. Build with confidence, knowing your applications always have a consistent view of your data.

VIDEO

Strong consistency at scale with Spanner

7:20

### Trusted security and compliance

Trust your data to a secure and compliant platform with Spanner. Enjoy centralized administration and control with Database Center, simplifying your cloud database management. Spanner offers enterprise-grade security and controls, including data encryption at rest and in transit, granular access management through Identity and Access Management (IAM), and compliance with industry standards. Protect your data further with robust backup and restore capabilities, including point-in-time recovery for operational peace of mind.

Database comparison

| Database attribute | Other Relational DB | Other Non-relational DB | Spanner |
| --- | --- | --- | --- |
| **Schema** | Static | Dynamic | Dynamic |
| **SQL** | Yes | No | Yes  (PostgreSQL, Google SQL) |
| **Transactions** | ACID  (atomicity, consistency, isolation, durability) | Eventual | Strong-ACID  with TrueTime ordering |
| **Scalability** | Vertical  (use a bigger machine) | Horizontal  (add more machines) | Horizontal |
| **Availability** | Failover (downtime) | High | High 99.999% SLA |
| **Replication** | Configurable | Configurable | Automatic |

**Gartner®** ranked Spanner #1 for Lightweight Transaction Use Case. Get the full report.

**Schema**

Other Relational DB

Static

Other Non-relational DB

Dynamic

Spanner

Dynamic

**SQL**

Other Relational DB

Yes

Other Non-relational DB

No

Spanner

Yes

(PostgreSQL, Google SQL)

**Transactions**

Other Relational DB

ACID

(atomicity, consistency, isolation, durability)

Other Non-relational DB

Eventual

Spanner

Strong-ACID

with TrueTime ordering

**Scalability**

Other Relational DB

Vertical

(use a bigger machine)

Other Non-relational DB

Horizontal

(add more machines)

Spanner

Horizontal

**Availability**

Other Relational DB

Failover (downtime)

Other Non-relational DB

High

Spanner

High 99.999% SLA

**Replication**

Other Relational DB

Configurable

Other Non-relational DB

Configurable

Spanner

Automatic

**Gartner®** ranked Spanner #1 for Lightweight Transaction Use Case. Get the full report.

How It Works

### Spanner instances provide compute and storage in one or more regions. A distributed clock called TrueTime guarantees transactions are strongly consistent even across regions. Data is automatically "split" for scalability and replicated using a synchronous, Paxos-based scheme for availability.

Common Uses

### Migration and modernization

##### Streamline MySQL and Cassandra modernization

Modernize your sharded MySQL and Cassandra workloads to superpower your development teams and scale for the next phase of growth. Take advantage of open-source Spanner migration tool and a network of qualified services and technology partners that can streamline your migration.

- Discover how Spanner enables live migrations of mission-critical workloads
- MySQL to Spanner migration guide
- Cassandra to Spanner migration guide

#### Tutorials, quickstarts, & labs

##### Streamline MySQL and Cassandra modernization

Modernize your sharded MySQL and Cassandra workloads to superpower your development teams and scale for the next phase of growth. Take advantage of open-source Spanner migration tool and a network of qualified services and technology partners that can streamline your migration.

- Discover how Spanner enables live migrations of mission-critical workloads
- MySQL to Spanner migration guide
- Cassandra to Spanner migration guide

### Hybrid and multicloud resilience

##### Ensure business continuity across diverse environments

Build truly resilient, high-availability architectures that extend beyond the boundaries of a single cloud provider. By deploying Spanner Omni in a secondary cloud or on-premises data center as a "hot/cold" failover site for your primary Spanner managed service in Google Cloud, you create a critical safety net. This "primary/secondary" architecture reduces vulnerability to service disruptions and helps meet strict "stressed exit" regulatory requirements for financial services.

- Download Spanner Omni
- Read the blog to learn more
- Take a deeper dive

#### Tutorials, quickstarts, & labs

##### Ensure business continuity across diverse environments

Build truly resilient, high-availability architectures that extend beyond the boundaries of a single cloud provider. By deploying Spanner Omni in a secondary cloud or on-premises data center as a "hot/cold" failover site for your primary Spanner managed service in Google Cloud, you create a critical safety net. This "primary/secondary" architecture reduces vulnerability to service disruptions and helps meet strict "stressed exit" regulatory requirements for financial services.

- Download Spanner Omni
- Read the blog to learn more
- Take a deeper dive

### User profile and entitlements

##### Manage critical user data securely at any scale

User profile management is a critical function that requires Spanner's scalability, availability, and global consistency. It is the entry point for players across games, platforms, and regions. Similarly financial services companies manage customer information and product offerings using Spanner.

- How Dragon Quest Walk handled millions of players with Spanner
- Build a sample gaming trade post with Spanner
- Read this whitepaper on building multiplayer games with Spanner

#### Tutorials, quickstarts, & labs

##### Manage critical user data securely at any scale

User profile management is a critical function that requires Spanner's scalability, availability, and global consistency. It is the entry point for players across games, platforms, and regions. Similarly financial services companies manage customer information and product offerings using Spanner.

- How Dragon Quest Walk handled millions of players with Spanner
- Build a sample gaming trade post with Spanner
- Read this whitepaper on building multiplayer games with Spanner

### Financial ledger

##### Gain up-to-date, consistent view of global transactions

Unify financial transactions, trades, settlements, and positions across the globe into a consolidated trade ledger built on Spanner that guarantees external consistency and scalability. Consolidation of data helps in quickly adapting to changing market conditions and regulatory requirements. Similarly retail/ecommerce businesses use Spanner for inventory ledger.

- Watch how Goldman Sachs consolidates trade ledgers on Spanner
- Learn how CERC has disrupted the **exchange receivables** market with new Spanner innovations
- Sample code for a financial application on GitHub

#### Tutorials, quickstarts, & labs

##### Gain up-to-date, consistent view of global transactions

Unify financial transactions, trades, settlements, and positions across the globe into a consolidated trade ledger built on Spanner that guarantees external consistency and scalability. Consolidation of data helps in quickly adapting to changing market conditions and regulatory requirements. Similarly retail/ecommerce businesses use Spanner for inventory ledger.

- Watch how Goldman Sachs consolidates trade ledgers on Spanner
- Learn how CERC has disrupted the **exchange receivables** market with new Spanner innovations
- Sample code for a financial application on GitHub

### Online banking

##### Deliver always-on interactivity for digital experiences

Consumers expect access to their critical financial data on their devices outside of regular banking hours. Allow your developers to focus on new experiences rather than operational overhead, such as manual sharding or eventual consistency. Reduce risk and downtime with 99.999% availability and zero maintenance.

- Create an online banking application with Spanner
- Whitepaper: How Spanner is enabling next-generation financial services
- Learn how Minna Bank built a digital-native banking application with Spanner

#### Tutorials, quickstarts, & labs

##### Deliver always-on interactivity for digital experiences

Consumers expect access to their critical financial data on their devices outside of regular banking hours. Allow your developers to focus on new experiences rather than operational overhead, such as manual sharding or eventual consistency. Reduce risk and downtime with 99.999% availability and zero maintenance.

- Create an online banking application with Spanner
- Whitepaper: How Spanner is enabling next-generation financial services
- Learn how Minna Bank built a digital-native banking application with Spanner

### Loyalty programs and promotions

##### Personalize experiences with real-time updates

Track customer participation and preferences in a loyalty program to analyze trends and improve customer satisfaction. Similarly, game companies use Spanner for building personalized leaderboards in games.

- Learn how REWE Group uses Spanner to optimize for speed and performance

#### Tutorials, quickstarts, & labs

##### Personalize experiences with real-time updates

Track customer participation and preferences in a loyalty program to analyze trends and improve customer satisfaction. Similarly, game companies use Spanner for building personalized leaderboards in games.

- Learn how REWE Group uses Spanner to optimize for speed and performance

### Omni-channel inventory management

##### Provide a consistent view across multiple channels and apps

Spanner provides a high-performance, single source of truth for retail inventory and orders across online, in-store, distribution centers, and shipping to match inventory with demand, improving customer experience and profitability. Game companies similarly use Spanner to store in-game inventory data.

- Watch how to build a real-time inventory management system with Spanner
- Check out how Walmart modernized its data management platform with Spanner
- Learn how Mahindra reimagined the selling process and sold 100,000 SUVs in 30 mins

#### Tutorials, quickstarts, & labs

##### Provide a consistent view across multiple channels and apps

Spanner provides a high-performance, single source of truth for retail inventory and orders across online, in-store, distribution centers, and shipping to match inventory with demand, improving customer experience and profitability. Game companies similarly use Spanner to store in-game inventory data.

- Watch how to build a real-time inventory management system with Spanner
- Check out how Walmart modernized its data management platform with Spanner
- Learn how Mahindra reimagined the selling process and sold 100,000 SUVs in 30 mins

### Knowledge graph

##### Reveal hidden relationships and connections in your data

With Spanner Graph, you can develop knowledge graphs that capture the complex connections between entities, represented as nodes, and their relationships, represented as edges. These connections provide rich context, making knowledge graphs invaluable for developing knowledge base systems and recommendation engines. With integrated search capabilities, you can seamlessly blend semantic understanding, keyword-based retrieval, and graph for comprehensive results.

- Get started with Spanner Graph
- Watch the latest capabilities in Spanner Graph

#### Tutorials, quickstarts, & labs

##### Reveal hidden relationships and connections in your data

With Spanner Graph, you can develop knowledge graphs that capture the complex connections between entities, represented as nodes, and their relationships, represented as edges. These connections provide rich context, making knowledge graphs invaluable for developing knowledge base systems and recommendation engines. With integrated search capabilities, you can seamlessly blend semantic understanding, keyword-based retrieval, and graph for comprehensive results.

- Get started with Spanner Graph
- Watch the latest capabilities in Spanner Graph

Generate a solution

What problem are you trying to solve?

What you'll get:

Step-by-step guide

Reference architecture

Available pre-built solutions

This service was built with Gemini. You must be 18 or older to use it. Do not enter sensitive, confidential, or personal info.

Pricing

| How Spanner pricing works | Spanner pricing is based on compute capacity, Spanner Data Boost, database storage, backup storage, replication, and network usage. Compute pricing varies depending on the edition and configuration selected. Committed use discounts can further reduce the compute price. | |
| --- | --- | --- |
| Service | Description | Price (USD) |
| Compute | **Standard edition**  Packed with a comprehensive suite of established capabilities for regional (single-region) configurations  Compute capacity is provisioned as processing units or nodes (1 node = 1000 processing units). | Starting at  $0.030  per 100 processing units per hour per replica |
| **Enterprise edition**  Provide additional multi-model and advanced search capabilities with enhanced operational simplicity and efficiency  Compute capacity is provisioned as processing units or nodes (1 node = 1000 processing units). | Starting at  $0.041  per 100 processing units per hour per replica |
| **Enterprise Plus edition**  Support the most demanding workloads with the highest levels of availability, performance, compliance, and governance  Compute capacity is provisioned as processing units or nodes (1 node = 1000 processing units). | Starting at  $0.057  per 100 processing units per hour per replica |
| **Data Boost** | On-demand, isolated compute resources, including CPU, memory, and local data transfer | Starting at  $0.00117  per serverless processing unit per hour |
| **Database storage﻿** | Price is based on the amount of data stored in the database and includes the cost of storage in read-write replicas and read-only replicas; witness replicas are free of charge.  **SSD storage**  Use SSD storage when you require low latency and high throughput for your operational data. | Starting at  $0.10  per GB per month per replica for SSD |
| **HDD storage**  Use HDD storage for data that needs to be accessed less frequently and can tolerate higher read latencies and lower throughput. You can also configure tiering policies to move data from SSD to HDD after expiration of a specified time window. | Starting at  $0.02  per GB per month per replica for HDD |
| **Backup storage** | **Regional configuration**  Pricing is based on the amount of backup storage and includes the cost of storage in all replicas. | Starting at  $0.10  per GB per month (incl. all replicas) |
| **Dual-region and multi-regional configuration**  Pricing is based on the amount of backup storage and includes the cost of storage in all replicas. | Starting at  $0.30  per GB per month (incl. all replicas) |
| **Replication** | Intra-region replication | Free |
| Inter-region replication | Starting at  $0.04  per GB |
| **Network** | Ingress | Free |
| Intra-region egress | Free |
| Inter-region egress | Starting at  $0.01  per GB |

Learn more about Spanner pricing and committed use discounts.

How Spanner pricing works

Spanner pricing is based on compute capacity, Spanner Data Boost, database storage, backup storage, replication, and network usage. Compute pricing varies depending on the edition and configuration selected. Committed use discounts can further reduce the compute price.

Compute

Description

**Standard edition**

Packed with a comprehensive suite of established capabilities for regional (single-region) configurations

Compute capacity is provisioned as processing units or nodes (1 node = 1000 processing units).

Price (USD)

Starting at

$0.030

per 100 processing units per hour per replica

**Enterprise edition**

Provide additional multi-model and advanced search capabilities with enhanced operational simplicity and efficiency

Compute capacity is provisioned as processing units or nodes (1 node = 1000 processing units).

Description

Starting at

$0.041

per 100 processing units per hour per replica

**Enterprise Plus edition**

Support the most demanding workloads with the highest levels of availability, performance, compliance, and governance

Compute capacity is provisioned as processing units or nodes (1 node = 1000 processing units).

Description

Starting at

$0.057

per 100 processing units per hour per replica

**Data Boost**

Description

On-demand, isolated compute resources, including CPU, memory, and local data transfer

Price (USD)

Starting at

$0.00117

per serverless processing unit per hour

**Database storage﻿**

Description

Price is based on the amount of data stored in the database and includes the cost of storage in read-write replicas and read-only replicas; witness replicas are free of charge.

**SSD storage**

Use SSD storage when you require low latency and high throughput for your operational data.

Price (USD)

Starting at

$0.10

per GB per month per replica for SSD

**HDD storage**

Use HDD storage for data that needs to be accessed less frequently and can tolerate higher read latencies and lower throughput. You can also configure tiering policies to move data from SSD to HDD after expiration of a specified time window.

Description

Starting at

$0.02

per GB per month per replica for HDD

**Backup storage**

Description

**Regional configuration**

Pricing is based on the amount of backup storage and includes the cost of storage in all replicas.

Price (USD)

Starting at

$0.10

per GB per month (incl. all replicas)

**Dual-region and multi-regional configuration**

Pricing is based on the amount of backup storage and includes the cost of storage in all replicas.

Description

Starting at

$0.30

per GB per month (incl. all replicas)

**Replication**

Description

Intra-region replication

Price (USD)

Free

Inter-region replication

Description

Starting at

$0.04

per GB

**Network**

Description

Ingress

Price (USD)

Free

Intra-region egress

Description

Free

Inter-region egress

Description

Starting at

$0.01

per GB

Learn more about Spanner pricing and committed use discounts.

### PRICING CALCULATOR

Estimate your monthly Spanner costs, tailored to your workload.

### CUSTOM QUOTE

Connect with our sales team to get a custom quote for your organization.

### Start your proof of concept

### Create a 90-day Spanner instance for free

### Learn how to use Spanner

### Create and query a database in console

### Get best practices for constructing SQL statements

### Dive into coding with examples

Business Case

Explore how other businesses built innovative apps to deliver great customer experiences, cut costs, and increase ROI with Spanner.

- **﻿Forrester's Total Economic Impact™ study** shows Spanner delivers a 132% ROI, 9-month payback period and multi-million dollar benefits for a representative composite organization. **Download the full study** to learn more.
- **Gartner®** identifies 13 Critical Capabilities for operational databases, and ranks Spanner #1 in the Lightweight Transactions Use Case. Get the **full report**.

---

How does Uber scale to millions of concurrent requests?

Explore how Uber redesigned its fulfillment platform leveraging Spanner.

### Related Content

- How Wayfair is modernizing, one database at a time
- Learn how Gmail migrated billions of users, trillions of emails, and exabytes of data to Spanner
- Dojo is a payments powerhouse, delivering 60% faster transactions with Spanner

Featured benefits and customers

Grow your business with innovative applications that scale limitlessly to meet any demand.

Lower TCO and free your developers from cumbersome operations to dream big and build faster.

Get superior price-performance and pay for what you use, starting at as low as $40 per month.

Partners & Integration

##### Take advantage of partners with Spanner expertise to help you at every step of the journey, from assessments and business case to migrations and building new apps on Spanner.

#### System integrators

Spanner partners help you modernize applications and migrate to the cloud seamlessly. Find your ideal partner or third-party integration in our directory.

Frequently asked questions

### Other resources and support

#### Is Spanner a relational or non-relational database?

Spanner simplifies your data architecture by bringing together relational, key-value, graph, and vector search workloads—all on the same database. It is a highly scalable database that combines unlimited scalability with relational semantics, such as secondary indexes, strong consistency, schemas, and SQL providing 99.999% availability in one easy solution. Hence, it’s suitable for both relational and non-relational workloads.

#### What is Spanner Omni?

Spanner Omni is a downloadable version of Spanner delivering the same core capabilities with the added flexibility for customers to deploy it anywhere. To learn more, visit https://cloud.google.com/products/spanner/omni

#### Does Spanner use SQL?

Spanner provides two ANSI-based SQL dialects over the same rich set of capabilities: GoogleSQL and PostgreSQL. GoogleSQL shares syntax with BigQuery for teams standardizing their data management workflows. The PostgreSQL interface provides familiarity for teams who already know PostgreSQL and portability of schemas and queries to other PostgreSQL environments. For more information about the Spanner PostgreSQL interface, see our documentation.

#### How do I migrate databases to Spanner?

Migrating existing workloads to Spanner ensures a foundation for future growth, without having to compromise on reliability or price-performance. Spanner‘s multi-model interface is used today by innovative organizations across industries with operational workloads coming from relational databases, like MySQL and SQL Server, key-value stores, such as Cassandra or DynamoDB, along with graph, search, and document tools. The specific approach for a migration will depend on requirements around data volume, performance SLOs, and availability. Spanner migration tool provides end-to-end assessment, schema and data migration, and low-downtime cutover for sharded MySQL and Cassandra databases as well as assessment and migration for PostgreSQL. A qualified network of technology and services partners can accelerate migrations from just about any source.

#### What are the key considerations for operating Spanner?

Spanner is a fully managed database so it automatically provides comprehensive infrastructure management features, but there are some application-specific management actions that may be required depending on your workload. You will need to make sure that you have set up proper alerting and monitoring and that you are watching those closely to ensure production is always running smoothly. You need to understand what actions to take when traffic grows organically over time, or if there is peak traffic expected, or how to handle data corruption due to application bugs, and last but not least, how to troubleshoot performance issues and understand what components are responsible for increased latencies.

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
