import boto3
import datetime

bedrock = boto3.client(service_name='bedrock')
account_id = boto3.client('sts').get_caller_identity()['Account']
    
# Set parameters
customModelName = "meta-custom-model-dolly"
baseModelIdentifier = "arn:aws:bedrock:us-east-1::foundation-model/meta.llama2-13b-v1:0:4k"
# customModelName = "amazon-titan-custom-model-dolly"
# baseModelIdentifier = "arn:aws:bedrock:us-east-1::foundation-model/amazon.titan-text-express-v1"


# Create job
datetime_string = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
response_ft = bedrock.create_model_customization_job(
    jobName=f"Finetune-Job-{datetime_string}",
    customizationType="FINE_TUNING",
    roleArn=f"arn:aws:iam::{account_id}:role/Bedrock-Finetuning-Role-{account_id}",
    hyperParameters = {
        "epochCount": "5",
        "batchSize": "1",
        "learningRate": ".0001",
        # "learningRateWarmupSteps": "5"
    },
    trainingDataConfig={"s3Uri": f"s3://bedrock-finetuning-{account_id}/train.jsonl"},
    # validationDataConfig={'validators': [{"s3Uri": f"s3://bedrock-finetuning-{account_id}/test.jsonl"}]},
    outputDataConfig={"s3Uri": f"s3://bedrock-finetuning-{account_id}/finetuning-output"},
    customModelName=customModelName,
    baseModelIdentifier=baseModelIdentifier
)

jobArn = response_ft.get('jobArn')
print(jobArn)