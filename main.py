from llama_index.llms.openai import OpenAI
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.core import Settings
from dotenv import load_dotenv
import os

load_dotenv()

# Config LLM
Settings.llm = OpenAI(model="gpt-4", api_key=os.getenv("OPENAI_API_KEY"))

# Data Ingestion
documents = SimpleDirectoryReader("./data").load_data()

# Creating Index
index = VectorStoreIndex.from_documents(documents)

# Querying
query_engine = index.as_query_engine()
response = query_engine.query("Cuales son los 3 mangas mas populares del 2023?")
print(response)