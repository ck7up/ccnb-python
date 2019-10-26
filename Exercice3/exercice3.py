tempInput = input("Entrer la température de votre corps en Celsius : ")
print("Votre température est de : " + tempInput + "°C")

k= 9/5
TempInput = float(tempInput)
temp_F = (TempInput*k) + 32
temp_K = TempInput + 273.15 

input("Appuyez sur la touche ENTREE pour Afficher votre température en Fahrenheit ... ;)")
print("Votre température en Fahrenheit est de : " + str(temp_F) + "°F")

input("Appuyez sur la touche ENTREE pour Afficher votre température en Kelvin ... :P")
print("Votre température en Kelvin est de : " + str(temp_K) + "°K")

input("Au revoir et à bientôt !" )


