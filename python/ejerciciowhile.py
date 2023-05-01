new_planet = ''
planets = []

while new_planet.lower() != "hecho":
    if new_planet:
        planets.append(new_planet)
    new_planet = input("ingrese un planeta, si ya nombro todos los planetas escriba hecho")

for planet in planets:
    print(planet)


