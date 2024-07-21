variable "aws_region" {
  description = "The AWS region to deploy to"
  default     = "us-east-1"
}

variable "bucket_name" {
  description = "The name of the S3 bucket"
}

variable "access_key" {
  description = "xxxxxxxxxx"
}

variable "secret_key" {
  description = "xxxxxxx"
}

variable "instance_type" {
  description = "The EC2 instance type"
  default     = "t2.micro"
}

variable "ami" {
  description = "The AMI ID to use for the EC2 instance"
  default     = "ami-0b72821e2f351e396"  # Amazon Linux 2 AMI
}
