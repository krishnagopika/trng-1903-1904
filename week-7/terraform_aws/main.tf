provider "aws" {
    region = "us-east-1"
}


resource "aws_iam_policy" "demo-policy" {
  name = "demo-policy"
  description = "s3 full access policy"
  policy = file("./policies/s3-full-access-policy.json")
}

resource "aws_s3_bucket" "demo-s3-bucket" {
    bucket = "demo-s3-bucket"
    tags = {
        Env = "dev"
    }
}

resource "aws_instance" "demo-ec2" {
    ami = data.aws_ami.ubuntu.image_id
    instance_type = "t2.micro"

    tags = {
        Name = "demo-ec2"
        Env = "dev"
    }

}

