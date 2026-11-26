from pydantic import BaseModel, EmailStr, Field

class Person(BaseModel):
    name:str=Field(min_length=3,max_length=50)
    age:int=Field(ge=17,le=70)
    email:EmailStr
    salary:float=Field(ge=0,multiple_of=100)