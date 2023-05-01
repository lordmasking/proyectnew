gravity_on_earth = 1.0
gravity_on_the_moon = 0.166
gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]
bus_weight = 12650

print("En mercurio el autobus pesa", bus_weight * gravity_on_planets[0], "kg")

# Python tiene funciones integradas para calcular los números más grandes y más 
# pequeños de una lista. La función max() devuelve el número más grande y min() 
# devuelve el más pequeño. Por lo tanto, min(gravity_on_planets) devuelve el número
# más pequeño de la lista gravity_on_planets.
print("On Earth, a double-decker bus weighs", bus_weight, "kg")
print("The lightest a bus would be in the solar system is", bus_weight * min(gravity_on_planets), "kg")
print("The heaviest a bus would be in the solar system is", bus_weight * max(gravity_on_planets), "kg")

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planets_before_earth = planets[0:5] # el ":" indica el desde izquierda, hasta derecha
print(planets_before_earth)

# Una segmentación crea una lista nueva. No modifica la lista actual.
planets_after_earth = planets[3:]
print(planets_after_earth)

# Para unir dos listas, debe usar el otro operador (+) con dos listas para devolver una nueva
amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"]
galilean_moons = ["Io", "Europa", "Ganymede", "Callisto"]

regular_satellite_moons = amalthea_group + galilean_moons
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

regular_satellite_moons.sort() # ordenará una lista de cadenas en orden alfabético y una lista de números en orden numérico
# al revez se coloca .sort(reverse=true)
print(regular_satellite_moons)



