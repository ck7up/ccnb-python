def Introduction():
    print("\x1b[33;103;30m" + "\n ************************************ ")
    print(" *            CONVERTISSEUR         * ")
    print(" *       DECIMAL -> HEXADECIMAL     * ")
    print(" ************************************ \n" + "\x1b[0m")

def SaisieDesDonnees():
    numDec = int(input("Entrez un nombre entier : "))
    # if numDec == 0:
    #     print("lol")
    # else:
    return numDec

def Traitement(numDec):
    if numDec == 0:
        print("\nLe nombre binaire de", numDec, "est: ""\x1b[33;103;30m" + "", numDec,"" + "\x1b[0m""\n")
    else:
        DecToBin = ""
        while numDec != 0:
            quotDiv = numDec // 2
            restDiv = numDec % 2
            DecToBin = str(restDiv) + DecToBin
            numDec = quotDiv
        return DecToBin
def AffichResult(numDec, DecToBin):
    if numDec != 0:
        print("\nLe nombre binaire de ""\x1b[103;30m" + "", numDec, "" + "\x1b[0m"" est: ""\x1b[42;30m" + "", DecToBin, "" + "\x1b[0m""\n")

def restart():
    while 1:
        restart = input("\nVoulez-vous recommencer? (O-Oui ou Y-Yes) ")
        #restart == restart.upper()
        #Si on entre un valeur presente dans la liste ci-dessous, le programme recommence
        if restart in ["y","o","Y","O"]:
            main()
        # Si on rentre une valeur presente dans la liste suivante, le programme s'arrete
        elif restart in ["n","N","no","NO"]:
            print("\n\x1b[33;42;30m"+"Aurevoir et a bientot!" + "\x1b[0m\n ")
            break
        else :
        #Si l'utilisateur n'entre pas une des valeurs presente dans la liste ci-dessous, il recoit un message lui demandant d'entrer une des valeur presente sur la liste (soit oui ou non)
            restart != ["y", "o", "Y", "O", "n", "N", "no", "NO"]
            print("\x1b[33;41;97m" + "/!\ Attention ! Entrer 'O' pour 'Oui' ou 'N' pour 'Non' "+ "\x1b[0m")

def main():
    Introduction()
    numDec = SaisieDesDonnees()
    DecToBin = Traitement(numDec)
    AffichResult(numDec, DecToBin)
    restart()
main()
#Copyright © | By Christian KALLA, Cyber Security 1 CCNB, Dieppe October 2019 |kallachristianovich@gmail.com | github : @ck7up