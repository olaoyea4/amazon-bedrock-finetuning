# Bedrock Model Finetuning

This repo shows how to finetune an Amazon Bedrock foundation model using a sample dataset.

## Contents
- `setup_prerequisites.py`: Sets up an S3 bucket and IAM role needed for finetuning 
- `data_prep.py`: Downloads the dataset, preprocesses it to conform with Bedrock finetuning format, and uploads it to the S3 bucket
- `finetune.py`: Starts a Bedrock finetuning job using a base foundation model
- `invoke_model.py`: Starts a basic Streamlit user interface to interact with the finetuned model
- `requirements.txt`: Python package dependencies 

## Dependencies
Install dependencies
    ```bash
    pip install -r requirements.txt
    ```

## Model Finetuning
1. Setup prerequisites
    ```bash
    python setup_prerequisites.py
    ```  
2. Prepare training data
    ```bash 
    python data_prep.py
    ```
3. Start finetuning
    ```bash
    python finetune.py
    ```

## Custom Model Usage
1. After model finetuning completes, purchase a provisioned throughput to use the model following instructions [here](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-use.html)
2. Retrieve the Provisioned Model Arn from the Bedrock Console and update the `provisioned_model_arn` variable in `invoke_model.py`. 
3. Run the streamlit application to interact with the finetuned
    ```bash
    streamlit run invoke_model.py
    ```
    This opens a UI window on your browser to start prompting the model
