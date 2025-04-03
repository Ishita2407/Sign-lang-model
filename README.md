# Sign-lang-model

## Workflows
constants
update entities - config and artifact entity
config_entity
artifact_entity
components - data ingestion, data validation, model evaluation etc
pipeline - training pipeline.py : to manage which thing will be done in what order
data ingestion -> data validation -> model trainer -> model pusher 
app.py


## Project Configuration

#install aws cli from the following link

https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

#Configure aws crediential (secret key & access key)

aws configure
#Create a s3 bucket for model pusher. name is mentioned in the consrtant


## How to run:
```bash
conda create -n signlang python=3.7 -y
```
```bash
conda activate signlang
```
```bash
pip install -r requirements.txt
```
```bash
python app.py
```
