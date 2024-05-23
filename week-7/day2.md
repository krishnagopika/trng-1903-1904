# Lecture Plan

1. Terrafrom Advanced

---

### Terraform Syantx

- HashiCorp Configuration Language (HCL)

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

### Type

- This argument specifies what value types are accepted for the variable.
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

### Variable loading precedence:

1. Environment variables
2. The terraform.tfvars file, if present.
3. The terraform.tfvars.json file, if present.
4. Any *.auto.tfvars or *.auto.tfvars.json files, processed in lexical order of their filenames.
5. Any -var and -var-file options on the command line, in the order they are provided. (This includes variables set by an HCP Terraform workspace.)

### builin function

   1. lookup
   2. count

### Templates

#### Interpolation

- used to embed expresions into the strings.

```
"${}"
```

#### Directives

- a sequence is a directive. 

" %{ if id var.name != "" } "

### Conditionals

```
condition ? true_val : false_val
```

### for each


```
resource "azurerm_resource_group" "rg" {
  for_each = tomap({
    a_group       = "eastus"
    another_group = "westus2"
  })
  name     = each.key
  location = each.value
}
```

### Data Sources

- used to define the information outside the terraform.
- information related to resources of a cloud provider

ex: aws ec2 ami

- supports filtering data


ex:


```tf
data "aws_ami" "ubuntu" {
  most_recent = true
  owners =["aws"]

  tags = {

  }
  filter {
    name   = "name"
    values = ["web"]
  }
}
```

### modules

### workspaces


- used to manage multiple deplpyments with same resourse configuration.

commands

`terraform workspace`

Subcommands:
    delete    Delete a workspace
    list      List Workspaces
    select    Select a workspace
    show      Show the name of the current workspace




### null resource & provisionr


- to perfom actions on a physical resource without actually provisioning the actual resource

```
resource "null_resource" "example" {
  provisioner "name" {
    command = ""
  }
}
```
**provisioner**: type of provisioner to execute commands. ex: local, remote


### tainting & updating resources/ replace


- used to relace the resource with the desired config
```
terraform apply -replace"resource.name"
```