from pymongo.mongo_client import MongoClient
from pymongo import MongoClient
from openai import OpenAI
import os

""" OPENAI and PINECONE """
os.environ["OPENAI_API_KEY"] = "sk-proj-zJIEk2g7DFVlQ6JbFSbAT3BlbkFJAWdBEGq1QxQXN671DKqc"
client = OpenAI()

""" CONNECT MONGO DB """
# SERVER PUBLIC MONGO DB
uri = "mongodb+srv://LLMDB:*Hanif20001108@cluster-hanif.gphzrlv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster-Hanif"
client_db = MongoClient(uri)
dbName = "Cluster-Hanif"
collection_jobdesc = client_db[dbName]["job_desc"]
collection_cvinput = client_db[dbName]["cv_input"]
collection_output_hr = client_db[dbName]["output_hr"]

""" Prompt Replacer """
class PromptReplacer:
    def __init__(self, template):
        self.template = template

    def replace_entities(self, replacements):
        updated_template = self.template
        for key, value in replacements.items():
            updated_template = updated_template.replace(key, value)
        return updated_template

""" Setup Unique Code JobDesc """
unique_code = "1a"