variable "project_tag" {
    type = string
    description = "Tag for organizing resources within AWS account"
}

variable "cidr_block" {
    type = string
    description = "CIDR block of VPC and in turn CIDR block of the public subnet"
}