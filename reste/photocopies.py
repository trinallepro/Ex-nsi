nbPhotocopies = float(input("Vueillez rentrer le nombre de photocopies que vous souhitez : "))
prix = float(0)
if nbPhotocopies > 50 :
    nbPhotocopies -= 50
    prix = nbPhotocopies * 0.06
    prix += 4
    print("Voici votre prix : ",prix)
else:
    prix = nbPhotocopies * 0.08
    print("Voici votre prix : ",prix)