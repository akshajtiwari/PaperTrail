from fastapi import  FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel,HttpUrl
from datetime import date,datetime
from uuid import uuid4

class application_detail(BaseModel):
    company_name: str
    role_title:str
    application_url:HttpUrl #Validates url
    date_applied: date
    status:str
    notes:str

class application_response(application_detail): #inherits application detail schema fields and adds 3 of its own (if, creation and updation)
    id:int
    created_at: datetime
    update_at: datetime

def generate_time():
    created_at=datetime.now()
    update_at=created_at
    return created_at,update_at

app=FastAPI()

@app.get("/health")
async def healthcheck():
    return JSONResponse( 
        content={"Status":"healthy"},
        status_code=200
    )
applications_list=[]

@app.post("/applications")
async def application(details:application_detail):
    created_at,updated_at=generate_time()
    post_id=uuid4() #creates a random number id using the 128 bits 122 are completely random , version 4 
    response=application_response(
        **details.model_dump(), #creates a dictionary of the details
        id=post_id.int,
        created_at=created_at,
        update_at=updated_at
    )
    applications_list.append(response) #add the response to a list of all the applications , use database later 
    return response

@app.get("/applications")
async def get_applications(
    page: int=1,
    page_size:int=20,
    status:str=None,
    search:str=None,
    sort:str="date_applied_desc"
):
    sorted_applications=sorted(
        applications_list, #using sort(list) creates a new list instead of sorting the original list
        key=lambda application:application.date_applied,
        reverse=True #last applied is first 
    )
    return sorted_applications

