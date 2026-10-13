---
doc_id: bigtable-overview
title: Bigtable overview
url: https://docs.cloud.google.com/bigtable/docs/overview
category: database
fetched_at: '2026-10-13T15:13:49+00:00'
license: CC BY 4.0 (Google Cloud documentation)
---

# Bigtable overview

Bigtable is a sparsely populated table that can scale to billions of
rows and thousands of columns, enabling you to store terabytes or even petabytes
of data. Bigtable is ideal for storing large amounts of single-keyed
data with low latency. It supports high read and write throughput at low
latency, and it's an ideal data source for MapReduce operations.

Bigtable is exposed to applications through multiple client
libraries, including a supported extension to the Apache HBase library for
Java. As a result, it integrates with the existing Apache ecosystem of
open source big data software.

Bigtable's powerful backend servers offer several key advantages:

- **Incredible scalability.** Bigtable scales in direct
  proportion to the number of machines in your cluster. A self-managed HBase
  installation has a design bottleneck that limits the performance after a
  certain threshold is reached. Bigtable does not have this
  bottleneck, so you can scale your cluster up to handle more reads and
  writes.
- **Simple administration.** Bigtable handles upgrades and
  restarts transparently, and it automatically maintains high data
  durability. To replicate your data, add a second
  cluster to your instance, and replication starts automatically. No more
  managing replicas or regions; just design your table schemas, and
  Bigtable will handle the rest for you.
- **Cluster resizing without downtime.** You can increase the size of a
  Bigtable cluster for a few hours to handle a large load, then
  reduce the size of the cluster again—all without any downtime. After you change
  a cluster's size, it typically takes just a few minutes under load for
  Bigtable to balance performance across all of the nodes in
  your cluster.
- **Tiered storage (Preview).** You can
  store infrequently accessed data in a separate, lower-cost storage tier.
  Tiered storage lets you choose the storage tier that best suits your
  Bigtable data access needs.
- **Autoscaling.** You can configure Bigtable to continuously
  monitor cluster CPU capacity and automatically adjust the number of nodes in
  a cluster when necessary.
- **Free trial.** You can explore Bigtable features and
  capabilities at no cost for 10 days, with an option to extend the
  free trial to 90 days. Bigtable provides a
  free trial Bigtable instance
  with up to 500 GB of SSD storage and a 1-node cluster, allowing you to test
  your application's performance by running high-volume read and write
  operations against your Bigtable tables to see how
  Bigtable handles operations with
  SSD-backed performance.
- **In-memory tier (Preview).** You can achieve sub-millisecond
  read latency and high throughput for your critical, time-sensitive data.
  The in-memory tier extends Bigtable's existing persistent
  solid-state drive (SSD) and cost-effective tiered storage with the in-memory
  tier storage (RAM) to provide integrated data tiering within a unified
  service.

## Bigtable editions

Bigtable editions is a pricing model that provides different
capabilities at different price points. You can choose between the standard
Enterprise and the premium Enterprise Plus edition. For more information, see
Editions overview.

## What it's good for

Bigtable is ideal for applications that need high throughput and
scalability for key-value data, where each value is typically no larger than 10
MB. Bigtable also excels as a storage engine for batch MapReduce
operations, stream processing/analytics, and machine-learning applications.

You can use Bigtable to store and query all of the following types
of data:

- **Time-series data,** such as CPU and memory usage over time for multiple
  servers.
- **Marketing data,** such as purchase histories and customer preferences.
- **Financial data,** such as transaction histories, stock prices, and
  currency exchange rates.
- **Internet of Things data,** such as usage reports from energy meters and
  home appliances.
- **Graph data,** such as information about how users are connected to one
  another.

## Bigtable storage model

Bigtable stores data in massively scalable tables, each of which
is a sorted key-value map. The table is composed of *rows*, each of which
typically describes a single entity, and *columns*, which contain individual
values for each row. A single value in each row is indexed. This value is known
as the *row key*. Columns that are related to one another are typically grouped
into a *column family*. Each column is identified by a combination of the column
family and a *column qualifier*, which is a unique name within the column family.

Each intersection of a row and column can contain multiple *cells*. Each cell
contains a unique timestamped version of the data for that row and column.
Storing multiple cells in a column provides a record of how the stored data for
that row and column has changed over time. Bigtable tables are
sparse; if a column is not used in a particular row, it does not take up any
space.

A few things to notice in this illustration:

- Columns can be unused in a row.
- Each cell in a given row and column has a unique timestamp (t).

## Bigtable architecture

The following diagram shows a simplified version of Bigtable's
overall resource architecture:

As the diagram illustrates, all client requests go through a frontend server
before they are sent to a Bigtable node. (In the original
Bigtable paper, these nodes are called "tablet servers.") The
nodes are organized into a Bigtable cluster, which belongs to a
Bigtable instance, a container for the cluster.

**Note:** The diagram shows an instance with a single cluster. You can also add
clusters to replicate your data, which improves data availability
and durability.

