note = float(input("votre derniere note de francais :"))

if note < 10 :
    print("pas terrible")
elif note < 14 :
    print("pas mal")
elif note > 20 :
    print("error")
else :
    print("bon travail")