def ok():
    nb = float(input("nb = "))
    if nb == 49:
        print("gagné")
        exit()
    elif nb > 49:
        print("trop grand")
        ok()
    elif nb < 49:
        print("trop petit")
        ok()
    else:
        ok()


ok()

