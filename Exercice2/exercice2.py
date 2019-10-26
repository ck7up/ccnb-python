DistInput = input("Entrer une distance en Km :")
distance =  float(DistInput)
TimeInput = input("Entrer le temps en heure :")
temps = int(TimeInput)
vit_kmh = distance/temps
vit_mph = (0.621371*distance)/temps
vit_ms = (distance*1000)/(temps*3600)

print("Votre vitesse en km est de :" + str( vit_kmh) + " Km/h" )
input("Appuyez sur la touche ENTREE pour Afficher votre vitesse en MPH ... :)" )

print("Votre vitesse en mph est de :" + str(vit_mph) + " mph" )
input("Appuyez sur la touche ENTREE pour Afficher votre vitesse en M/S ... :)" )

print("Votre vitesse en m/s est de :" + str(vit_ms) + " m/s" )
input("Merci et bonne ROUTE!" )