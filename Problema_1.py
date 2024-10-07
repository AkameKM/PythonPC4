import requests

def api_precio_bitcoin():
    
    try:
        url = "https://api.coindesk.com/v1/bpi/currentprice.json"
        
        resultado = requests.get(url)
        resultado.raise_for_status()  

        cambio_bitcoin = resultado.json()

        precio_bitcoin_usd = cambio_bitcoin['bpi']['USD']['rate_float']
        return precio_bitcoin_usd

    except requests.RequestException as e:
        print("Error al conectar con la API:", e)
        return None

def calcular_valor_bitcoins(n, precio_bitcoin):

    return n * precio_bitcoin

def main():
    try:

        n = float(input("Ingrese la cantidad de bitcoins que tiene: "))

        precio_bitcoin = api_precio_bitcoin()

        if precio_bitcoin is not None:

            valor_total = calcular_valor_bitcoins(n, precio_bitcoin)

            print(f"El valor de {n} bitcoins es: ${valor_total:,.4f} USD")

    except ValueError:
        print("Por favor ingrese un número válido.")

if __name__ == "__main__":
    main()
