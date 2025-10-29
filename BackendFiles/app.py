from fastapi import FastAPI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Optional
import os
import uvicorn #this handles all url in the browser
import json

# # Loading .env file and confirming that it has been loaded
load_dotenv()
# print(os.getenv('host'))

#Creating an instance of the FastAPI
app = FastAPI(title='esther simple app', version='1.0.0')

data = [{
    "name": "Esther",
    "track": "Engineer"},
    
    {"name": "Ayo",
    "track": "Developer"},

    {"name": "Deborah", 
     "track": "Engineer"}
]

#GET REQUEST
@app.get("/") #/ indicates the root file
def get_file():
    return "this is your file"

#POST REQUEST
class FilePost(BaseModel):
    name: str 
    track: str

@app.post("/send_file")
def send_file(input: FilePost):
    data.append(input.model_dump())
    return {"message":"File saved successfully.","hgfchgf":data}

#PUT REQUEST
@app.put("/update_file/{id}")
def update_file(id : int, req: FilePost): #updates info at the specified index number {id}
    data[id].update(req.model_dump())
    return {"message": "file update", "data": data}

#DELETE REQUEST
@app.delete("/remove_file/{id}")
def remove_file(id: int, req: FilePost):
    d_id = data[id]
    req = req.model_dump()
    if (req["name"] == d_id["name"]) & (req["track"] == d_id["track"]):
        data.pop(id)
        return {"message": "data deleted", "data": data}
    else:
        return {"message":"Data not found"}


#PATCH REQUEST this edits existing information
class FilePostPatch(BaseModel):
    name: Optional[str] = Field(None)
    track: Optional[str] = Field(None)

@app.patch('/patch_file/{id}')
def change_file(id: int, req:FilePostPatch):
    data[id].update(req.model_dump(exclude_unset=True))
    return {"message": "Data update", "data": data}


if __name__ == "__main__":
    uvicorn.run(app, host=os.getenv("host"), port=int(os.getenv("port"))) #converted port to integer because all .env entries are strings

