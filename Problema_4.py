import csv

def leer_temperaturas(nombre_archivo):
    temperaturas = []
    
    try:
       
        with open(nombre_archivo, newline='', encoding='utf-8') as archivo:
            leer_csv = csv.reader(archivo)
            for fila in leer_csv:
                try:
                
                    temperatura = float(fila[1])
                    temperaturas.append(temperatura)
                except ValueError:
                    print(f"Error al convertir temperatura: {fila[1]}")
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no se encuentra.")

    return temperaturas

def calcular_estadisticas(temperaturas):
    if not temperaturas:
        return None, None, None
    
    temperatura_promedio = sum(temperaturas) / len(temperaturas)
    temperatura_maxima = max(temperaturas)
    temperatura_minima = min(temperaturas)
    
    return temperatura_promedio, temperatura_maxima, temperatura_minima

def escribir_resumen(nombre_archivo, promedio, maxima, minima):
    try:
        
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            archivo.write(f"Temperatura promedio: {promedio:.2f}°C\n")
            archivo.write(f"Temperatura máxima: {maxima:.2f}°C\n")
            archivo.write(f"Temperatura mínima: {minima:.2f}°C\n")
        print(f"Resumen escrito en {nombre_archivo}")
    except Exception as e:
        print(f"Ocurrió un error al escribir el archivo: {e}")

def main():
    archivo_temperaturas = "temperaturas.txt"
    archivo_resumen = "resumen_temperaturas.txt"
    
    temperaturas = leer_temperaturas(archivo_temperaturas)
    
    promedio, maxima, minima = calcular_estadisticas(temperaturas)
    
    if promedio is not None:

        escribir_resumen(archivo_resumen, promedio, maxima, minima)
    else:
        print("No se pudieron calcular estadísticas debido a datos insuficientes.")

if __name__ == "__main__":
    main()