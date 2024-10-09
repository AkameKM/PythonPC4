
def crear_tabla_multiplicar(n):
    archivo_tabla = f"tabla-{n}.txt"
    with open(archivo_tabla, "w") as archivo:
        for i in range(1, 11):
            archivo.write(f"{n} x {i} = {n * i}\n")
    print(f"Tabla de multiplicar del {n} guardada en {archivo_tabla}")

def leer_tabla(n):
    archivo_tabla = f"tabla-{n}.txt"
    try:
        with open(archivo_tabla, "r") as archivo:
            print(f"Mostrando la tabla de multiplicar del {n}:")
            print(archivo.read())
    except FileNotFoundError:
        print(f"El archivo de la tabla de multiplicar {archivo_tabla} no existe.")

def leer_fichero(n, m):
    archivo_tabla = f"tabla-{n}.txt"
    try:
        with open(archivo_tabla, "r") as archivo:
            fichero = archivo.readlines()
            if 1 <= m <= 10:
                print(f"Línea {m} de la tabla de multiplicar del {n}: {fichero[m-1]}")
            else:
                print("El valor de m debe estar entre 1 al 10.")
    except FileNotFoundError:
        print(f"El archivo {archivo_tabla} no existe.")

def menu():
    while True:
        print("\nMenú:")
        print("1. Crear tabla de multiplicar")
        print("2. Leer tabla de multiplicar")
        print("3. Leer una línea del fichero dentro de la tabla de multiplicar")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            n = int(input("Ingrese un número entre 1 al 10: "))
            if 1 <= n <= 10:
                crear_tabla_multiplicar(n)
            else:
                print("Número fuera de rango.")
        
        elif opcion == "2":
            n = int(input("Ingrese un número de la tabla de multiplicar que desea leer: "))
            if 1 <= n <= 10:
                leer_tabla(n)
            else:
                print("Número fuera de rango.")
        
        elif opcion == "3":
            n = int(input("Ingrese el numero de la tabla: "))
            m = int(input(f"Ingrese el número que desea leer del fichero {n}: "))
            if 1 <= n <= 10 and 1 <= m <= 10:
                leer_fichero(n, m)
            else:
                print("Los números deben estar entre 1 al 10.")
        
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el menú
if __name__ == "__main__":
    menu()
