---
doc_id: logging-overview
title: Cloud Logging overview
url: https://docs.cloud.google.com/logging/docs/overview
category: operations
fetched_at: '2026-10-13T15:13:49+00:00'
license: CC BY 4.0 (Google Cloud documentation)
---

This document provides an overview of Cloud Logging, which is a real-time
log-management system with storage, search, analysis, and monitoring support.
Cloud Logging automatically collects log data from Google Cloud resources.
Your applications, on-premise resources,
and resources from other cloud providers can send log data to Cloud Logging.
You can also configure alerting policies so that Cloud Monitoring notifies
you when certain kinds of events are reported in your log data. For regulatory
or security reasons, you can determine where your log data is stored.

## Collect log data from your applications and third-party software

You can collect log data from applications that you write by using a
client library to instrument your
application. However, it's not always
necessary to instrument your application. For example, for some
configurations you can use the Ops Agent
to send log data that were written to
`stdout` or `stderr` to your Google Cloud project.

You can also collect log data from your third-party applications, like `nginx`,
by installing the Ops Agent and then configuring it to write log data
from that application to your Google Cloud project.

See Which should you use: Logging agent or client library?
for information that can help you decide which approach best suits your
requirements.

## Query, view, and analyze log data

To view and analyze your log data, use the Logs Explorer or Observability Analytics
pages of the Google Cloud console:

- Logs Explorer: This interface lets you view individual
  log entries and to find and view related log entries. The interface also
  annotates log entries when they are part of an error group,
  or when trace data is available. We recommend this interface when you
  want to troubleshoot your services and applications.
- Observability Analytics: This interface lets you query your log data with
  SQL, and to find trends and patterns in that data.
  For example, you can compute the average latency for HTTP requests issued
  to a specific URL over time, and monitor whether the latency has any
  fluctuations.

For more information, see Query and view log data.

## Visualize and monitor your log data

You can configure Cloud Logging to notify you when certain kinds of events
occur in your log data. These notifications might be sent when a particular
pattern appears in a log entry, or when a trend is detected in your log data.
If you're interested in viewing the error rates of your Google Cloud services,
then you can view the Cloud Logging dashboard, which is preconfigured.

To get notified when a particular message is part of a log entry,
like when a critical security-related event occurs,
create a log-based alerting policy. These policies are useful for important
but rare events, like the following:

- An event appears in an audit log entry.
  For example, a user accesses the security key of a service account.
- A deployment message is in a log entry.

To get notified when a trend occurs in your log data, create a log-based metric
and monitor the metric with an alerting policy.
A *log-based metric* either counts the number of log entries that match some
criterion, or they extract and organize information like response times
into histograms. Log-based metrics are suitable when you want
to do any of the following:

- Monitor the count of occurrences of a message in your log data, like the
  number of log entries that record a status of error.
- Observe trends in your data, like latency values in your log data,
  and receive a notification if the values change in an unacceptable way.
- Create charts to display the numeric data extracted from your log data.

For more information, see Monitor your log data.

## Log storage and retention

You don't have to configure the location where log data is stored.
By default, Google Cloud projects, billing accounts, folders, and organization
resources automatically store the log data that originates in the resource.
For example, if your Google Cloud project contains a
Compute Engine instance, then the log data
Compute Engine generates is automatically stored.

You can configure a number of aspects about
your log storage, such as which log data are stored,
which are discarded, and where the log data are stored.
For more information, see Store log entries.

Log entries are stored for a specified length of time and are then deleted. For
more information, see Logs retention periods.

## Log routing

You can *route*, or forward, log entries to the following destinations:

- Google Cloud project
- Log bucket

- BigQuery dataset

- Cloud Storage bucket

- Pub/Sub topic, which provides support for third-party integrations
  like Splunk or Datadog.

When log data is routed, the destination can be in a different
resource from where the log data originates. For example, you can route
log data from one project to a log bucket stored in a different project.

For more information, see Route log entries.

## Categories of log data

Log categories are meant to help describe the logging information available
to you; the categories aren't mutually exclusive:

- *Platform* log entries are written by Google Cloud services. These
  log entries can help you debug and troubleshoot issues, and help you better
  understand the Google Cloud services you're using.
- *Component* log entries are generated by Google Cloud-provided software
  components that run on your systems. For example, GKE
  provides software components that users can run on their own virtual
  machine or in their own data center. These log entries are often used to
  provide user support.
- *Security* log entries help you answer "who did what, where, and when":

  - Cloud Audit Logs provide information about
    administrative activities and accesses within your
    Google Cloud resources.
    Enabling audit logs helps your security, auditing, and compliance
    entities monitor Google Cloud data and systems for possible
    vulnerabilities or external data misuse.
    For a list of supported services, see
    Google Cloud services with audit logs.
  - Access Transparency logs record actions taken by Google Cloud
    staff when accessing your Google Cloud content. Access Transparency
    logs can help you track compliance with your legal and
    regulatory requirements for your organization.
    For a list of supported services, see
    Google Cloud services with Access Transparency logs.

- *User-written* log entries are logs written by custom applications and
  services. Typically, this data is written to Cloud Logging by using
  the Ops Agent, the Cloud Logging API, or the
  Cloud Logging client libraries.

- *Multicloud* and *Hybrid-cloud* log entries refer to log data from
  other cloud providers like Microsoft Azure and
  logs from on-premises infrastructure.

## Access control

Identity and Access Management (IAM) permissions and roles control access to log buckets.
You can grant predefined roles to principals, or you can create custom roles.
For more information about required permissions, see
Access control.

## Pricing

To learn about pricing for Cloud Logging, see the Google Cloud Observability pricing page.

## What's next

- Log entry data-model.
- Store log data.
- Route log data.
- Query and view logs overview.
