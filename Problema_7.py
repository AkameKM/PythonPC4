#usuario = 'kiaraalvamarinos'
#contra = 'MFmiKqEHcNYcowC4'

#cadena_conexion_mongo = "mongodb+srv://kiaraalvamarinos:MFmiKqEHcNYcowC4@clustermongodb.7yxgk.mongodb.net/?retryWrites=true&w=majority&appName=ClusterMongoDB"

import requests
import sqlite3
from pymongo import MongoClient

####### API SUNAT ######
url = "https://api.apis.net.pe/v1/tipo-cambio-sunat"

def obtener_tipo_cambio():
    repuesta_solicitud = requests.get(url)
    data = repuesta_solicitud.json()
    return data['compra'], data['venta']
    

def almacenar_data_sqlite(fecha, compra, venta):
    conexion = sqlite3.connect('base_sunat_info.db')
    cursor = conexion.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sunat_info (
            fecha TEXT PRIMARY KEY,
            compra REAL,
            venta REAL
        )
    ''')


    cursor.execute('''
        INSERT OR REPLACE INTO sunat_info (fecha, compra, venta)
        VALUES (?, ?, ?)
    ''', (fecha, compra, venta))

    conexion.commit()
    conexion.close()

def almacenar_en_mongodb(fecha, compra, venta):
    cadena_conexion_mongo = "mongodb+srv://kiaraalvamarinos:MFmiKqEHcNYcowC4@clustermongodb.7yxgk.mongodb.net/?retryWrites=true&w=majority&appName=ClusterMongoDB"
    client = MongoClient(cadena_conexion_mongo)
    db = client['sunat_db']
    compilacion = db['sunat_info']

    
    compilacion.insert_one({
        "fecha": fecha,
        "compra": compra,
        "venta": venta
    })

    client.close()

def mostrar_datos_sqlite():
    conexion = sqlite3.connect('base_sunat_info.db')
    cursor = conexion.cursor()

    cursor.execute('SELECT * FROM sunat_info')
    registros = cursor.fetchall()

    for registro in registros:
        print(f"Fecha: {registro[0]}, Compra: {registro[1]}, Venta: {registro[2]}")

    conexion.close()


if __name__ == "__main__":
    compra, venta = obtener_tipo_cambio()

    if compra and venta:
        fecha_actual = "2024-10-09"  

        almacenar_data_sqlite(fecha_actual, compra, venta)

      
        almacenar_en_mongodb(fecha_actual, compra, venta)

        print("\nDatos almacenados en SQLite:")
        mostrar_datos_sqlite()
