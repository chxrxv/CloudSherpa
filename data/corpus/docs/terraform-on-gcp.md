---
doc_id: terraform-on-gcp
title: Overview of Terraform on Google Cloud
url: https://docs.cloud.google.com/docs/terraform/terraform-overview
category: operations
fetched_at: '2026-10-13T15:13:49+00:00'
license: CC BY 4.0 (Google Cloud documentation)
---

Hashicorp Terraform is an Infrastructure as code (IaC) tool that lets you
provision and manage cloud infrastructure. Terraform provides plugins called
*providers* that lets you interact with cloud providers and other
APIs. You can use the *Terraform provider for Google Cloud* to
provision and manage Google Cloud infrastructure.

## Benefits of using Terraform

This section explains some of the benefits of using Terraform to provision and
manage Google Cloud infrastructure:

- Terraform is the most commonly used tool to provision and automate
  Google Cloud infrastructure. You can use the
  Google Cloud provider
  to configure and manage all Google Cloud resources using the same
  declarative syntax and tooling.
- Terraform lets you specify your preferred end state for your infrastructure.
  You can then deploy the same configuration multiple times to create
  reproducible development, test, and production environments.
- Terraform lets you generate an execution plan that shows what Terraform will
  do when you apply your configuration. This lets you avoid any surprises when
  you modify your infrastructure through Terraform.
- Terraform lets you package and reuse common code in the form of
  modules.
  Modules present standard interfaces for creating cloud resources. They
  simplify projects by increasing readability and allow teams to organize
  infrastructure in readable blocks. Additionally, Google Cloud
  publishes a number of opinionated deployable modules as
  blueprints and
  getting-started examples as Jump Start
  Solutions.
- Terraform records the current state of your infrastructure and lets you
  manage state effectively. The Terraform state file keeps track of all
  resources in a deployment.

## Using Terraform

Terraform has a declarative and configuration-oriented syntax, which you can use
to author the infrastructure
that you want to provision. Using this syntax, you'll define your preferred
end-state for your infrastructure in a *Terraform configuration file*. You'll then
use the Terraform CLI to provision
infrastructure based on the configuration file.

The following steps explain how Terraform works:

1. You describe the Google Cloud infrastructure you want to provision
   in a Terraform configuration file. You don't need to author code
   describing *how* to provision this configuration.
2. You run the `terraform plan` command, which evaluates your configuration
   and generates an execution plan. You can review the plan and make changes as
   needed.
3. Then, you run the `terraform apply` command, which performs the following
   actions:
   - It provisions your infrastructure based on your execution plan by invoking
     the corresponding Google Cloud APIs in the background.
   - It creates a *Terraform state file*, which is a JSON formatted mapping of
     resources in your configuration file to the resources in the
     real world infrastructure. Terraform uses this file to know the latest
     state of your infrastructure, and to determine when to create, update, and
     destroy resources.
4. Subsequently, when you run `terraform apply`, Terraform uses the mapping in
   the state file to compare the existing infrastructure to the code, and make
   updates as necessary:
   - If a resource object defined in the configuration file does not exist in
     the state file, Terraform creates it.
   - If a resource object exists in the state file, but has a different
     configuration from your configuration file, Terraform updates the
     resource to match your configuration file.
   - If a resource object in the state file matches your configuration
     file, Terraform leaves the resource unchanged.

## Google Cloud providers

There are two providers that let you provision and manage Google Cloud
infrastructure:

- `google`: Use this provider to provision and manage
  Google Cloud APIs.
- `google-beta`: Use this provider to provision and manage
  Google Cloud beta APIs.

For instructions on using these providers, see the
Google Cloud provider configuration reference.

`google` and `google-beta` providers are developed using a tool called
*Magic Modules*. Magic Modules allows contributors to make changes against a
single codebase and develop both `google` and `google-beta` providers
simultaneously.

You can contribute to the Google Cloud providers using Magic
Modules by following the instructions in the
Magic Modules contribution guide.

## What's next

- Learn how to
  create a basic web server on Compute Engine using Terraform
- Learn how to
  store Terraform state in a Cloud Storage bucket
- Look through the
  Terraform modules and blueprints for Google Cloud
- Look through the various
  Terraform for Google Cloud samples
