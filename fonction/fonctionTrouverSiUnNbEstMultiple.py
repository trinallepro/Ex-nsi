def est_multiple(nombre, diviseur):
    nb = nombre / diviseur
    if nombre % diviseur > 0:
        print(nombre,"n'est pas un multible de", diviseur)
        return False
    else:
        print(nombre,"est un multiple de", diviseur)
        return True


print(est_multiple(10, 5))
