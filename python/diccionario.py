name = 'Earth'
moons = 1

jupiter_name = 'Jupiter'
jupiter_moons = 79

# Python usa llaves ({ }) y dos puntos (:) para indicar un diccionario. Puede crear un diccionario vacío y 
# agregar valores más adelante, o bien rellenarlo en el momento de la creación. Cada clave o valor está 
# separado por dos puntos y el nombre de cada clave se incluye entre comillas como un literal de cadena

planet = {
    'name': 'Earth',
    'moons': 1
}

# Puede leer valores dentro de un diccionario. Los objetos de diccionario tienen un método get que puede usar 
# para acceder a un valor mediante su clave. Si quiere imprimir name, puede usar el código siguiente:

print(planet.get('name'), planet['moons'])

# Displays Earth

planet.update({'name': 'Makemake'})

print(planet["name"])
# actualizar una variable en el diccionario: name es ahora Makemake

planet['name'] = 'Makemake'
print(planet["name"])
# name is now set to Makemake

# AGREGAR

planet['orbital period'] = 4333

# planet dictionary now contains: {
#   name: 'jupiter'
#   moons: 79
#   orbital period: 4333
# }

#BORRAR

planet.pop('orbital period')

# planet dictionary now contains: {
#   name: 'jupiter'
#   moons: 79
# }

# Agregar datos complejos

# Add address
planet['diameter (km)'] = {
    'polar': 133709,
    'equatorial': 142984
}

# planet dictionary now contains: {
#   name: 'Jupiter'
#   moons: 79
#   diameter (km): {
#      polar: 133709
#      equatorial: 142984
#   }
# }

print(f'{planet["name"]} polar diameter: {planet["diameter (km)"]["polar"]}')

# Output: Jupiter polar diameter: 133709