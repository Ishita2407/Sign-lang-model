# Sign-lang-model
![image](https://github.com/user-attachments/assets/e226d0db-e69d-4617-9770-daf05e715384)

![image](https://github.com/user-attachments/assets/c7d4c1e0-57af-4855-9e1a-f75770490068)

![image](https://github.com/user-attachments/assets/7cb31ea7-58ed-4829-b615-0183794c5354)

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
## Project OUTPUT for detecting several actions

# No ouput
![image](https://github.com/user-attachments/assets/10c0cfb5-9538-4560-93fb-cd5e7fca0c44)


# Yes output
![image](https://github.com/user-attachments/assets/ac7fa04a-34c7-49c1-84c8-4bc92616f097)


# Hello output
![image](https://github.com/user-attachments/assets/83227deb-07c9-4c94-838c-6509d7ba23df)


# Please output
![image](https://github.com/user-attachments/assets/543d7abc-fa58-4a18-8208-10fcdf5960de)

# Thanks output
![image](https://github.com/user-attachments/assets/ceac64c8-1906-472b-8f41-64722a333407)


# I love you 
![image](https://github.com/user-attachments/assets/28997ede-a733-4837-94da-659d164e382b)

![image](https://github.com/user-attachments/assets/7eef436a-f10c-4232-bac6-34ec6b093840)


