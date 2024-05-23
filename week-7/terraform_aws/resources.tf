# resource "aws_s3_bucket" "demo" {

#     bucket = "demo-trng-1903-1904-1" 
#     tags= {
#         Env = "dev"
#     }
# }

# resource "aws_s3_bucket" "trng-1903-s3-buckets" {
#     for_each = var.s3_bucket_names
#     bucket = each.value
  
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

