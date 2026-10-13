---
doc_id: cdn-overview
title: Cloud CDN overview
url: https://docs.cloud.google.com/cdn/docs/overview
category: networking
fetched_at: '2026-10-13T15:13:49+00:00'
license: CC BY 4.0 (Google Cloud documentation)
---

Cloud CDN (Content Delivery Network) uses Google's global edge network to
serve content closer to users, which accelerates your websites and
applications.

Cloud CDN works with the global external Application Load Balancer
or the classic Application Load Balancer
to deliver content to your users. The external Application Load Balancer provides the frontend IP
addresses and ports that receive requests and the backends that respond to the
requests.

Cloud CDN content can be sourced from various types
of backends.

In Cloud CDN, these backends are also called *origin servers*.
Figure 1 illustrates how responses from origin servers that run on
virtual machine (VM) instances flow through an external Application Load Balancer before being
delivered by Cloud CDN. In this situation, the
Google Front End (GFE)
comprises Cloud CDN and the external Application Load Balancer.

**Figure 1.** Responses flow from origin servers through Cloud CDN to clients.

## How Cloud CDN works

When a user requests content from an external Application Load Balancer, the request
arrives at a GFE that is at the edge of Google's
network as close as possible to the user.

If the load balancer URL map routes traffic to a backend service or backend
bucket that has Cloud CDN configured, the GFE uses Cloud CDN.
Backend services can use Compute Engine, GKE Ingress,
or GKE Gateway backends.

### Cache hits and cache misses

A cache is a group of servers that stores and manages content so that
future requests for that content can be served faster. The cached content is a
copy of cacheable content that is stored on origin servers.

If the GFE looks in the Cloud CDN cache and finds a cached response
to the user's request, the GFE sends the cached response to the user. This is
called a *cache hit*. When a cache hit occurs, the GFE looks up the content by
its cache key and responds directly to the user,
shortening the round-trip time and saving the origin server from having to
process the request.

A *partial hit* occurs when a request is served partially from cache and
partially from a backend. This can happen if only part of the requested content
is stored in a Cloud CDN cache, as described in
Support for byte range requests.

The first time that a piece of content is requested, the GFE determines that it
can't fulfill the request from the cache. This is called a *cache miss*. When a
cache miss occurs, the GFE forwards the request to the external Application Load Balancer. The
load balancer then forwards the request to one of your origin servers. When the
cache receives the content, the GFE forwards the content to the user.

If the origin server's response to this request is
cacheable, Cloud CDN stores the
response in the Cloud CDN cache for future requests.
Data transfer from a cache to a client is called *cache egress*.
Data transfer to a cache is called *cache fill*.

Cache hit and cache miss behavior is consistent across all supported backend
types, including Compute Engine, backend buckets, GKE Ingress,
and GKE Gateway.

Figure 2 shows a cache hit and a cache miss:

1. Origin servers running on VM instances send HTTP(S) responses.
2. The external Application Load Balancer distributes the responses to Cloud CDN.
3. Cloud CDN delivers the responses to end users.

**Figure 2.** The initial response is served by the origin server
while subsequent responses are served by the GFE from cache.

For costs related to cache hits and cache misses, see Pricing.

### Cache hit ratio

The *cache hit ratio* is the percentage of times that a requested object is
served from the cache. If the cache hit ratio is 60%, it means that the
requested object is served from the cache 60% of the time and must be retrieved
from the origin 40% of the time.

For information about how cache keys can affect the cache hit ratio,
see Using cache keys.
For troubleshooting information, see Cache hit ratio is
low.

#### View the cache hit ratio for a small time period

To view the cache hit ratio for a small time period (the last few minutes):

1. In the Google Cloud console, go to the **Cloud CDN** page.

   Go to Cloud CDN
2. For each origin, see the **Cache hit ratio** column.

   **n/a** means that the load-balanced content isn't cached or hasn't
   been requested recently.

#### View the cache hit ratio for a longer time period

To view the cache hit ratio for a time period from 1 hour to 30 days:

1. In the Google Cloud console, go to the **Cloud CDN** page.

   Go to Cloud CDN
2. In the **Origin name** column, click the origin name.
3. Click the **Monitoring** tab.
4. Optional: select a specific backend.

The CDN hit rate is one of the available monitoring graphs. A graph that
displays **No data** means that the content isn't cached or hasn't been requested in the displayed time range.

You can adjust the time period by selecting a different time range. The
following image is an example of time ranges that you can select:

### Insert content into the cache

Caching is reactive in that an object is stored in a particular cache if a
request goes through that cache and if the response is cacheable. An object
stored in one cache does not automatically replicate into other caches; cache
fill happens only in response to a client-initiated request. You cannot preload
caches except by causing the individual caches to respond to requests.

When the origin server supports byte range
requests, Cloud CDN can initiate
multiple cache fill requests in reaction to a single client request.

### Serve content from a cache

After you enable Cloud CDN, caching happens automatically for all
cacheable content. Your origin server uses HTTP headers to indicate which
responses are cached. You can also control cacheability by using cache
modes.

When you use a backend bucket, the origin server is Cloud Storage. When
you use VM instances, the origin server is the web server software that you run
on those instances.

Cloud CDN uses caches in numerous locations around the world. Because
of the nature of caches, it is impossible to predict whether a particular
request is served out of a cache. You can, however, expect that popular requests
for cacheable content are served from a cache most of the time, yielding
significantly reduced latencies, reduced cost, and reduced load on your origin
servers.

