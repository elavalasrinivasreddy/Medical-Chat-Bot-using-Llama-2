from src.helper import data_extractor,text_splitter,download_embedding_model
from langchain.vectorstores import Pinecone
import pinecone
from dotenv import load_dotenv
import os

load_dotenv()

# load the .env keys
PINE_CONE_API_KEY = os.getenv('PINE_CONE_API_KEY')
PINE_CONE_ENV = os.getenv('PINE_CONE_ENV')
index_name = os.getenv('index_name')

# load the pdf data 
pdf_data = data_extractor('data/')

# creating text chunks
text_chunks = text_splitter(pdf_data)

# loading the embedding model {text to vectors}
embedding_model = download_embedding_model()

# initializing the vector DB pinecone
pinecone.init(api_key = PINE_CONE_API_KEY, #type: ignore
              environment = PINE_CONE_ENV #type: ignore
            )

# creating embeddings for each text chunk and storing into pinecone
doc_search = Pinecone.from_texts([i.page_content for i in text_chunks], # list of chunks text
                                  embedding = embedding_model, # Embedding model
                                  index_name = index_name  # pinecone index name
                                  )

