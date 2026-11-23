from fastapi import FastAPI
from Person import Person

app=FastAPI()
@app.get("/saludo")
def saludar():
    return {"saludo":"Hola Fast API"}
@app.get("/saludo/{name}")
def saludar(name):
    return {"saludo":"Bienvenido/a "+name+" a Fast API"}
@app.get("/saludo-completo")
def saludar(name:str, age:str):
   return {"saludo":"Bienvenido/a "+name+" a Fast API. Tienes "+age+" años"} 
@app.get(path="/person",response_model=Person)
def person()->Person:
    #return {"name":"prueba","age":33,"email":"prueba@gmail.com"}
    return Person(name="prueba",age="33",email="prueba@gmail.com")

@app.post(path="/person",response_model=Person)
def person(person:Person):
    print(person.name,person.age,person.email)
    return person