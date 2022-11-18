import mysql.connector


class ConexionMsql :

    #-----------------CONEXON----------------------------------
  ENDPOINT ="bdnuevo.csxxus8lnosn.us-east-1.rds.amazonaws.com"
  PORT="3306"
  USER="admin"
  PASSWORD="123456789"
  DBNAME="bdnuevo"

  try:
    conexion=mysql.connector.connect(
        host=ENDPOINT, 
        user=USER, 
        password=PASSWORD, 
        database=DBNAME
        )
    # if conexion.is_connected():
    #    print ("Conexión Exitosa")
    #    info_server=conexion.get_server_info()
    #    print(info_server)
    #    cursor=conexion.cursor()
    #    cursor.execute("SELECT DATABASE()")
    #    row=cursor.fetchall()
    #    print("Conectado a la base de datos: {}".format(row))
       
  except  Exception as ex:
    print (ex) 
#   finally:
#     if conexion.is_connected():
#         conexion.close()
#         print ("Conexión finalizada") 







     

