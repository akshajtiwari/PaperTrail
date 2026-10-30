from fastapi import  FastAPI,status,HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel,HttpUrl
from datetime import date,datetime
from uuid import uuid4
from typing import Optional #Used to mark the fields in the PATCH schema as optional

class application_detail(BaseModel):
    company_name: str
    role_title:str
    application_url:HttpUrl #Validates url
    date_applied: date
    status:str
    notes:str

class application_response(application_detail): #inherits application detail schema fields and adds 3 of its own (id, creation and updation)
    id:str
    created_at: datetime
    updated_at: datetime

class application_update(BaseModel): #Optional Schema for the Patch endpoint  
    company_name: Optional[str]=None
    role_title:Optional[str]=None
    application_url:Optional[HttpUrl]=None #Validates url
    date_applied: Optional[date]=None
    status:Optional[str]=None
    notes:Optional[str]=None

def generate_time():
    created_at=datetime.now()
    updated_at=created_at
    return created_at,updated_at

app=FastAPI()

@app.get("/health")
async def healthcheck():
    return JSONResponse( 
        content={"Status":"healthy"},
        status_code=200
    )
applications_list=[]

@app.post("/applications",status_code=status.HTTP_201_CREATED)
async def application(details:application_detail):
    created_at,updated_at=generate_time()
    post_id=str(uuid4()) #random version 4 UUID as a string, e.g. "6770d16c-4394-..." (a string so JavaScript can't round it like a big int)
    response=application_response(
        **details.model_dump(), #creates a dictionary of the details
        id=post_id,
        created_at=created_at,
        updated_at=updated_at
    )
    applications_list.append(response) #add the response to a list of all the applications , use database later 
    return response

@app.get("/applications")
async def get_applications(
    page: int=1,
    page_size:int=20,
    status:str|None=None, #the variable can contain either a string or None if nothing then None
    search:str|None=None, #search is defined as a Function Parameter with default value (None) but not used so fastapi will use it as a query parameter
    sort:str="date_applied_desc"
):
    sorted_applications=sorted(
        applications_list, #using sort(list) creates a new list instead of sorting the original list
        key=lambda application:application.date_applied,
        reverse=True #last applied is first 
    )
    return sorted_applications

@app.get("/applications/{application_id}",status_code=status.HTTP_200_OK)
async def applications_byid(application_id:str):
    for application in applications_list:
        if application.id==application_id:
            return application
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Application not found"
    )
    
@app.patch("/applications/{application_id}",status_code=status.HTTP_200_OK)
async def application_update_status(application_id:str,             update_data:application_update): #update_data: application_update is a type annotation that tells to expect a request body matching the application_update schema.
    for application in applications_list:
        if application.id ==application_id:

            changes=update_data.model_dump(exclude_unset=True) # creates a dictionary with only the fields that were sent , and not the entire schema
            if any(value is None for value in changes.values()):
                raise HTTPException(
                    status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
                    detail="Updated fields cannot be Null"
                )
            for field,value in changes.items():
                setattr(application,field,value)
            if changes:
                application.updated_at=datetime.now() #if there is a field in changes then it was updated so put its time again 
            return application
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Application not Found"
    )