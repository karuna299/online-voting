provider "aws" {
  region = "ap-south-1"
}

# Use default VPC
data "aws_vpc" "default" {
  default = true
}

# Use first subnet in default VPC
data "aws_subnets" "default" {
  filter {
    name   = "vpc-id"
    values = [data.aws_vpc.default.id]
  }
}

# Security Group
resource "aws_security_group" "app_sg" {
  name        = "online-voting-sg"
  description = "Allow HTTP, SSH, Jenkins, and App traffic"

  ingress {
    description = "SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "HTTP"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "Jenkins"
    from_port   = 8080
    to_port     = 8080
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "online-voting"
    from_port   = 5000
    to_port     = 5000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# EC2 Instance (single)
resource "aws_instance" "app_server" {
  ami           = "ami-02d26659fd82cf299" # Ubuntu AMI (Mumbai region)
  instance_type = "t2.micro"

  vpc_security_group_ids = [aws_security_group.app_sg.id]
  subnet_id              = tolist(data.aws_subnets.default.ids)[0]
  key_name               = var.key_name

  tags = {
    Name = "online-voting-app"
  }
}

