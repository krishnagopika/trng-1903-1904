variable "location" {
    type = string
    default = "EAST US"
    sensitive = false 
}

variable "saname" {

    type = map(string)
    default = {
        "EAST US" = "demo-eastus"
        "WEST US" = "demo-westus"
    }

}


