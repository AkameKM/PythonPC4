# /workspaces/PythonPC4/archivo_para_problema_6.py   ------- ruta de prueba para contar las lineas 

def contar_lineas(ruta_archivo):

    if not ruta_archivo.endswith('.py'):
        print("El archivo debe terminar en .py")
        return

    try:
        
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()

        cant_lineas_codigo = 0
        for linea in lineas:
            
            eliminar_espacio_lineas = linea.strip()
            
            if eliminar_espacio_lineas and not eliminar_espacio_lineas.startswith("#"):
                cant_lineas_codigo += 1

        print(f"Número de líneas de código: {cant_lineas_codigo}")

    except FileNotFoundError:
        print("El archivo no fue encontrado. Verifique la ruta.")
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")

ruta = input("Ingrese la ruta del archivo .py: ")
contar_lineas(ruta)
