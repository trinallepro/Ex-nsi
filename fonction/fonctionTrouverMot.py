# La fonction permet de donner une chaine de carateres dont la longueur est egale a la taille de l'index

def mystere2(mot,indice):
    resultat = ""
    for i in range(indice):
        resultat = resultat+mot[i]
    return resultat

print(mystere2("coucou",4))