For more information about what Cloud CDN caches
and for how long, see the Caching overview.

To see what Cloud CDN is serving from a cache, you can view
logs.

### Remove content from the cache

To remove an item from a cache, you can invalidate cached content. For more
information, see:

- Cache invalidation overview
- Invalidate cached content

### Cache bypass

To bypass Cloud CDN, you can request an object directly from a
Cloud Storage bucket or a Compute Engine VM. For example, a URL for a
Cloud Storage bucket object looks like this:

```
https://storage.googleapis.com/STORAGE_BUCKET/FILENAME
```

### Cache expiration and eviction policies

For content to be served from a cache, it must have been inserted into the
cache, it must not be evicted, and it must not be expired.

*Eviction* and *expiration* are two different concepts. They both affect what
gets served, but they don't directly affect each other.

#### Eviction

If you are testing content caching with a small number of requests, you might
notice that the content gets evicted.

Every cache has a limit on how much it can hold. However, Cloud CDN
adds content to caches even after they're full. To insert content into a full
cache, the cache first removes something else to make room. This is called
eviction. Caches are usually full, so they are constantly evicting content. They
generally evict content that hasn't recently been accessed, regardless of the
content's expiration time. The evicted content might be expired, and it might
not be. Setting an expiration time doesn't affect eviction.

*Unpopular content* means content that hasn't been accessed in a while. *A
while* and *unpopular* are both relative to the bulk of other items in the
cache. Multiple Google Cloud projects share a common pool of cache space
because the projects are served from the same set of GFEs. The relative
popularity of content is compared across multiple projects, not only within
a single project.

As caches receive more traffic, they also evict more cached content.

As with all large-scale caches, content can be evicted unpredictably, so no
particular request is guaranteed to be served from the cache.

#### Expiration

Content in HTTP(S) caches can have a configurable expiration time. The
expiration time informs the cache not to serve old content, even if the content
hasn't been evicted.

For example, consider a picture-of-the-hour URL. Its responses should
be set to expire in under one hour. Otherwise, the served content might be an
old picture from a cache.

For information about fine tuning expiration times, see
Using TTL settings and overrides.

## Requests initiated by Cloud CDN

When your origin server supports byte range requests, Cloud CDN
can send multiple requests to the origin server in reaction to a single client
request. As described in
Support for byte range requests,
Cloud CDN can initiate two types of requests: validation requests
and byte range requests.

## Data location settings of other Cloud Platform Services

Using Cloud CDN means that data may be stored at serving
locations outside of the region or zone of your origin server. This is normal
and how HTTP caching works on the internet. Under the
Service Specific Terms of the Google Cloud Platform
Terms of Service, the Data Location Setting that is available for certain Cloud
Platform Services does not apply to Core Customer Data for the respective Cloud
Platform Service when used with other Google products and services (in this case
the Cloud CDN service). If you don't want this outcome,
don't use the Cloud CDN service.

## Support for Google-managed SSL certificates

You can use
Google-managed certificates when Cloud CDN is enabled.

## Global Front End

**Preview**

This product or feature is
subject to the "Pre-GA Offerings Terms" in the General Service Terms section
of the Service Specific
Terms.
Pre-GA products and features are available "as is" and might have limited support.
For more information, see the
launch stage descriptions.

Global Front End
combines Cloud CDN,
global external Application Load Balancers,
Google Cloud Armor, and
Service Extensions into one
solution to help deliver, scale, and secure your internet-facing applications.
With the
Global Front End Enterprise
billing tier, pricing for these products is consolidated under a
single pricing plan.

You can enable the
Global Front End Enterprise billing tier in your Google Cloud project. For
more information, see Global Front End pricing
or go to the
Global Front End page
on the Google Cloud console.

**Note:** You can use Cloud CDN with standalone pricing
or under the unified pricing of Global Front End Enterprise. To
continue using standalone pricing, you don't need to take any further action.

## Integration with Google Cloud Armor

Google Cloud Armor with Cloud CDN features two types of security policies:

- **Edge security policies**. These policies can be applied to your
  Cloud CDN-enabled origin servers. They apply to all
  traffic, before CDN lookup.
- **Backend security policies**. These policies are enforced only for requests
  for dynamic content, cache misses, or other requests that are destined for
  your origin server.

For more information, see the Cloud Armor
documentation.

## Integration with Service Extensions

Cloud CDN lets you add custom code to the request processing path of
global external Application Load Balancers by using Service Extensions plugins.
These plugins help you implement customizations in the request path
pre-cache and influence how content is cached within Cloud CDN.
Additionally, you can run your plugins on the request path or the response
path from your server.

For more information, see
Use Service Extensions for edge compute.

## Integration with GKE Gateway

For workloads running on GKE, you can configure
Cloud CDN by using the Gateway API. Cloud CDN caching behavior
is defined using the `GCPHTTPFilter` resources that are attached to the
`HTTPRoute` resources. For traffic routed through the Gateway, these filters let you configure cache policies, including cache modes and TTL settings.

For more information, see Configure Cloud CDN for Gateway.

## What's next

- To enable Cloud CDN for your HTTP(S) load balanced instances and
  storage buckets, see Using Cloud CDN.
- GKE Ingress: To use Cloud CDN with
  GKE Ingress controller, see
  Configure Cloud CDN through Ingress
- GKE Gateway API: To use Cloud CDN with
  Gateway API and `GCPHTTPFilter`, see Configure Cloud CDN for Gateway
- To find GFE points of presence, see Cache locations.
