import httpx as http
class Persona:
    def __init__(self,name,age,salary,email):       
        self.name=name
        self.age=age
        self.salary=salary
        self.email=email
    
res=http.get("http://localhost:8000/person")
pr=Persona(**res.json())
#print(pr.name)

res=http.post("http://localhost:8000/person/77",json=vars(Persona("unos",22,1000,"aaaa@gmail.com")))
print(res.status_code)
print(res.json())