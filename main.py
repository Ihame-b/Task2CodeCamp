from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def hello_world():
    return {'Hello' : 'World'}

#path parameter
@app.get("/component/{component_id}") # path parameter
async def get_component(component_id: int):
    return {"component_id": component_id}


#query parameter
@app.get("/component")
def showComponentId(id:int):
    return{"ID":id}