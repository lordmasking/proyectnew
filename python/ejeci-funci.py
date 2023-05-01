def generate_report(main_tank, external_tank, hydrogen_tank):
    output = f"""Fuel Report:
    Main tank: {main_tank}
    External tank: {external_tank}
    Hydrogen tank: {hydrogen_tank} 
    """
    print(output)

generate_report(80, 70, 75)

from datetime import timedelta, datetime

def arrival_time(hours=0):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime("Arrival: %A %H:%M")

arrival_time()

def arrival_time(destination, hours=0):
    destination = "Moon"
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime(f"{destination} Arrival: %A %H:%M")

arrival_time("destination", hours=51)

def variable_length(*args):
    print(args)

variable_length("one", "two")

def sequence_time(*args):
    total_minutes = sum(args)
    if total_minutes < 60:
        return f"Total time to launch is {total_minutes} minutes"
    else:
        return f"Total time to launch is {total_minutes/60} hours"

sequence_time(40,10,20)


def variable_length(**kwargs):
    print(kwargs)

variable_length(tanks=1, day="Wednesday", pilots=3)

def crew_members(**kwargs):
    print(f"{len(kwargs)} astronauts assigned for this mission:")
    for title, name in kwargs.items():
        print(f"{title}: {name}")

crew_members(captain="Neil Armstrong", pilot="Buzz Aldrin", command_pilot="Michael Collins")

def report_combus(**tanque_ful):
    for name, value in tanque_ful.items():
        print(f"{name}: {value}")

report_combus(main = 50,
external = 100,
emergency = 60)

