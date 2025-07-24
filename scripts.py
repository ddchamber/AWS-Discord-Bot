# list_models.py
from dotenv import load_dotenv
import os
import boto3

load_dotenv()
region = os.getenv("AWS_DEFAULT_REGION")
print(f"Using region: {region}")

# Print which AWS identity we’re using
sts = boto3.client("sts", region_name=region)
print("Caller identity:", sts.get_caller_identity()["Arn"])

# List all foundation models
bedrock = boto3.client("bedrock-runtime", region_name=region)
models = bedrock.list_foundation_models()["modelSummaries"]
print("\nAccessible Bedrock models:")
for m in models:
    print(" •", m["modelId"])
