print("Estoy en el curso de Python")
import numpy as np
a = np.array([1, 2, 3, 4, 7])
print(a[a>4])
import pandas as pd
datos=[{"nombre":"paco","edad":20},
    {"nombre":"ana","edad":45},
    {"nombre":"maria","edad":30},
    {"nombre":"laura","edad":32}]
df=pd.DataFrame(datos).query("edad>30")
print(df)

print(df.to_dict(orient="records"))
      

