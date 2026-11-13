import datetime as dt
fecha=dt.date(2023,4,20)
print(fecha)
formato="%d/%m/%Y"
print(dt.datetime.strftime(fecha,formato))