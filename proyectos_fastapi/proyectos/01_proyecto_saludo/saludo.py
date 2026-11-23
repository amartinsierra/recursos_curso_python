from fastapi import FastAPI
app=FastAPI()
@app.get("/saludo")
def saludar():
    return {"saludo":"Hola Fast API"}