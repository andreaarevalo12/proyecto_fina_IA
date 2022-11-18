import json
from datetime import datetime
from flask import Flask, request, jsonify
import os
import time
from random import choice
from flask_cors import CORS, cross_origin
from sistemadereglas import *
from conexion import *


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
    fechaActual = ''

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


if __name__ == '__main__':
   app.run(debug=True)