user_input = ''
inputs = []
while user_input.lower() != 'done':
    if user_input:
        inputs.append(user_input)
    #observamos que al colocar un if comple el ciclo de agregar a una lista
    user_input = input('Enter a new value, or done when done')

print(inputs)
#se observa que no es necesario colocar un imput al inicio para ingresar el dato de comprobacion hacia la cadena directamente
#directamente podemos colocar la comprobacion entra al bucle y dentro realizamos lo que queremos

