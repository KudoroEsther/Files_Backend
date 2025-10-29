from fastapi import FastAPI
from dotenv import load_dotenv
import os
import uvicorn #this handles all url in the browser
import json

# # Loading .env file and confirming that it has been loaded
load_dotenv()
# print(os.getenv('host'))

#Creating an instance of the FastAPI
app = FastAPI(title='esther simple app', version=1.0)

data = [{
    "name": "Esther",
    "track": "Engineer"},
    
    {"name": "Ayo",
    "track": "Developer"}
]

#GET REQUEST
@app.get("/") #/ indicates the root file
def get_file():
    return "this is your file"

#POST REQUEST
class FilePost():
    name: str 
    track: str

@app.post("/send_file")
def send_file(input: FilePost):
    data.append(input.model_dump())
    return "File saved successfully."



if __name__ == "__main__":
    uvicorn.run(app, host=os.getenv("host"), port=int(os.getenv("port"))) #converted port to integer because all .env entries are strings

