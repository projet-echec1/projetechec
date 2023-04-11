def jouer(self):
    print("Bienvenue au jeu d'échecs!")
    while self.echec_et_mat() is False:
        print(self.echiquier)
def deroulement():

    if self.tour=='blanc':
        print("C'est au tour des blancs")
        depart=self.choixpiece()
        arrivee=self.choixmouvement()
        if self.coup_legal()==True:
            self.deplacer_piece(depart, arrivee)
            self.sauvegarder_etat_echiquier()
            self.changement_tour()
            print("C'est au tour des noirs")
            if self.echec():
                print("Vous êtes en échec")
        else:
            print("Coup impossible, veuillez rejouez")
            self.deroulement()

    else:
        print("C'est au tour des noirs")
        depart=self.choixpiece()
        arrivee=self.choixmouvement()
        if self.coup_legal()==True:
            self.deplacer_piece(depart, arrivee)
            self.sauvegarder_etat_echiquier()
            self.changement_tour()
            print("C'est au tour des blancs")
            if self.echec():
                print("Vous êtes en échec")
        else:
            print("Coup impossible, veuillez rejouez")
            self.deroulement()
        


        if echec_et_mat():
            print("C'est finito pour toi, révise tes leçons")



#ATTENTION: à finir 







