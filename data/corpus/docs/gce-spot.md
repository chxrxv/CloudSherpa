---
doc_id: gce-spot
title: Spot VMs
url: https://docs.cloud.google.com/compute/docs/instances/spot
category: cost
fetched_at: '2026-10-13T15:13:49+00:00'
license: CC BY 4.0 (Google Cloud documentation)
---

This page describes Spot VMs:
virtual machine (VM) instances that are excess
Compute Engine capacity. Spot VMs have significant discounts,
but Compute Engine might preemptively stop or delete (*preempt*)
Spot VMs to reclaim the capacity at any time. Spot VMs
are the latest version of
preemptible VMs.

Specifically, Spot VMs are VMs that use the *spot provisioning model*.
The provisioning model of a VM
affects its discounts and availability. The spot provisioning model lets you
obtain resources at much lower prices compared to standard VMs. However,
Compute Engine can preempt Spot VMs at any time to reclaim
resources. Use Spot VMs to reduce costs for fault-tolerant workloads,
such as batch processing jobs or stateless applications.

## What are Spot VMs?

Spot VMs are available at much lower
prices—up to 91% discounts for many machine types, GPUs, TPUs,
and Local SSDs—compared to the on-demand price for standard VMs.

However, Compute Engine might preempt Spot VMs at any time,
such as when it needs the resources for other tasks. At this uncertain
preemption time, Compute Engine either stops (default) or deletes your
Spot VMs depending on your specified termination action for each
Spot VM.

Spot VMs are excess Compute Engine capacity, so their
availability varies based on Compute Engine usage. You can help
mitigate availability issues for Spot VMs by following the best
practices, like viewing the availability of Spot VMs before creation,
as explained later in this document. Spot VMs don't have a minimum
or maximum runtime unless you specifically
limit the runtime.

If your workloads are fault-tolerant and can withstand possible VM
preemption, Spot VMs can reduce your Compute Engine
costs significantly. For example, batch processing jobs can run on
Spot VMs. If some of those VMs stop during processing, the
job slows but does not completely stop. Spot VMs complete your
batch processing tasks without placing additional load on your existing
VMs and without requiring you to pay full price for additional standard VMs.

## Spot VMs limitations

Spot VMs function like standard VMs but have the
following limitations:

- Spot VMs don't support the following machines:
  - The A4X machine series
  - Bare metal instances
- The Google Cloud Free Tier credits for
  Compute Engine don't apply to Spot VMs.
- Compute Engine might preempt Spot VMs to reclaim
  the resources at any time. Compute Engine preempts
  Spot VMs for a variety of reasons—for example, system events.
  The probability that Compute Engine preempts Spot VMs is
  generally low, but might vary from day to day and from zone to zone depending
  on current conditions. For more information, see
  Preemption selection in this document.
- Spot VMs are finite Compute Engine resources, so they
  might not always be available.
- Spot VMs can't
  live migrate
  to become standard VMs while they are running or be set to
  automatically restart
  when there is a host event.
- Due to the preceding limitations, Spot VMs are not covered by any
  Service Level Agreement and are excluded from the
  Compute Engine SLA.

## Preemption of Spot VMs

This section describes how Compute Engine preempts Spot VMs
and which VMs are selected for preemption. Additionally, instructions to detect,
handle, and test preemption of Spot VMs are explained later in
Manage preemption of Spot VMs.

### Preemption process

Compute Engine performs the following steps to preempt
Spot VMs:

1. Compute Engine sends a preemption notice to the VM by updating
   the `preempted` value in your VM's default metadata to `TRUE`, which your
   workload can monitor to detect preemption.

   The *preemption notice duration*
   is the duration between this metadata signal and when
   Compute Engine sends a
   ACPI G2 Soft Off
   signal to begin the shutdown period. The preemption notice duration affects
   how your workload can handle preemption and can be set to one of the
   following values while you are creating a Spot VM:

   - **120 seconds**:
     We recommend setting the preemption notice duration to 120 seconds for any
     workloads that need a dedicated duration or longer than 30 seconds to
     handle preemption. You can handle preemption within your workload by
     waiting for the VM to be preempted. (Optionally, you can also specify a
     shutdown script, which runs during the following best-effort shutdown
     period.)
   - **0 seconds (default)**: If the preemption notice duration for a
     Spot VM isn't specified or is set to 0, then there is no
     dedicated delay between detecting preemption in metadata and the
     ACPI G2 Soft Off signal. Your workload can handle the preemption notice
     during the following shutdown period by using a shutdown script.
