variable "region" {
    description = "aws region"
    type = string
    default = "us-east-1"
  
}

variable "s3_bucket_names" {
  type = map(string)
  description = "sample bucket names"
  default = {
    "us-east-1-1" = "demo-trng-1903-1904-1"
    "us-east-1-1" = "demo-trng-1903-1904-2"
  }
  
}

variable "ami_ids_al2" {
    description = "ami ids per region"
    type = map(string)
    default = {
      "us-east-1" = "ami-0bb84b8ffd87024d8"
      "us-west-1" = "ami-0cbe318e714fc9a82"
    }
    
  
}

variable "ami_pattern" {
  type = string
  description = "ami pattern"
  default = "ubuntu/images/hvm-ssd-gp3/ubuntu-noble-24.04-amd64-server-20240423"
  
}


variable "default_buckt_name" {
  type = string
  description = "def value"
}