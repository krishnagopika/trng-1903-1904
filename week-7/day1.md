# Lecture Plan

1. Terraform Fundamentals


### IaC

**IaC:** Infrastructure as Code.

- **Automation** of infrastructure
- used to maintain the **state** (compliant)
- makes the infrastructure **auditable**
  - used to keep the infrastructure change history in a version constrol system.

### Installing Terraform

1. download the zip file from [https://developer.hashicorp.com/terraform/downloads](https://developer.hashicorp.com/terraform/downloads)
2. extract it in a folder
3. set the path variable for the tearraform
4. run `terraforn -v` to get the terraform version and check if the terraform is installed.


### Provider

- Cloud providers

ex: AWS, Azure and GCP etc.

### Resource

- Cloud Resources

ex: `aws_s3_bucket`, `azurerm_resource_group`

### State

1. Desired State
2. Known State
3. Actual State

### Outputs

```
output "my_output" {
  value = resource.name.value
}
```

### Basic TF commands

1. `terraform init`
2. `terraform plan`
3. `terraform apply`