output "resource_group_name" {
  value = azurerm_resource_group.streamcart.name
}

output "resource_group_location" {
  value = azurerm_resource_group.streamcart.location
}
output "acr_login_server" {
  value = azurerm_container_registry.acr.login_server
}

output "aks_cluster_name" {
  value = azurerm_kubernetes_cluster.aks.name
}
