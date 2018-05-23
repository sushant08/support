import boto3

logs = boto3.client('logs')
log_groups = logs.describe_log_groups()

for log_group in log_groups['logGroups']:
    log_group_name = log_group['logGroupName']
    if "lambda" in log_group_name:
        print("log group name:", log_group_name)
        response = logs.put_retention_policy(
            logGroupName=log_group_name,
            retentionInDays=30
        )
