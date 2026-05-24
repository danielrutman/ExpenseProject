#terraform config file to be used by terraform to config infrastruct to desired state

#declaration of needed provider
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}
#initialization of providers
provider "aws" {
  region = "eu-central-1"
}

data "aws_caller_identity" "current" {}

# Output the API Gateway URL
output "api_gateway_url" {
  value = "${aws_apigatewayv2_stage.default.invoke_url}/expense-bot"
  description = "Twilio webhook URL"
}

