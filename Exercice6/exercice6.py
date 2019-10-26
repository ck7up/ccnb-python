print("\nExercice #6 \n")
print("Faire un programme qui permet de déterminer les résultats du jeux Rock/Paper/Scissors/Lizard/Spock \n")
print("\x1b[33;107;91m" + " Menu : Entrer ..." + "\x1b[0m")
game = "pour joueur,"
print("\x1b[33;103;30m" + " p "+str(game)+" Paper " + "\x1b[0m")
print("\x1b[33;104;30m" + " r "+str(game)+" Rock " + "\x1b[0m")
print("\x1b[33;42;30m" + " l "+str(game)+" Lizard " + "\x1b[0m")
print("\x1b[33;105;30m" + " sp "+str(game)+" Spock " + "\x1b[0m")
print("\x1b[33;106;30m" + " sc "+str(game)+" Scissors " + "\x1b[0m""\n")

joueur1 = input("Entrer le nom du premier joueur : ")
joueur2 = input("Entrer le nom du deuxième joueur : ")
#joueur1.lower()
#joueur2.lower()
replay = 0
#Boucle pour repeter le jeu avec les memes joueurs
while replay!=1:
    print("\nBonjour",joueur1,"!")
    play_j1 = input("Pour jouer, entrez votre choix (r,p,sc,l,sp) selon le menu : ")
    print("\nBonjour",joueur2,"!")
    play_j2 = input("Pour jouer, entrez votre choix (r,p,sc,l,sp) selon le menu : ")

    r = "ROCK"
    p = "PAPER"
    sc = "SCISSORS"
    l = "LIZARD"
    sp = "SPOCK"

    #Egalite (couleur ( "\x1b[29;42m" + "text" + "\x1b[0m" ))
    if play_j1 == play_j2:
        print("\x1b[33;101;97m" + "\n  >> C'est intéressant,", joueur1, "et",joueur2, "sont à égalité :) Récommencez!  " + "\x1b[0m")

    #Paper Win
    if play_j1=='p' and play_j2=='r':
        print("\x1b[33;93m" + ">>", joueur1, "gagne car le " +str(p) + " emballe le "+str(r)+" Bravo!" + "\x1b[0m")
    elif play_j1=='p' and play_j2=='sp':
        print("\x1b[33;93m" + ">>", joueur1, "gagne car le " +str(p) + " refute "+str(sp) + " Bravo!" + "\x1b[0m")
    #Paper Lose
    elif play_j1=='p' and play_j2=='sc':
        print("\x1b[33;96m" + ">>", joueur1, "à perdu car les "+str(sc) +" coupent le "+str(p)+". "+str(joueur2)+" gagne, Bravo " +str(joueur2)+"!" + "\x1b[0m")
    elif play_j1=='p' and play_j2=='l':
        print("\x1b[33;32m" + ">>", joueur1, "à perdu car les "+str(sc) + " décapitent le " + str(l)+". "+str(joueur2)+" gagne, Bravo " + str(joueur2)+"!" + "\x1b[0m")

    #Rock win
    if play_j1=='r' and play_j2=='sc':
        print("\x1b[33;94m" + ">>", joueur1, "gagne car le " +str(r)+" écrase les " + str(sc)+", Bravo!" + "\x1b[0m")
    elif play_j1=='r' and play_j2=='l':
        print("\x1b[33;94m" + ">>", joueur1, "gagne car le " +str(r)+" écrase les " + str(sc)+", Bravo!" + "\x1b[0m")
    #Rock lose
    if play_j1 == 'r' and play_j2 == 'sp':
        print("\x1b[33;95m" + ">>", joueur1, "à perdu car " + str(sp) + " vaporise le " + str(r)+". " + str(joueur2)+" gagne, Bravo "+str(joueur2)+"!" + "\x1b[0m")
    elif play_j1 == 'r' and play_j2 == 'p':
        print("\x1b[33;93m" + ">>", joueur1, "à perdu car le " + str(p) + " emballe le " + str(r)+". " + str(joueur2)+" gagne, Bravo "+str(joueur2)+"!" + "\x1b[0m")

    #Lezard win
    if play_j1 == 'l' and play_j2 == 'p':
        print("\x1b[33;32m" + ">>", joueur1, "gagne car le " +str(l)+" mange le "+str(p)+", Bravo!" + "\x1b[0m")
    elif play_j1 == 'l' and play_j2 == 'sp':
        print("\x1b[33;32m" + ">>", joueur1, "gagne car le " +str(l)+" empoisonne "+str(sp)+", Sorry!" + "\x1b[0m")
    #Lezard lose
    if play_j1 == 'l' and play_j2 == 'sc':
        print("\x1b[33;94m" + ">>", joueur1, "à perdu car le " + str(r) + " casse les " + str(sp)+". " +str(joueur2)+" gagne, Bravo "+str(joueur2)+"!" + "\x1b[0m")
    elif play_j1 == 'l' and play_j2 == 'p':
        print("\x1b[33;96m" + ">>", joueur1, "à perdu car le " + str(r) + " casse les " + str(sc)+". " +str(joueur2)+" gagne, Bravo "+str(joueur2)+"!" + "\x1b[0m")

    #Spock win
    if play_j1 == 'sp' and play_j2 == 'r':
        print("\x1b[33;95m" + ">>", joueur1, "gagne car " +str(sp)+" pulverise le "+str(r)+", Bravo!" + "\x1b[0m")
    elif play_j1 == 'sp' and play_j2 == 'sc':
        print("\x1b[33;95m" + ">>", joueur1, "gagne car " +str(sp)+" fracasse les "+str(sc)+", Bravo!" + "\x1b[0m")
    #Spock lose
    if play_j1 == 'sp' and play_j2 == 'p':
        print("\x1b[33;93m" + ">>", joueur1, "à perdu car le " + str(p) + " réfute " + str(sp)+". " + str(joueur2)+" gagne, Bravo "+str(joueur2)+"!" + "\x1b[0m")
    elif play_j1 == 'sp' and play_j2 == 'l':
        print("\x1b[33;32m" + ">>", joueur1, "à perdu car le " + str(l) + " empoisonne " + str(sp)+". " + str(joueur2)+" gagne, Bravo "+str(joueur2)+"!" + "\x1b[0m")

    #Scissors win
    if play_j1 == 'sc' and play_j2 == 'p':
        print("\x1b[33;96m" + ">>", joueur1, "gagne car les" +str(sc)+" coupent le "+str(p)+", Bravo!" + "\x1b[0m")
    elif play_j1 == 'sc' and play_j2 == 'l':
        print("\x1b[33;96m" + ">>", joueur1, "gagne car les " + str(sc)+" décapitent le "+str(l)+", Bravo!" + "\x1b[0m")
    #Scissors lose
    if play_j1 == 'sc' and play_j2 == 'sp':
        print("\x1b[33;95m" + ">>", joueur1, "à perdu car " + str(sp) + " fracasse " + str(sc)+". " + str(joueur2)+" gagne, Bravo "+str(joueur2)+"!" + "\x1b[0m")
    elif play_j1 == 'sc' and play_j2 == 'r':
        print("\x1b[33;94m" + ">>", joueur1, "à perdu car " + str(r) + " écrase les " + str(sc)+". " + str(joueur2)+" gagne, Bravo "+str(joueur2)+"!" + "\x1b[0m")
    else :
        play_j1 or play_j2 !=[r,p,sc,l,sp]
        print("\n \x1b[33;101;93m " + " /!\ Attention! Vous avez entré ", play_j1, " et/ou ", play_j2, ", choix qui ne fait pas partie du menu.\n       Entrer un des choix du menu('p', 'r', 'l', 'sp' ou alors 'sc') pour joueur""\x1b[0m")

#Copyright © | By Christian KALLA, Cyber Security 1 CCNB, Dieppe October 2019 |kallachristianovich@gmail.com | github : @ck7up