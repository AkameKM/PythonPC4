#### EXCEPCIONES ######
number_one,  number_two = 5, "1"
# Try except
try:
    print(number_one + number_two)
    #print("No se ha producido error")
except:
    # Se ejecuta si se produce una excepción
    print("Se ha producido un error ")

# Try except else 

try:
    print(number_one + number_two)
    #print("No se ha producido error")
except:
    print("Se ha producido un error ")
else: # Opcional 
    #Esto se ejecuta si no se produce una excepcion
    print("La ejecución continua correctamente")

# Try except else finally

try:
    print(5 + 8)
    print("No se ha producido error")
except:
    print("Se ha producido un error ")
else: # Opcional
    #Esto se ejecuta si no se produce una excepcion
    print("La ejecución continua correctamente")
finally: # Opcional
    # Se ejecuta siempre
    print("La ejecución continúa")

# Excepciones por tipo

try:
    print(number_one + number_two)
    #print("No se ha producido error")
# se va a ejecutar cuando se produzca erros de tipo typeerror
except TypeError: 
    print("Se ha producido un error TypeError ")

#try:
   # print(number_one + number_two)
    #print("No se ha producido error")
# Se va a ejcutar cuando se produzca erros tipo valueerror
#except ValueError:  #
   # print("Se ha producido un error ")

try:
    print(number_one + number_two)

except ValueError:  
    print("Se ha producido un error tipo ValueError")
except TypeError:
    print("Se produce un error tipo TypeError")

try:
    print(number_one + number_two)

except TypeError as errornombrequeseledaalavariable:  # con el as capturo el error
    print(errornombrequeseledaalavariable)


#Si el error que se produce no es value se va por Exception
try:
    print(number_one + number_two)
except ValueError as my_error:  
    print(my_error)
except Exception as error :
    print(error)
