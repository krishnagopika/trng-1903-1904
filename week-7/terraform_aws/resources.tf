resource "aws_s3_bucket" "demo" {

    bucket = "demo-trng-1903-1904-1" 
    tags= {
        Env = "dev"
    }
}


resource "aws_instance" "demo" {
    ami = lookup(var.ami_ids_al2, var.region)
    instance_type = "t2.micro"

    tags = {
      Name = "demo-trng-1903-1904-1"
      Env = "dev"
    }
  
}

