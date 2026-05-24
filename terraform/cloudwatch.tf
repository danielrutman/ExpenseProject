# SNS topic for CloudWatch alarm notifications
resource "aws_sns_topic" "alerts" {
  name = "expense-bot-alerts"
}

# SNS email subscription
resource "aws_sns_topic_subscription" "email" {
  topic_arn = aws_sns_topic.alerts.arn
  protocol  = "email"
  endpoint  = "danielrutman8@gmail.com"
}

# Alarm 1 - Lambda errors
resource "aws_cloudwatch_metric_alarm" "lambda_errors" {
  alarm_name          = "expense-bot-errors"
  alarm_description   = "Lambda function is throwing errors"
  metric_name         = "Errors"
  namespace           = "AWS/Lambda"
  statistic           = "Sum"
  period              = 60
  evaluation_periods  = 1
  threshold           = 0
  comparison_operator = "GreaterThanThreshold"
  dimensions = {
    FunctionName = aws_lambda_function.expense_bot.function_name
  }
  alarm_actions = [aws_sns_topic.alerts.arn]
}

# Alarm 2 - Lambda invocations approaching free tier
resource "aws_cloudwatch_metric_alarm" "lambda_invocations" {
  alarm_name          = "expense-bot-invocations"
  alarm_description   = "Approaching Lambda free tier limit"
  metric_name         = "Invocations"
  namespace           = "AWS/Lambda"
  statistic           = "Sum"
  period              = 604800
  evaluation_periods  = 1
  # max 1000 free requests weekly allowance of 200 this way wont exceed 800 in a month and will stay in free tier
  threshold           = 200
  comparison_operator = "GreaterThanThreshold"
  dimensions = {
    FunctionName = aws_lambda_function.expense_bot.function_name
  }
  alarm_actions = [aws_sns_topic.alerts.arn]
}

# Alarm 3 - Lambda duration approaching timeout
resource "aws_cloudwatch_metric_alarm" "lambda_duration" {
  alarm_name          = "expense-bot-duration"
  alarm_description   = "Lambda execution time approaching 30s timeout"
  metric_name         = "Duration"
  namespace           = "AWS/Lambda"
  statistic           = "Maximum"
  period              = 60
  evaluation_periods  = 1
  threshold           = 25000
  comparison_operator = "GreaterThanThreshold"
  dimensions = {
    FunctionName = aws_lambda_function.expense_bot.function_name
  }
  alarm_actions = [aws_sns_topic.alerts.arn]
}
