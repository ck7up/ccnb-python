restart =0
while restart !=1:
    print("Entrez 3 nombres SVP : ")
    nbr1 = int(input("Entrez le 1er nombre = "))
    nbr2 = int(input("Entrez le 2eme nombre = "))
    nbr3 = int(input("Entrez le 3eme nombre = "))
    if nbr1 >= nbr2 and nbr1>=nbr3:
        nbr_max = nbr1
    elif nbr2 >= nbr3 and nbr2>=nbr1 :
        nbr_max = nbr2
    else:
        nbr_max = nbr3

    input("Appuyez sur ENTER pour afficher le plus grand des trois nombres.\n")
    print("Le maximum des 3 nombres est : \x1b[33;101;97m", nbr_max,"\x1b[0m""\n")
    input("\nMerci et à bientôt! ")
    #Copyright © | By Christian KALLA, Cyber Security 1 CCNB, Dieppe October 2019 |kallachristianovich@gmail.com | github : @ck7up