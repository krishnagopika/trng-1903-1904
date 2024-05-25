resource "aws_s3_bucket" "demo" {

    bucket = "demo-trng-1903-1904-1" 
    tags= {
        Env = "dev"
    }
}

# resource "aws_s3_bucket" "trng-1903-s3-buckets" {
#     count = 3
#     bucket = "%{ if var.s3_bucket_names!="" }${var.s3_bucket_names}-${count.index}%{else}${var.default_buckt_name}%{ endif }"

#     tags = {
#       name = "${var.s3_bucket_names}-${count.index}"
#     }
  
# }

# data "aws_ami" "ubuntu"{
#     most_recent = true
#     owners = ["amazon"]
#     filter {
#       name = "name" 
#       values = [var.ami_pattern]
#     }
# }
# resource "aws_instance" "demo-1903" {

#     ami = data.aws_ami.ubuntu.image_id
#     instance_type = "t2.micro"

#     tags = {
#       Name = "demo-trng-1903-1904-1"
#       Env = "prod"
#     }
  
# }

# resource "null_resource" "demo_null_resource" {

#     depends_on = [ aws_instance.demo-1903 ]

#     provisioner "local-exec" {

#       command = "echo ${aws_instance.demo-1903.public_ip} > public_ip.txt"
      
#     }
  
# }


# resource "aws_instance" "demo" {
#     ami = lookup(var.ami_ids_al2, var.region)
#     instance_type = "t2.micro"

#     tags = {
#       Name = "demo-trng-1903-1904-1"
#       Env = "dev"
#     }
  
# }


# module "vpc" {
#   source = "terraform-aws-modules/vpc/aws"

#   name = "my-vpc"
#   cidr = "10.0.0.0/16"

#   azs             = ["us-east-1a", "us-east-1b", "us-east-1c"]
#   private_subnets = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
#   public_subnets  = ["10.0.101.0/24", "10.0.102.0/24", "10.0.103.0/24"]

#   enable_nat_gateway = true
#   enable_vpn_gateway = true

#   tags = {
#     Terraform = "true"
#     Environment = "dev"
#   }
# }