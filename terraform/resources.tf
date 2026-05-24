#terraform resource file for expense project

# ECR repository for expense-bot Docker image
resource "aws_ecr_repository" "expense_bot" {
  name                 = "expense-bot"
  image_tag_mutability = "MUTABLE"
  image_scanning_configuration {
    scan_on_push = false
  }
}

# IAM policy for GitHub Actions
resource "aws_iam_policy" "github_actions_policy" {
  name = "github-actions-expense-bot-policy"
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "ecr:GetAuthorizationToken",
          "ecr:BatchCheckLayerAvailability",
          "ecr:GetDownloadUrlForLayer",
          "ecr:BatchGetImage",
          "ecr:InitiateLayerUpload",
          "ecr:UploadLayerPart",
          "ecr:CompleteLayerUpload",
          "ecr:PutImage"
        ]
        Resource = "*"
      },
      {
        Effect   = "Allow"
        Action   = ["lambda:UpdateFunctionCode"]
        Resource = "arn:aws:lambda:eu-central-1:${data.aws_caller_identity.current.account_id}:function:expense-bot"
      }
    ]
  })
}

# IAM user for GitHub Actions
resource "aws_iam_user" "github_actions_user" {
  name = "github-actions-expense-bot"
}

# Attach policy to user
resource "aws_iam_user_policy_attachment" "github_actions_attachment" {
  user       = aws_iam_user.github_actions_user.name
  policy_arn = aws_iam_policy.github_actions_policy.arn
}

# IAM role for Lambda execution
resource "aws_iam_role" "lambda_exec_role" {
  name = "expense-bot-lambda-role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect    = "Allow"
        Principal = { Service = "lambda.amazonaws.com" }
        Action    = "sts:AssumeRole"
      }
    ]
  })
}

# S3 read/write policy for Lambda
resource "aws_iam_role_policy" "lambda_s3" {
  name = "expense-bot-s3-policy"
  role = aws_iam_role.lambda_exec_role.id
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "s3:GetObject",
          "s3:PutObject"
        ]
        Resource = "${aws_s3_bucket.expense_data.arn}/*"
      }
    ]
  })
}

# Attach basic Lambda execution policy (CloudWatch logs)
resource "aws_iam_role_policy_attachment" "lambda_basic" {
  role       = aws_iam_role.lambda_exec_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

# Lambda function
resource "aws_lambda_function" "expense_bot" {
  function_name = "expense-bot"
  role          = aws_iam_role.lambda_exec_role.arn
  package_type  = "Image"
  image_uri     = "${aws_ecr_repository.expense_bot.repository_url}:latest"
  memory_size   = 256
  timeout       = 30

  environment {
    variables = {
      S3_BUCKET_NAME = aws_s3_bucket.expense_data.bucket
    }
  }
}

# API Gateway HTTP API
resource "aws_apigatewayv2_api" "expense_bot" {
  name          = "expense-bot-API"
  protocol_type = "HTTP"
}

# API Gateway stage
resource "aws_apigatewayv2_stage" "default" {
  api_id      = aws_apigatewayv2_api.expense_bot.id
  name        = "default"
  auto_deploy = true
}

# Lambda integration
resource "aws_apigatewayv2_integration" "lambda" {
  api_id                 = aws_apigatewayv2_api.expense_bot.id
  integration_type       = "AWS_PROXY"
  integration_uri        = aws_lambda_function.expense_bot.invoke_arn
  payload_format_version = "2.0"
}

# Route
resource "aws_apigatewayv2_route" "post" {
  api_id    = aws_apigatewayv2_api.expense_bot.id
  route_key = "POST /expense-bot"
  target    = "integrations/${aws_apigatewayv2_integration.lambda.id}"
}

# Permission for API Gateway to invoke Lambda
resource "aws_lambda_permission" "api_gw" {
  statement_id  = "AllowAPIGatewayInvoke"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.expense_bot.function_name
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${aws_apigatewayv2_api.expense_bot.execution_arn}/*/*"
}

# S3 bucket for persistent expense data
resource "aws_s3_bucket" "expense_data" {
  bucket = "expense-bot-data-115643029932"
}

# Block all public access
resource "aws_s3_bucket_public_access_block" "expense_data" {
  bucket                  = aws_s3_bucket.expense_data.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}