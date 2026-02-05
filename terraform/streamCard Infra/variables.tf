variable "resource_group_name" {
  description = "Resource Group name for StreamCart"
  type        = string
}

variable "location" {
  description = "Azure region"
  type        = string
  default     = "eastus"
}

variable "subscription_id" {
  description = "Azure Subscription ID"
  type        = string
}
variable "acr_name" {
  description = "Azure Container Registry name (must be globally unique)"
  type        = string
}

variable "aks_name" {
  description = "AKS cluster name"
  type        = string
}

variable "node_count" {
  description = "AKS node count"
  type        = number
  default     = 1
}

variable "node_vm_size" {
  description = "AKS node VM size"
  type        = string
  default     = "Standard_B2s"
}
