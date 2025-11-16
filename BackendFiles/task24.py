from fastapi import FastAPI
from pydantic import BaseModel, Field
from dotenv import load_dotenv
import os
import uvicorn
from typing import Optional

load_dotenv()
data = [{
    "name": "Esther","age": 70,"track": "Engineer"
},
{
    "name": "Eli", "age": 45, "track": "Developer"
},
{
    "name": "Daniel", "age": 25, "track": "Engineer"
}]
app = FastAPI(title="Simple FastAPI App", version= "1.0.0")

#using pydantic to restrict the data types that can be inputted by the user

class Item(BaseModel):
    name: str = Field(..., example="Esther")
    age: int = Field(..., example = 20)
    track: str = Field(..., example= "Developer")

#Implementing an API endpoint to delete a specifid field from the data variable
@app.delete("/remove-data/{id}")
def remove_data(id:int, req: Item):
    req = req.model_dump()
    dt = data[id]
    if (req["name"] == dt["name"]) & (req["age"] == dt["age"]):
        data.pop(id)
        print(data)
        return {"Message": "Data updated", "Data": data}
    
    else:
        return {"Message": "Data not found"}
    
# Implementing an API endpoint to update (PATCH) a specific value in the DATA variable.
class ItemPatch(BaseModel):
    name: Optional[str] = Field(None, example = "Esther")
    age: Optional[int] =Field(None,example=25)
    track: Optional[str] =Field(None,example="Fullstack Developer")

@app.patch("/modify-data/{id}")
def modify_data(id:int, req:ItemPatch):
    data[id].update(req.model_dump(exclude_unset = True))
    print(data)
    return {"Message": "Data successfully modified", "Data": data}

if __name__ == '__main__':
    print(os.getenv('host'))
    print(os.getenv('port'))
    uvicorn.run(app, host= os.getenv('host'), port=int(os.getenv("port")))