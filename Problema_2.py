import random
from pyfiglet import Figlet

def main():
    
    figlet = Figlet()

    fuente_figlets_admitidas = figlet.getFonts()

    fuente_figlet = input("Ingrese el nombre de una fuente (Presione Enter si desea una fuente aleatoria): ")

    if not fuente_figlet:
        fuente_figlet = random.choice(fuente_figlets_admitidas)
        print(f"Fuente aleatoria seleccionada: {fuente_figlet}")
    
    elif fuente_figlet not in fuente_figlets_admitidas:
        print("FUENTE no válida. Se seleccionará una fuente aleatoria.")
        fuente_figlet = random.choice(fuente_figlets_admitidas)
        print(f"Fuente aleatoria seleccionada: {fuente_figlet}")

    figlet.setFont(font=fuente_figlet)

    texto = input("Ingrese el texto a convertir en arte ASCII: ")

    resultado = figlet.renderText(texto)

    print(resultado)

if __name__ == "__main__":
    main()
