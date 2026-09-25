# Terraform Infrastructure

This directory contains the Terraform configuration for the Tiny AI Agent development environment.

## Infrastructure

- AWS S3 bucket
- Region: us-east-1
- Environment: dev
- Managed by Terraform

## Terraform Commands

Initialize Terraform:


terraform init

Review the infrastructure plan:

terraform plan

Apply the infrastructure:

terraform apply

Show managed resources:

terraform state list

Destroy the infrastructure when no longer needed:

terraform destroy

Idempotency

After applying the infrastructure, running:

terraform plan

returned:

No changes

This demonstrated that Terraform recognized the infrastructure as already matching the configuration.

Drift Detection

A test tag was manually added to the S3 bucket through the AWS Console.

Running:

terraform plan

then returned:

Plan: 0 to add, 1 to change, 0 to destroy.

This demonstrated that Terraform detected a difference between the actual AWS infrastructure and the Terraform configuration.

Cleanup

The S3 bucket is a development resource and uses:

force_destroy = true

Unused infrastructure should be destroyed with:

terraform destroy