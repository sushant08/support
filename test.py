import boto3

logs = boto3.client('logs')
log_groups = logs.describe_log_groups()

for log_group in log_groups['logGroups']:
    log_group_name = log_group['logGroupName']
    codebuild = (x for x in log_group_name if 'lambda' in x)
            response = logs.put_retention_policy(
                logGroupName=codebuild,
                retentionInDays=7
                )


