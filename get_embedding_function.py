import os
from langchain_ollama import OllamaEmbeddings
#from langchain.embeddings.bedrock import BedrockEmbeddings


def get_embedding_function():
#    embeddings = BedrockEmbeddings(
#        credentials_profile_name="default", region_name="us-east-1"
#    )
    embeddings = OllamaEmbeddings(
        model="nomic-embed-text", base_url=os.getenv("OLLAMA_BASE_URL", "http://127.0.0.1"))
    return embeddings
