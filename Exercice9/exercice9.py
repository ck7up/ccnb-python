def Introduction():
    print("\x1b[33;103;30m" + "\n ****************************************** ")
    print(" *           Calcul du Plus Grand         * ")
    print(" * Commun Diviseur (pgcd) de deux nombres * ")
    print(" ****************************************** \n" + "\x1b[0m")

def InputNumb1():
    numb1=int(input("Entrer 1er nombre entier : "))
    return numb1

def InputNumb2():
    numb2=int(input("Entrer 2eme nombre entier : "))
    return numb2

def calculPgcd(numb1, numb2):
    while numb2 != 0:
            restDiv = numb1 % numb2
            numb1 = numb2
            numb2 = restDiv
    print(numb1,"est le plus grand commun diviseur (pgcd)\n")
    return numb1

    while numb1 != 0:
            restDiv = numb2 % numb1
            numb2 = numb1
            numb1 = restDiv
    print(numb2,"est le plus grand commun diviseur (pgcd)\n")
    return numb2

def main ():
    Introduction()
    numb1=InputNumb1()
    numb2=InputNumb2()
    calculPgcd(numb1, numb2)
    # affchResult(numb1, numb2)
main()
#Copyright © | By Christian KALLA, Cyber Security 1 CCNB, Dieppe October 2019 |kallachristianovich@gmail.com | github : @ck7up