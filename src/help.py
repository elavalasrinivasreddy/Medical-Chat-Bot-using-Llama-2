from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings 

# Loading the data from PDF file
def data_extractor(dir_path):
    loader = DirectoryLoader(dir_path, # directory path
                            glob="*.pdf", # only pdf files
                            loader_cls = PyPDFLoader, # using module # type: ignore
                            show_progress=True,
                            use_multithreading=True
                            )
    # loading the pdf documents
    documents = loader.load()

    return documents

#Create text chunks
def text_splitter(extracted_data):
    text_split = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 20)
    text_chunks = text_split.split_documents(extracted_data)
    return text_chunks

# Downloading the embedding model from hugging face
def download_embedding_model():
    MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
    emb_model =  HuggingFaceEmbeddings(model_name = MODEL_NAME)
    return emb_model