Each node in the cluster handles a subset of the requests to the cluster. By
adding nodes to a cluster, you can increase the number of simultaneous requests
that the cluster can handle. Adding nodes also increases the maximum throughput
for the cluster. If you enable replication by adding additional clusters, you
can also send different types of traffic to different clusters. Then if one
cluster becomes unavailable, you can fail over to another cluster.

A Bigtable table is sharded into blocks of contiguous rows, called
*tablets*, to help balance the workload of queries. (Tablets are similar to
HBase regions.) Tablets are stored on Colossus, a Google-developed file system,
in SSTable format. An SSTable provides a persistent, ordered immutable map from
keys to values, where both keys and values are arbitrary byte strings. Each
tablet is associated with a specific Bigtable node. In addition to
the SSTable files, all writes are stored in Colossus's shared log as soon as
they are acknowledged by Bigtable, providing increased durability.

Importantly, data is never stored in Bigtable nodes themselves;
each node has pointers to a set of tablets that are stored on Colossus. As a
result:

- Rebalancing tablets from one node to another happens quickly, because the
  actual data is not copied. Bigtable updates the
  pointers for each node.
- Recovery from the failure of a Bigtable node is fast, because
  only metadata must be migrated to the replacement node.
- When a Bigtable node fails, no data is lost.

While the introduction of the in-memory tier (Preview) and tiered
storage (Preview) add complexity to the physical storage model, the
fundamental resource architecture of instances, clusters, and nodes remains the
same. This hybrid storage architecture lets Bigtable use a
consistent storage model across all tiers, enabling you to access your data
through the same semantic interface regardless of whether it physically resides
in RAM, SSD, or lower-cost storage.

For more information about how to work with these fundamental building blocks,
see Instances, clusters, and nodes.
For details on interacting with your data across these tiers, see
Accessing data.

## Load balancing

Each Bigtable zone is managed by a primary process, which balances
workload and data volume within clusters. This process splits busier or larger
tablets in half and merges less-accessed/smaller tablets together,
redistributing them between nodes as needed. If a certain tablet gets a spike of
traffic, Bigtable splits the tablet in two, then moves one of the
new tablets to another node. Bigtable manages the splitting,
merging, and rebalancing automatically, saving you the effort of manually
administering your tablets. Understand performance provides more
details about this process.

To get the best write performance from Bigtable, it's important to
distribute writes as evenly as possible across nodes. One way to achieve this
goal is by using row keys that don't follow a predictable order. For example,
usernames tend to be distributed more or less evenly throughout the alphabet, so
including a username at the start of the row key will tend to distribute writes
evenly.

At the same time, it's useful to group related rows so they are next to one
another, which makes it much more efficient to read several rows at the same
time. For example, if you're storing different types of weather data over time,
your row key might be the location where the data was collected, followed by a
timestamp (for example, `WashingtonDC#201803061617`). This type of row key would
group all of the data from one location into a contiguous range of rows. For
other locations, the row would start with a different identifier; with many
locations collecting data at the same rate, writes would still be spread evenly
across tablets.

See Choosing a row key for more details about choosing an appropriate
row key for your data.

## Compute

Bigtable provides different compute options depending on your
workload requirements. By default, Bigtable uses cluster
nodes for both storage and
compute.

For high-throughput read jobs, you can use Data Boost for
Bigtable for compute. Data Boost lets you send large read jobs
and queries using serverless compute while your core application continues using
cluster nodes for compute. Enterprise Plus extends the capabilities of these
jobs to include SQL support, as well as access to HDD and tiered storage data.
For more information, see Bigtable Data Boost
overview.

For specialized workloads that require high-throughput, sub-millisecond
point-read latency you can enable the in-memory tier for your
Bigtable nodes.

## Supported data types

Bigtable treats all data as raw byte strings for most purposes.
The only time Bigtable tries to determine the type is for
increment operations, where the target must be a 64-bit integer encoded as an
8-byte big-endian value.

## Memory and disk usage

The following sections describe how several components of Bigtable
affect memory and disk usage for your instance.

### Unused columns

Columns that are not used in a Bigtable row don't take up any
space in that row. Each row is essentially a collection of key-value entries,
where the key is a combination of the column family, column qualifier and
timestamp. If a row does not include a value for a specific column, the
key-value entry is not present.

### Column qualifiers

Column qualifiers take up space in a row, since each column qualifier used in a
row is stored in that row. As a result, it's often efficient to use column
qualifiers as data.

For more information about column qualifiers, see Columns.

### Compactions

Bigtable periodically rewrites your tables to remove deleted
entries, to reorganize your data so that reads and writes are more efficient,
and to move data as part of tiered storage. This process is known as a
*compaction*. There are no configuration settings for compactions—
Bigtable compacts your data automatically. **On average, it takes
a week for a compaction to complete and execute tasks such as data deletion or
moving data to tiered storage.**

Compaction carries out deletions identified by the garbage collection process.
For more information, see Garbage collection. For more
information on compactions in tiered storage, see
How tiered storage works.

### Mutations and deletions

*Mutations*, or changes, to a row take up extra storage space, because
Bigtable stores mutations sequentially and compacts them only
periodically. When Bigtable compacts a table, it removes values
that are no longer needed. If you update the value in a cell, both the original
value and the new value will be stored on disk for some amount of time until the
data is compacted.

