# la fonction trouve si un nombre(nombre) est present dans une liste(liste)

def mystere3(liste,nombre):
    for element in liste:
        if element == nombre:
            return "trouvé"
    return "Pas trouvé"

print(mystere3(liste=[1,5],nombre=5))