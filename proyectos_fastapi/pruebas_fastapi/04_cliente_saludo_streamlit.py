import httpx as http
class Persona:
    def __init__(self,name,age,salary,email):       
        self.name=name
        self.age=0
        self.salary=100
        self.email=""
    
res=http.get("http://localhost:8000/person")
pr=Persona(**res.json())
print(pr.name)