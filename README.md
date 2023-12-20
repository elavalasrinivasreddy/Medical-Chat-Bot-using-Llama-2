# Medical-Chat-Bot-using-Llama-2
## Building end to end medical chat bot using Llama 2 LLM

### Steps to run the application

#### clone the git repo
```bash
git clone https://github.com/elavalasrinivasreddy/Medical-Chat-Bot-using-Llama-2
```
Create a virtual environment in conda 
```bash
conda create -n medical_chat_bot python=3.9 -y
```
Activate the virtual environment
```bash
conda activate medical_chat_bot
```
Change the directory to downloaded git repo by
```bash
~$ cd
```
Install all the requirements
```bash
pip install -r requirements.txt
```
Get the pinecone API key and environment 
```bash
https://www.pinecone.io/

API_KEY = ********-****-****-****-************
ENVIRON = ********-****-****-****-************
```
Create Pinecone Indexes 
```bash
index_name = 'test'
```
Embedding model we are usning from HF
```bash
sentence-transformers/all-MiniLM-L6-v2
```
Download the Llama-2 model from HF
```bash
URL : https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML
model = "TheBloke/Llama-2-7B-Chat-GGML"
model_file = 'llama-2-7b-chat.ggmlv3.q5_0.bin'
```
create a .env in your directory and mention values for below keys
```bash
PINE_CONE_API_KEY=""
PINE_CONE_ENV=""
index_name=""
model_name=""
model_file=""
```
If you have data in pinecone index, skip this step other wise follow below steps
Create a "data" directory and move all the pdfs into "data" directory
```bash
mkdir data
mv path/to/*.pdf path/to/data directory
```
And run the below command
```bash
python store_index.py
```
Finally we can run application using below cmd
```bash
python app.py
```
Open the any web browser and paste
```bash
http:\\localhost:5000
```
If you do not have data in pinecone index first you can 

Tech-stack :
--Python
--Langchain
--Flask
--Meta Llama-2
--Pinecone
