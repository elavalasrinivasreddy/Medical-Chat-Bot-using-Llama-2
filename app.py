from flask import Flask,render_template,request
from src.helper import download_embedding_model
from langchain.vectorstores import Pinecone
import pinecone
from langchain.llms import CTransformers
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
import os
from src.prompt import *
from store_index import PINE_CONE_API_KEY, PINE_CONE_ENV

# Creating flask app
app = Flask(__name__)
load_dotenv()

# Reading pine cone keys
PINE_CONE_API_KEY = os.getenv('PINE_CONE_API_KEY')
PINE_CONE_ENV = os.getenv('PINE_CONE_ENV')
index_name = os.getenv('index_name')
model_name = os.getenv('model_name')
model_file = os.getenv('model_file')

# Loading the embedding model
embedding_model = download_embedding_model()

# initializing the pinecone
pinecone.init(api_key=PINE_CONE_API_KEY, #type: ignore
              environment=PINE_CONE_ENV) #type: ignore

# loading the existing index from pinecone
doc_search = Pinecone.from_existing_index(index_name,embedding_model)

# loading the prompt
prompt = PromptTemplate(template=prompt_template,
                        input_variables=['context','question'],
                        )
chain_type_kwargs = {'prompt':prompt}

# loading the llm model
# model_type='llama',
model = CTransformers(  model=model_name,
                        model_file=model_file,
                        config = {  'temperature':0.35,
                                    'max_new_tokens':1024
                                }
                    )

# # creating QA
qa_bot = RetrievalQA.from_chain_type(llm=model,
                                     chain_type="stuff",
                                     retriever = doc_search.as_retriever(search_kwargs={'k':4}),
                                     return_source_documents=True,
                                     chain_type_kwargs=chain_type_kwargs
                                    )


# routing the initial page
@app.route('/')
def index():
    return render_template('chat.html')

@app.route("/response", methods=["GET", "POST"])
def chat():
    user_input = request.form["input"]
    print('User Input : ',user_input)
    result = qa_bot({"query": user_input})
    print("Response : ", result["result"])
    return str(result["result"])

if __name__=="__main__":

    app.run(debug=True)