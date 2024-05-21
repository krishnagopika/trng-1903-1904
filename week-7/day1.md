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


### State

### Output



### Terraform Syantx


**Argument:** An argument assigns a value to a particular name.

**Block:** A block is a container for other content:

**Identifier:** 

- Argument names, block type names, and the names of most Terraform-specific constructs like resources, input variables, etc. are all identifiers.
- Identifiers can contain letters, digits, underscores (_), and hyphens (-). The first character of an identifier must not be a digit, to avoid ambiguity with literal numbers.

**Variables:**

- Variable is decraled using variable block

```tf
variable "var-name" {
    type = type-name
    default = "default-value"
}
```

- variable must be unique among all variables in the same module.
- The name of a variable can be any valid identifier except the following: `source`, `version`, `providers`, `count`, `for_each`, `lifecycle`, `depends_on`, `locals`.

**Argumemts:**

Terraform CLI defines the following optional arguments for a variable.
- default : A default value, If present, the variable is considered to be optional and the default value will be used if no value is set when calling the module or running Terraform. The default argument requires a literal value and cannot reference other objects in the configuration.
- type : This argument specifies what value types are accepted for the variable.
   - string
   - number
   - bool
 - complex types
   - list
   - set
   - map
      - `element` retrieves a value from a list given its index.(`element(list, index)`)
      - `index` finds the element index for a given value in a list.(`index(list, value)`)
      - `lookup` retrieves the value of a single element from a map, given its key. If the given key does not exist, the given default value is returned instead. (`lookup(map, key, default)`)
   - object
   - tuple 

- description : This specifies the input variable's documentation.
- validation : A block to define validation rules, usually in addition to type constraints.
- sensitive : Limits Terraform UI output when the variable is used in configuration.
- nullable : Specify if the variable can be null within the module.

```tf
variable "image_id" {
  type        = string
  default     = "ami-0111101110" 
  description = "The id of the machine image (AMI) to use for the server."

  validation {
    condition     = length(var.image_id) > 4 && substr(var.image_id, 0, 4) == "ami-"
    error_message = "The image_id value must be a valid AMI id, starting with \"ami-\"."
  }
  sensitivie = true
  nullable = false
}
```

- variables can be assigned during the terrafrom plan `-var="var-name=value"`
- Tfvars files allow us to manage variable assignments systematically in a file with the extension .tfvars or .tfvars.json.
- Terraform auto loads tfvars files only when they are named terraform.tfvars or terraform.tfvars.json.
- any other var file can be loaded during runtime using `terraform plan -var-file="filename"`
- to auto load other file, name the file as "name.auto.tfvars"

Variable loading precedence:

![terrafrorm vars precedence](./images/tfvars-precedence.PNG)


### main.tf


### resource


### modules


### State


### outputs


### TF commands