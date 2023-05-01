gr = 0
ra = 0
hu = 0
sl = 0

print ("Te gusta amanecer o oscuridad?")
q1 = int(input("1) Amanecer \n2) Oscuridad "))
if q1 == 1:
  gr += 1
  ra += 1
elif q1 == 2:
  hu += 1
  sl += 1
else:
  print("Entrada incorrecta")
  pass

print("Cuando este muerto, quiero que la gente me recuerde como:")
q2 = int(input("1) El Bien \n2) El Grande \n3) El Sabio \n4) El audaz "))
if q2 == 1:
  hu += 2
elif q2 == 2:
  sl += 2
elif q2 == 3:
  ra += 2
elif q2 == 4:
  gr += 2
else:
  print("Entrada incorrecta")
  pass

print("Que tipo de intrumento agrada mas a tu aido?")
q3 = int(input("1) The violin \n2) The trumpet \n3) The piano \n4) The drum "))
if q3 == 1:
  sl += 4
elif q3 == 2:
  hu += 4
elif q3 == 3:
  ra += 4
elif q3 == 4:
  gr += 4
else:
  print("Entrada incorrecta")

if gr > ra and gr > hu and gr > sl:
  print("Gryffindor")
elif ra > gr and ra > hu and ra > sl:
  print("Ravenclaw")
elif hu > gr and hu > ra and hu > sl:
  print("Hufflepuff")
elif sl > gr and sl > ra and sl > hu:
  print("Slytherin")
else:
  pass


print(gr, ra, hu, sl)

