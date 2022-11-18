#install
#pip install -U scikit-learn
#pip install matplotlib
import numpy as np
import pandas as pd
## SCIKIT LEARN 
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from conexion import *
conexion = ConexionMsql.conexion
##lectura del archivo
data=pd.read_sql("SELECT * FROM trafico", conexion)
Hora=data["Hora"].values
Bus_inmovilizado=data["bus_inmobil"].values
Camión_averiado=data["camion_ave"].values
Exceso_de_vehículo=data["trancon"].values
Atropello=data["atropello"].values
Ocurrencia_con_carga=data["carga"].values
Incidente_con_carga_peligrosa=data["carga_peligrosa"].values
Falta_de_energía_eléctrica=data["energia"].values
Punto_de_inundaciones=data["inundacion"].values
Manifestaciones=data["manifestacion"].values
Árbol_en_la_vía=data["arbol"].values
Semáforo_apagado=data["semaforo_off"].values
Semáforo_intermitente=data["semaforo_int"].values
lentitud_en_el_trafico=data["lentitud_porc"].values
#entrenamiento
X=np.array([Hora,
Bus_inmovilizado,
Camión_averiado,
Exceso_de_vehículo,
Atropello,
Ocurrencia_con_carga,
Incidente_con_carga_peligrosa,
Falta_de_energía_eléctrica,
Punto_de_inundaciones,
Manifestaciones,
Árbol_en_la_vía,
Semáforo_apagado,
Semáforo_intermitente]).T
Y=np.array(lentitud_en_el_trafico)
reg=linear_model.LinearRegression()
reg=reg.fit(X,Y)
Y_pred=reg.predict(X)
error=np.sqrt(mean_squared_error(Y,Y_pred))
r=reg.score(X,Y)
#informacion del entrenamiento
print("el error es: ",error)
print("el varlor de r(score): ",r)
print("los coeficiente son: \n",reg.coef_)
def prediccion(Hora,Bus_inmovilizado,Camión_averiado,Exceso_de_vehículo,Atropello,Ocurrencia_con_carga,Incidente_con_carga_peligrosa,Falta_de_energía_eléctrica,Punto_de_inundaciones,Manifestaciones,Árbol_en_la_vía,Semáforo_apagado,Semáforo_intermitente):
    prediccion=reg.predict([[Hora,
    Bus_inmovilizado,
    Camión_averiado,
    Exceso_de_vehículo,
    Atropello,
    Ocurrencia_con_carga,
    Incidente_con_carga_peligrosa,
    Falta_de_energía_eléctrica,
    Punto_de_inundaciones,
    Manifestaciones,
    Árbol_en_la_vía,
    Semáforo_apagado,
    Semáforo_intermitente]])
    prediccion=round(prediccion[0],2)
    scor=reg.score(X,Y)
    scor=round(scor,2)
    resul=[prediccion,scor]
    print("predict:",prediccion)
    print("escore:",scor)
    return resul