resource "aws_vpc" "personal_vpc" {
  cidr_block = var.cidr_block

  tags = {
      project = var.project_tag
  }
}

resource "aws_subnet" "public" {
  cidr_block              = var.cidr_block
  vpc_id                  = aws_vpc.default.id
  map_public_ip_on_launch = true

  tags = {
      project = var.project_tag
  }
}

resource "aws_internet_gateway" "gateway" {
  vpc_id = aws_vpc.personal_vpc.id
}

resource "aws_route" "internet_access" {
  route_table_id         = aws_vpc.personal_vpc.main_route_table_id
  destination_cidr_block = "0.0.0.0/0"
  gateway_id             = aws_internet_gateway.gateway.id
}

resource "aws_eip" "gateway" {
  vpc        = true
  depends_on = [aws_internet_gateway.gateway]
}
