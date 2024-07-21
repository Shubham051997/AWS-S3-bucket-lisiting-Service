output "bucket_name" {
  value = var.bucket_name
}

output "instance_ip" {
  value = aws_instance.web.public_ip
}
