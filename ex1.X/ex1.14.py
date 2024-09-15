def ok():
    nb = float(input("nb = "))
    if nb == 9:
        print("vous avez gagné!!")
        exit()
    else:
        ok()


ok()
