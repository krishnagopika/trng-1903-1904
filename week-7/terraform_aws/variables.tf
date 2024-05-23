variable "region" {
    description = "aws region"
    type = string
    default = "us-east-1"
  
}

variable "ami_ids_al2" {
    description = "ami ids per region"
    type = map(string)
    default = {
      "us-east-1" = "ami-0bb84b8ffd87024d8"
      "us-west-1" = "ami-0cbe318e714fc9a82"
    }
  
}
