output "bucket_arn" {
  value = aws_s3_bucket.demo.arn  
}

output "instance_id" {
    value = aws_instance.demo.id
  
}
