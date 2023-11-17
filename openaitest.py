import os
import openai

#to do tasks simple we will not set env variables instead will create file where will store our
# api key and access here
from config import apikey

#todo - here we will paste our accounts API key to access openai for responses and results
openai.api_key = apikey

#mera account trial finished bro, toh future mein open krke run kro code it will work then.

response = openai.Completion.create(
  model="davinci",
  prompt="Generate code for creating a desktop game of the name \"Fibonacci numbers game\". It must be written in java.",
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
#Hi 
#printing the response only, not generating here now
print(response)
