resource "azurerm_resource_group" "TRNG1904-RG" {
    name="TRNG1904-RG"
    location=var.location
  
}

resource "azurerm_storage_account" "demo" {
    name=lookup(var.saname, var.location)
    resource_group_name = azurerm_resource_group.TRNG1904-RG.name
    location = var.location
    account_tier = "Standard"
    account_replication_type = "LRS" 
}