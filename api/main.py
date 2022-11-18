import json
from datetime import datetime
from flask import Flask, request, jsonify
import os
import time
from random import choice
from flask_cors import CORS, cross_origin
from sistemadereglas import *
from conexion import *
from regresion_multiple import *


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

conexion = ConexionMsql.conexion



# @cross_origin()
@app.route('/api/v1/sistemasDeReglas', methods=['POST'])
def sistemasDeReglas():
    fullname = request.json['fullname']
    respuesta1 = request.json['respuesta1']
    respuesta2 = request.json['respuesta2']
    respuesta3 = request.json['respuesta3']
    respuesta4 = request.json['respuesta4']
    respuesta5 = request.json['respuesta5']

    # creacion del objeto
    engine = sistemadereglas()

    ### reset Preparar el motor para la ejecución.
    engine.reset()

    v_abdominal = respuesta1
                                               
    engine.declare(reglas(abdominal=choice([str(v_abdominal)])))
                
    v_fiebre = respuesta2
    engine.declare(reglas(fiebre=choice([str(v_fiebre)])))

    v_deposiciones = respuesta3
    engine.declare(reglas(deposiciones=choice([int(v_deposiciones)])))  
        
    v_vomito = respuesta4
    engine.declare(reglas(vomito=choice([str(v_vomito)])))
                
                
    v_apetito = respuesta5                 
    engine.declare(reglas(apetito=choice([str(v_apetito)])))
                           
    engine.run()
    
    if conexion.is_connected():
       print ("Conexión Exitosa")
       cursor=conexion.cursor()
       cursor.execute("""INSERT INTO sistemareglas (nombre, pr1, pr2, pr3, pr4, pr5, diagnostico,fechareg) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""", (fullname, respuesta1, respuesta2, respuesta3, respuesta4, respuesta5, engine.diagnostico, datetime.now()))
       conexion.commit()
       cursor.close()
   
    return jsonify(engine.diagnostico)

@app.route('/api/v1/getAllReports/<diagnostico>', methods=['GET'])
def getAllReports(diagnostico):
    diagnosticoFinal = {
        "1": "Usted no presenta sintomas de una enfermedad del sistema digestivo",
        "2": "Usted no presenta sintomas de una enfermedad del sistema digestivo. Se recomienda valoracion por nutricion",
        "3": "Los sintomas no son concluyentes, se necesita mas informacion para realizar un diagnostico certero", 
        "4": "Los sintomas no son concluyentes, se necesita mas informacion para realizar un diagnostico certero. Se recomienda hidratarse bien",
        "5": "Usted tiene ENFERMEDAD DIARREICA AGUDA, favor hidratarse bien",
        "6": "Los sintomas no son concluyentes, se necesita mas informacion para realizar un diagnostico certero. Se recomienda valoracion medica",
        "7": "Los sintomas presentados son asociados a PANCREATITIS, se recomienda valoracion medica",
        "8":"Los sintomas presentados son asociados a GASTRITIS, se recomienda valoracion medica",
        "9": "Los sintomas presentados son asociados a ENFERMEDAD DE CROHN, se recomienda valoracion medica",
        "10": "Los sintomas presentados son asociados a SINDROME DE INTESTINO IRRITABLE, se recomienda valoracion medica",
        "11":"Los sintomas presentados son asociados a ENFERMEDAD CELIACA, se recomienda valoracion medica",
        "12": "Los sintomas presentados son asociados a COLECISTITIS (Calculos Biliares), se recomienda valoracion medica",
        "13": "Los sintomas presentados son asociados a GASTROENTERITIS, se recomienda valoracion medica",
        "14":"Los sintomas presentados son asociados a APENDICITIS, se recomienda valoracion medica",
        "15": "Los sintomas presentados son asociados a APENDICITIS, se recomienda valoracion medica urgente"
    } 

    cur = conexion.cursor(buffered=True)
    cur.execute("""SELECT nombre, diagnostico, fechareg FROM sistemareglas WHERE diagnostico LIKE %s""", (diagnosticoFinal[diagnostico],))
    conexion.commit()
    rv = cur.fetchall()
    print('RESPONSE ', rv)
    cur.close()
    payload = []
    content = {}
    for result in rv:
       content = {'fullname': result[0], 'diagnostico': result[1], 'fecha': result[2]}
       payload.append(content)
       content = {}
    return jsonify(payload)

@app.route('/api/v1/regresionmultiple', methods=['POST'])
def regresionmultiple():
   Hora=request.json['hora']
   Bus_inmovilizado=request.json['bus_inmovilizado']
   Camión_averiado=request.json['camión_averiado']
   Exceso_de_vehículo=request.json['exceso_de_vehículo']
   Atropello=request.json['atropello']
   Ocurrencia_con_carga=request.json['ocurrencia_con_carga']
   Incidente_con_carga_peligrosa=request.json['incidente_con_carga_peligrosa']
   Falta_de_energía_eléctrica=request.json['falta_de_energía_eléctrica']
   Punto_de_inundaciones=request.json['punto_de_inundaciones']
   Manifestaciones=request.json['manifestaciones']
   Árbol_en_la_vía=request.json['arbol_en_la_vía']
   Semáforo_apagado=request.json['semáforo_apagado']
   Semáforo_intermitente=request.json['semáforo_intermitente']
   resultado=prediccion(Hora,Bus_inmovilizado,Camión_averiado,Exceso_de_vehículo,Atropello,Ocurrencia_con_carga,Incidente_con_carga_peligrosa,Falta_de_energía_eléctrica,Punto_de_inundaciones,Manifestaciones,Árbol_en_la_vía,Semáforo_apagado,Semáforo_intermitente)
   predic=resultado[0]
   



   if conexion.is_connected():
      print ("Conexión Exitosa")
      cursor=conexion.cursor()
      cursor.execute("""INSERT INTO trafico (Hora,bus_inmobil,camion_ave,trancon,atropello,carga,carga_peligrosa,energia,inundacion,manifestacion,arbol,semaforo_off,semaforo_int,lentitud_porc) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s,%s)""",
       (Hora,Bus_inmovilizado,Camión_averiado,Exceso_de_vehículo,Atropello,Ocurrencia_con_carga,Incidente_con_carga_peligrosa,Falta_de_energía_eléctrica,Punto_de_inundaciones,Manifestaciones,Árbol_en_la_vía,Semáforo_apagado,Semáforo_intermitente,predic))
      conexion.commit()
      cursor.close()
   
   return jsonify(resultado)
   ## hasta aqui lo hice (Duvan)


if __name__ == '__main__':
   app.run(debug=True)