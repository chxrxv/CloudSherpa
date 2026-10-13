---
doc_id: pubsub-overview
title: What is Pub/Sub?
url: https://docs.cloud.google.com/pubsub/docs/overview
category: analytics
fetched_at: '2026-10-13T15:13:49+00:00'
license: CC BY 4.0 (Google Cloud documentation)
---

**Key Point:** Understand what Pub/Sub is, why businesses require
Pub/Sub, and the advantages of Pub/Sub compared to similar
technologies. Also, learn about core Pub/Sub concepts that
include the terms topic, publisher, and subscriber.

Pub/Sub is an asynchronous and scalable messaging service that decouples
services producing messages from services processing those messages.

Pub/Sub allows services to communicate asynchronously, with
latencies typically on the order of 100 milliseconds.

Pub/Sub is used for streaming analytics and data integration
pipelines to load and distribute data. It's equally effective as a
messaging-oriented middleware for service integration or as a queue to parallelize tasks.

Pub/Sub lets you create systems of event producers and consumers,
called **publishers** and **subscribers**. Publishers communicate with
subscribers asynchronously by broadcasting events, rather than by
synchronous remote procedure calls (RPCs).

Publishers send events to the Pub/Sub service, without regard to
how or when these events are to be processed. Pub/Sub then
delivers events to all the services that react to them. In systems communicating
through RPCs, publishers must wait for subscribers to receive the data. However,
the asynchronous integration in Pub/Sub increases the flexibility
and robustness of the overall system.

To get started with Pub/Sub, check out the
Quickstart using Google Cloud console.
For a more comprehensive introduction, see
Building a Pub/Sub messaging system.

## Common use cases

- **Ingesting user interaction and server events.** To use user
  interaction events from end-user apps or server events from your system,
  you might forward them to Pub/Sub. You can then use a
  stream processing tool, such as Dataflow, which delivers
  the events to databases. Examples of such databases are
  BigQuery, Bigtable, and Cloud Storage.
  Pub/Sub lets you gather events from many clients
  simultaneously.
- **Real-time event distribution.** Events, raw or processed, may
  be made available to multiple applications across your team and organization
  for real- time processing. Pub/Sub supports an "enterprise
  event bus" and event-driven application design patterns.
  Pub/Sub lets you integrate with many systems that export
  events to Pub/Sub.
- **Replicating data among databases.** Pub/Sub
  is commonly used to distribute change events from databases. These events
  can be used to construct a view of the database state and state history in
  BigQuery and other data storage systems.
- **Parallel processing and workflows.** You can efficiently
  distribute many tasks among multiple workers by using Pub/Sub
  messages to communicate with the workers. Examples of such tasks are
  compressing text files, sending email notifications, evaluating AI models,
  and reformatting images.
- **Enterprise event bus.** You can create an enterprise-wide
  real-time data sharing bus, distributing business events, database updates,
  and analytics events across your organization.
- **Data streaming from applications, services, or IoT devices.**
  For example, a SaaS application can publish a real-time feed of events. Or,
  a residential sensor can stream data to Pub/Sub for use in
  other Google Cloud products through a data-processing pipeline.
- **Refreshing distributed caches.** For example, an application
  can publish invalidation events to update the IDs of objects that have
  changed.
- **Load balancing for reliability.** For example, instances of a
  service may be deployed on Compute Engine in multiple zones but subscribe
  to a common topic. When the service fails in any zone, the others can pick
  up the load automatically.

## Comparing Pub/Sub to other messaging technologies

Pub/Sub combines the horizontal scalability of
Apache Kafka and
Pulsar with
features found in messaging middleware such as Apache ActiveMQ and
RabbitMQ. Examples of such features are dead-letter queues and filtering.

**Note:**
Google Cloud Managed Service for Apache Kafka
is available. If you're considering a migration from Kafka to
Pub/Sub, consult this migration guide.

Another feature that Pub/Sub adopts from messaging middleware is
**per-message parallelism**, rather than partition-based messaging.
Pub/Sub "leases" individual messages to subscriber clients, then
tracks whether a given message is successfully processed.

By contrast, other horizontally scalable messaging systems
use partitions for horizontal scaling. This forces subscribers
to process messages in each partition in order and limits the number of concurrent
clients to the number of partitions. Per-message processing
maximizes the parallelism of subscriber applications, and helps ensure
publisher and subscriber independence.

## Compare Service-to-service and service-to-client communication

Pub/Sub is intended for service-to-service communication rather
than communication with end-user or IoT clients. Other patterns are
better supported by other products:

- **Client-server.** To send messages between a mobile or web app and a service,
  use products that include Firebase Realtime Database and
  Firebase Cloud Messaging.
- **Asynchronous service calls.** Use Cloud Tasks.

You can use a combination of these services to build client -> services -> database
patterns. For example, see the tutorial
Streaming Pub/Sub messages over WebSockets.

## Integrations

Pub/Sub has many integrations with other Google Cloud products to create a fully
featured messaging system:

- **Stream processing and data integration.** Supported by Dataflow, including Dataflow templates and SQL, which allow processing and
  data integration into BigQuery and data lakes on Cloud Storage. Dataflow
  templates for moving data from Pub/Sub to
  Cloud Storage, BigQuery, and other products are available in
  the Pub/Sub and Dataflow UIs in the
  Google Cloud console. Integration with Apache Spark, particularly when managed with Managed Service for Apache Spark is also available. Visual composition of integration and
  processing pipelines running on Spark + Managed Service for Apache Spark can be accomplished with
  Data Fusion.
- **Monitoring, Alerting and Logging.** Supported by Monitoring and
  Logging products.
- **Authentication and IAM.** Pub/Sub relies on a standard OAuth
  authentication used by other Google Cloud products and supports granular IAM,
  enabling access control for individual resources.
- **APIs.** Pub/Sub uses standard gRPC and REST service API
  technologies along with client libraries for several languages.
- **Triggers, notifications, and webhooks.** Pub/Sub offers push-based
  delivery of messages as HTTP POST requests to webhooks. You can implement workflow automation using Cloud Functions
  or other serverless products.
- **Orchestration.** Pub/Sub can be integrated into multistep serverless
  Workflows
  declaratively. Big data and analytic orchestration often done with
  Managed Airflow, which supports Pub/Sub triggers.
  You can also integrate Pub/Sub with
  Application Integration
  (Preview) which is an
  Integration-Platform-as-a-Service (iPaaS) solution. Application Integration provides a
  Pub/Sub trigger
  to trigger or start integrations.
- **Integration Connectors.**(Preview)
  These connectors let you connect to various data sources.
  With connectors, both Google Cloud services and third-party business applications are exposed
  to your integrations through a transparent, standard interface. For Pub/Sub, you can create a Pub/Sub connection
  for use in your integrations.

## Next steps

- Get started with the Pub/Sub
  quickstart.
- Read the basics of the
  Pub/Sub service.
- Learn how to build a
  Pub/Sub messaging system.
- Understand Pub/Sub pricing.
- Understand quotas and limits for
  Pub/Sub.
- Read the Pub/Sub release
  notes.
- Explore data
  engineering with Google Cloud services on Qwiklabs.
