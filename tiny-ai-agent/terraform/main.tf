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

resource "aws_s3_bucket" "dev_environment" {
  bucket_prefix = "tiny-ai-agent-${var.environment}-"

  force_destroy = true

  tags = {
    Project     = "Tiny-AI-Agent"
    Environment = var.environment
    ManagedBy   = "Terraform"
  }
}
