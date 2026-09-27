terraform {
  required_version = ">= 1.6.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.62"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

module "s3_bucket" {
  source = "./modules/s3-bucket"

  bucket_prefix = "tiny-ai-agent-dev-"
  force_destroy = true
  environment  = var.environment
  bucket_name  = "tiny-ai-agent-${var.environment}"
}