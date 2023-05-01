planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
print("The first planet is", planets[0])
print("The second planet is", planets[1])
print("The third planet is", planets[2])

planets[3] = "Red Planet"
print("Mars is also known as", planets[3])

number_of_planets = len(planets) #len sirve para contar las variables que tenga la cadena
print("There are", number_of_planets, "planets in the solar system.")

planets.append("Pluto") #Para agregar un elemento a una lista, use el método .append(value)
number_of_planets = len(planets)
print("There are actually", number_of_planets, "planets in the solar system.")

planets.pop()  # Puede quitar el último elemento de una lista llamando al método .pop()
number_of_planets = len(planets)
print("No, there are definitely", number_of_planets, "planets in the solar system.")

jupiter_index = planets.index("Jupiter") # Para determinar dónde se almacena un valor en una lista, use el método index de la lista.
print("Jupiter is the", jupiter_index + 1, "planet from the sun")


