import boto3

ecr_client = boto3.client('ecr')

response = ecr_client.create_repository(repositoryName="ecr_repo_flask")

repository_uri = response ['repository']['repositoryUri']
print(repository_uri)