Deletions also take up extra storage space, at least in the short term, because
deletions are actually a specialized type of mutation. Until the table is
compacted, a deletion uses extra storage rather than freeing up space.

### Data compression

Bigtable compresses your data automatically using an intelligent
algorithm. You cannot configure compression settings for your table. However, it
is useful to know how to store data so that it can be compressed efficiently:

- **Random data cannot be compressed as efficiently as patterned data.**
  Patterned data includes text, such as the page you're reading right now.
- **Compression works best if identical values are near each other,** either
  in the same row or in adjoining rows. If you arrange your row keys so that
  rows with identical chunks of data are next to each other, the data can be
  compressed efficiently.
- **Bigtable compresses values that are up to 1 MiB in size.**
  If you store values that are larger than 1 MiB, compress them before
  writing them to Bigtable, so you can save CPU cycles, server
  memory, and network bandwidth.

## Data durability

When you use Bigtable, your data is stored on Colossus, a
Google-developed, highly durable file system, using storage devices in
Google Cloud's data centers. You don't need to run an HDFS cluster or any other
file system to use Bigtable. Behind the scenes, Colossus uses
proprietary storage methods to achieve data durability beyond what standard HDFS
three-way replication provides.

Durability is further improved when using replication.
Bigtable maintains a separate copy of your data in the location
that you select for each cluster of a replicated instance.

## Consistency model

Single-cluster Bigtable instances provide strong consistency. By
default, instances that have more than one cluster provide eventual consistency,
but for some use cases they can be configured to
provide read-your-writes consistency or strong consistency, depending on the
workload and app profile settings.

## Security

Access to your Bigtable tables is controlled by your Google Cloud
project and the Identity and Access Management (IAM) roles that you assign to
users. For example, you can assign IAM roles that prevent
individual users from reading from tables, writing to tables, or creating new
instances. If someone does not have access to your project or does not have an
IAM role with appropriate permissions for Bigtable,
they cannot access any of your tables.

You can also control access to table data by creating an authorized view
of a table that represents a subset of the table data. Then you can grant
authorized view-level permissions to some users without
granting them table-level permissions.
You can manage security at the project, instance, table, or
authorized view levels. Bigtable does not support
row-level, column-level, or cell-level security restrictions.

## Encryption

By default, all data stored within Google Cloud, including the data in
Bigtable tables, is encrypted at rest using
the same hardened key management systems that we use for our own encrypted data.

If you want more control over the keys used to encrypt your
Bigtable data at rest, you can use customer-managed encryption
keys (CMEK).

## Backups

Bigtable backups let you save a copy of a
table's schema and data and then restore to a new table at a later time.
Using backups and backup copies, you can restore to a new table in any region or
project where you have a Bigtable instance, regardless of where
the source table is.

## Change data capture

Bigtable provides change data capture (CDC) in the form of *change
streams*. Change streams let you capture and stream out data changes to a table
as the changes happen. You can read a change stream using a service such as
Dataflow to support use cases including data analytics, audits,
archiving requirements, and triggering downstream application logic. For more
information, see the Overview of change streams.

## Request routing with app profiles

App profile routing policies let you control which clusters
handle incoming requests from your applications. Bigtable offers
the following types of app profiles based on the compute model used:

- **Standard app profiles**: use provisioned cluster nodes to handle requests.
  They support the following routing policies:

  - **Single-cluster routing**: sends all requests to a single cluster.

    You can enable the in-memory tier (Preview) only for app
    profiles that use single-cluster routing. When you configure an app
    profile to use the in-memory tier on a cluster, all eligible point-read
    traffic uses the in-memory tier.
  - **Multi-cluster routing to any cluster**: sends requests to the nearest
    available cluster in an instance, either among all clusters or a
    specified cluster group.
- **Data Boost app profiles**: use serverless compute instead of the
  cluster's nodes to isolate high-throughput read jobs from your core
  application traffic. These profiles are restricted to a single-cluster
  routing policy.

## Other storage and database options

Bigtable isn't a traditional relational database.
While it does support SQL queries, certain use cases might
be better suited for another database option.

- If you must store highly structured objects in a document database, with
  support for ACID transactions and SQL-like queries, consider Firestore.
- To sync data between users in real time, consider the Firebase Realtime Database.
- If you need interactive querying in an online analytical processing (OLAP)
  system, consider BigQuery.

For more information about other database options, see the overview
of database services.
Google Cloud also has various
storage options.

## What's next

- Try a Bigtable quickstart using the
  `cbt` CLI
  , the command-line tool for Bigtable.
- Work through a Bigtable codelab.
- Learn about Bigtable instances, clusters, and nodes.
- Learn about Bigtable tiered storage.
- Learn about Bigtable editions.
- Learn about the Bigtable in-memory tier.
- Learn how to create a Bigtable instance.
- Learn how to migrate to Bigtable.
- Learn about the client libraries for Cloud Bigtable.
- Read the original OSDI paper about Bigtable.
