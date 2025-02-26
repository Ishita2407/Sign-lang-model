# Sign-lang-model

## Workflows
constants
config_entity
artifact_entity
components
pipeline
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
