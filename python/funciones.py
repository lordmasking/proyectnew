def rocket_parts():
    print("payload, propellant, structure")
rocket_parts()

output = rocket_parts()
#payload, propellant, structure
output is None


def rocket_parts():
    return "payload, propellant, structure"

output = rocket_parts()
print(output)


def distance_from_earth(destination):
    destination = input("tierra o luna?")
    if destination == "Moon":
        return "238,855"
    else:
        return "Unable to compute to that destination"

print(distance_from_earth("destination"))

def dias_completos(distancia, velocidad):
    distancia = int(input("ingrese distancia"))
    velocidad = int(input("ingrese velocidad en km/h"))
    horas = distancia/velocidad
    return horas/24
pass

print(f"faltan", dias_completos("distancia","velocidad"), "para completar el viaje")



