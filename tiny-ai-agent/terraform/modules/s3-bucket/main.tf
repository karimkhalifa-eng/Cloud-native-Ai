resource "aws_s3_bucket" "this" {
  bucket_prefix = var.bucket_prefix
  force_destroy = var.force_destroy

  tags = {
  Name        = var.bucket_name
  Environment = var.environment
  ManagedBy   = "Terraform"
  Project     = "Tiny-AI-Agent"
 }
}
