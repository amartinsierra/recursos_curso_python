import matplotlib.pyplot as plot, pandas as pd
df=pd.read_json("alumnos.json")
df.index=df["nombre"] #eje x
df["nota"].plot(kind="bar")
plot.show()
