argent = int(input("argent = "))
nb = int(0)
while argent <= 500 :
    argent *= 1.05
    nb += 1
    print("--------------------------------")
    print("| années ",nb, " argent =", round(argent, 2),"|")
print("--------------------------------")



