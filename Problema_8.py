import csv
import pymongo


cadena_conexion_mongo = "mongodb+srv://kiaraalvamarinos:MFmiKqEHcNYcowC4@clustermongodb.7yxgk.mongodb.net/?retryWrites=true&w=majority&appName=ClusterMongoDB"

def obtener_tipo_cambio(fecha):
    cliente = pymongo.MongoClient(cadena_conexion_mongo)
    db = cliente["ventas_db"]  
    coleccion = db["ventas_info"]  

    resultado = coleccion.find_one({"fecha": fecha})
    cliente.close()

    if resultado:
        return resultado["compra"], resultado["venta"]  
    else:
        return None, None  

def procesar_ventas():
    archivo_csv = '/workspaces/PythonPC4/ventas.csv'
    
    if not csvfile_exists(archivo_csv):
        print("Error: No se encontró el archivo 'ventas.csv'")
        return

    with open(archivo_csv, newline='') as csvfile:
        leer_csv = csv.reader(csvfile)
        next(leer_csv)  
        for fila in leer_csv:
            fecha_compra = fila[0]
            producto = fila[1]
            cant = fila[2]
            precio_por_unidad = fila[3]

            
            if not cant.isdigit() or not precio_por_unidad.replace('.', '', 1).isdigit():
                print(f"Error: Datos no válidos para el producto '{producto}'")
                continue  
            cantidad = int(cant)
            precio_unitario_dolares = float(precio_por_unidad)

            
            precio_total_dolares = precio_unitario_dolares * cantidad

            
            compra, venta = obtener_tipo_cambio(fecha_compra)

            if compra is not None:
               
                precio_total_soles = precio_total_dolares * compra

                
                print(f"Fecha: {fecha_compra}")
                print(f"Producto: {producto}")
                print(f"Cantidad: {cantidad}")
                print(f"Precio unitario en dólares: ${precio_unitario_dolares:.2f}")
                print(f"Precio total en dólares: ${precio_total_dolares:.2f}")
                print(f"Precio total en soles: S/{precio_total_soles:.2f}\n")
            else:
                print(f"No se encontró el tipo de cambio para la fecha {fecha_compra}")

def csvfile_exists(filepath):

    import os
    return os.path.isfile(filepath)


procesar_ventas()
