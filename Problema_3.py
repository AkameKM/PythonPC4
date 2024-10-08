import requests
import zipfile
import os

def descargar_imagen(url, imagen_guardada):
    try:
        repuesta_solicitud = requests.get(url)
        repuesta_solicitud.raise_for_status()  
        
        with open(imagen_guardada, 'wb') as imagen:
            imagen.write(repuesta_solicitud.content)
        print(f"Se descargo y guardo la imagen como {imagen_guardada}")
    except requests.RequestException as e:
        print(f"Error al descargar la imagen: {e}")

def creacion_archivo_zip(imagen_descargada, archivo_zip):
    try:
        with zipfile.ZipFile(archivo_zip, 'w') as zipf:
            zipf.write(imagen_descargada)
        print(f"La imagen {imagen_descargada} se zipeo como {archivo_zip}")
    except Exception as e:
        print(f"Error al crear el archivo zip: {e}")

def extracion_archivo_zip(archivo_zip, ruta_destino):
    try:
        with zipfile.ZipFile(archivo_zip, 'r') as zipf:
            zipf.extractall(ruta_destino)
        print(f"Archivo {archivo_zip} extraído en {ruta_destino}")
    except Exception as e:
        print(f"Error al extraer el archivo zip: {e}")

def main():
    url_imagen = "https://i.pinimg.com/736x/63/c4/f5/63c4f5a5ad175f209fe1843319e992b7.jpg"
    imagen_descargada = "imagen_descargada.jpg"
    archivo_zip = "imagen_comprimida.zip"
    ruta_extraccion = "imagen_extraida"
    
    
    descargar_imagen(url_imagen, imagen_descargada)
    
    creacion_archivo_zip(imagen_descargada, archivo_zip)
    
    if not os.path.exists(ruta_extraccion):
        os.makedirs(ruta_extraccion)
    extracion_archivo_zip(archivo_zip, ruta_extraccion)

if __name__ == "__main__":
    main()
