from math import sqrt
print("# Faire un programme qui demande à un utilisateur d'entrer les 3 coefficients d'un équation quadratique, soient a, b, c. => y = ax^2 + bx + c #")

run = 0
while run != 1:
    a = float(input("Entrez la valeur de a = "))
    b = float(input("Entrez la valeur de b = "))
    c = float(input("Entrez la valeur de c = "))
    input(">>> Toutes les valeurs sont entrées, appuyez sur ENTER pour calculer le DÉTERMINANT D = (b**2)-(4*a*c)...\n")

    det = float((b**2)-(4*a*c))
    print("DETERMINANT est D =",det)
    if det < 0 :
        print("Il n'existe pas de solution.\n")

    elif det == 0 :
        print("Il existe une solution double qui est : X2=X1=X2.")
        input(">>> Presser Enter pour effectuer le calcul de X=X1=X2...")
        X=-b/(2*a)
        print("X =",X,"\n")

    elif det > 0 :
        print("Il existe deux solutions X1 et X2.\n")
        input(">>> Presser Enter pour effectuer le calcul de X1...")
        X1 = (-b + sqrt(det))/(2*a)
        print("X1 =",X1,"\n")

        input(">>> Presser Enter pour effectuer le calcul de X2...")
        X2 = (-b - sqrt(det))/(2*a)
        print("X1 =",X2,"\n")

    input("Presser '0' ensuite ENTER pour recommencer le calcul : ")
