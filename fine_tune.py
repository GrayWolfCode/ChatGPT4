import openai
import json

openai.api_key = "your_openai_api_key"

with open("my_dataset.json", "r") as f:
   data = json.load(f)

dataset = openai.Dataset.create(
   data=data,
   name="my_dataset_name",
   description="my_dataset_metadata",
)

fine_tuning = openai.FineTune.create(
   model="text-davinci-002",  
   dataset=dataset["id"], 
   n_steps=1000,  
   prompt_tokens=1024,  
)

# You can check the status of the fine-tuning job using the fine-tuning ID
job_id = fine_tuning["id"]