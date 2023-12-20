import os
from pathlib import Path
import logging

# Creating basic logging
logging.basicConfig(level = logging.INFO,
                    format='%(asctime)s == %(message)s')

files_list = [
                'src/__init__.py',
                'src/help.py',
                'src/prompt.py',
                '.env',
                'setup.py',
                'app_test/chat_bot.ipynb',
                'app.py',
                'store_index.py',
                'static/.gitkeep',
                'templates/chat.html'
            ]

for file in files_list:

    # Converting to OS path
    file_path = Path(file)
    # Splitting the path
    file_dir, file_name = os.path.split(file_path)

    # check and create directory
    if os.path.exists(file_dir):
        os.makedirs(file_dir,exist_ok=True)
        logging.info(f"Creating directory : {file_dir}")
    else:
        logging.info(f"{file_dir} is already exist")

    # check and create file
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) ==0) :
        # creating the file
        with open(file_path,'w') as f:
            pass
        logging.info(f"Creating empty file : {file_path}")
    else:
        logging.info(f"{file_path} is already exist")
