# resource "aws_s3_bucket" "demo" {

#     bucket = "demo-trng-1903-1904-1" 
#     tags= {
#         Env = "dev"
#     }
# }

# resource "aws_s3_bucket" "trng-1903-s3-buckets" {
#     count = 3
#     bucket = "%{ if var.s3_bucket_names!="" }${var.s3_bucket_names}-${count.index}%{else}${var.default_buckt_name}%{ endif }"

#     tags = {
#       name = "${var.s3_bucket_names}-${count.index}"
#     }
  
# }

data "aws_ami" "ubuntu"{
    most_recent = true
    owners = ["amazon"]
    filter {
      name = "name" 
      values = [var.ami_pattern]
    }
}


resource "aws_instance" "demo" {
    ami = data.aws_ami.ubuntu.image_id
    instance_type = "t2.micro"

    tags = {
      Name = "demo-trng-1903-1904-1"
      Env = "dev"
    }
  
}


# resource "aws_instance" "demo" {
#     ami = lookup(var.ami_ids_al2, var.region)
#     instance_type = "t2.micro"

#     tags = {
#       Name = "demo-trng-1903-1904-1"
#       Env = "dev"
#     }
  
# }

