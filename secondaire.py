#fonction qui détermine si une pièce est capturable lors d'un mouvement: 



def est_capturable(echiquier, depart, arrivee):
    piece_depart = echiquier[depart[0]][depart[1]]
    piece_arrivee = echiquier[arrivee[0]][arrivee[1]]
    if piece_arrivee is None:
        return False
    elif piece_depart.couleur != piece_arrivee.couleur:
        return True
    else:
        return False
        
def capture_piece(self, position):
    piece = self.obtenir_piece(position)
    if piece is None:
        return "Aucune pièce à cette position"
    else:
        self.echiquier[position[0]][position[1]] = None
        return "La pièce a été capturée avec succès"


#pour mettre à jour le jeu:

def mettre_a_jour_jeu(self, position_depart, position_arrivee):
    piece_depart = self.obtenir_piece(position_depart)
    piece_arrivee = self.obtenir_piece(position_arrivee)
    
    # Vérifier si la case d'arrivée est vide ou si la pièce sur la case d'arrivée est de couleur différente
    if piece_arrivee is None or piece_arrivee.couleur != piece_depart.couleur:
        # Vérifier si le déplacement est autorisé pour la pièce
        if position_arrivee in self.piecemouvementpossible(position_depart):
            # Déplacer la pièce
            self.echiquier[position_depart[0]][position_depart[1]] = None
            self.echiquier[position_arrivee[0]][position_arrivee[1]] = piece_depart
            
            # Capturer la pièce si nécessaire
            if piece_arrivee is not None:
                # Ajouter la pièce capturée à la liste des pièces capturées du joueur adverse
                if piece_arrivee.couleur == 'blanc':
                    self.piece_capturee_noir.append(piece_arrivee)
                else:
                    self.piece_capturee_blanc.append(piece_arrivee)
            
            # Changer le tour du joueur
            if self.tour == 'blanc':
                self.tour = 'noir'
            else:
                self.tour = 'blanc'
                
            print("Déplacement effectué avec succès !")
        else:
            print("Déplacement non autorisé pour cette pièce !")
    else:
        print("Impossible de capturer une pièce de même couleur !")









#ENREGISTER L'ÉTAT DE L'ÉCHIQUIER

def sauvegarder_etat_echiquier(echiquier):
    etat_echiquier = []

    for ligne in echiquier:
        ligne_echiquier = []
        for piece in ligne:
            if piece:
                ligne_echiquier.append((piece.couleur, piece.symbole))
            else:
                ligne_echiquier.append(None)
        etat_echiquier.append(ligne_echiquier)

    return etat_echiquier


#EXEMPLE:

def sauvegarder_etat_echiquier(echiquier):
    etat_echiquier = []

    for ligne in echiquier:
        ligne_echiquier = []
        for piece in ligne:
            if piece:
                ligne_echiquier.append((piece.couleur, piece.symbole))
            else:
                ligne_echiquier.append(None)
        etat_echiquier.append(ligne_echiquier)

    return etat_echiquier

#coup legal

def est_coup_legal(self, depart, arrivee):
        piece_depart = self.obtenir_piece(depart)
        piece_arrivee = self.obtenir_piece(arrivee)
        if piece_depart is None:
            return False
        if piece_arrivee is not None and piece_arrivee.couleur == pieceif piece_depart.couleur != self.tour:
        return False
    if depart == arrivee:
        return False
    if piece_arrivee is not None and piece_depart.couleur == piece_arrivee.couleur:
        return False

    # Vérification des déplacements spécifiques de chaque pièce
    if piece_depart.symbole == 'P':
        if piece_depart.couleur == 'blanc':
            if depart[1] == arrivee[1] and self.obtenir_piece(arrivee) is None:
                if arrivee[0] == depart[0] + 1:
                    return True
                if arrivee[0] == depart[0] + 2 and depart[0] == 1 and self.obtenir_piece((depart[0] + 1, depart[1])) is None:
                    return True
            elif abs(depart[1] - arrivee[1]) == 1 and arrivee[0] == depart[0] + 1 and self.obtenir_piece(arrivee) is not None and self.obtenir_piece(arrivee).couleur == 'noir':
                return True
        else:
            if depart[1] == arrivee[1] and self.obtenir_piece(arrivee) is None:
                if arrivee[0] == depart[0] - 1:
                    return True
                if arrivee[0] == depart[0] - 2 and depart[0] == 6 and self.obtenir_piece((depart[0] - 1, depart[1])) is None:
                    return True
            elif abs(depart[1] - arrivee[1]) == 1 and arrivee[0] == depart[0] - 1 and self.obtenir_piece(arrivee) is not None and self.obtenir_piece(arrivee).couleur == 'blanc':
                return True
    elif piece_depart.symbole == 'R':
        if depart[0] == arrivee[0] or depart[1] == arrivee[1]:
            if depart[0] == arrivee[0]:
                debut, fin = (depart[1], arrivee[1]) if arrivee[1] > depart[1] else (arrivee[1], depart[1])
                for i in range(debut+1, fin):
                    if self.obtenir_piece((depart[0], i)) is not None:
                        return False
            else:
                debut, fin = (depart[0], arrivee[0]) if arrivee[0] > depart[0] else (arrivee[0], depart[0])
                for i in range(debut+1, fin):
                    if self.obtenir_piece((i, depart[1])) is not None:
                        return False
            return True
    elif piece_depart.symbole == 'N':
        if abs(depart[0] - arrivee[0]) == 2 and abs(depart[1] - arrivee[1]) == 1 or abs(depart[0] - arrivee[0]) == 1 and abs(depart[1] - arrivee[1]) == 2:
            return True
    elif piece_depart.symbole == 'B':
        if abs(depart[0] - arrivee[0]) == abs(depart[1] - arrivee[1]):
            ligne_debut, colonne_debut = (depart[0], depart[1]) if depart[0] < arrivee[0] else (arrivee[0],arrivee[1])
            pas_ligne = 1 if arrivee[0] > depart[0] else -1
            pas_colonne = 1 if arrivee[1] > depart[1] else -1
            for i in range(1, abs(depart[0] - arrivee[0])):
                if self.obtenir_piece((ligne_debut + i*pas_ligne, colonne_debut + i*pas_colonne)) is not None:
                    return False
            return True
    elif piece_depart.symbole == 'Q':
        if abs(depart[0] - arrivee[0]) == abs(depart[1] - arrivee[1]):
            ligne_debut, colonne_debut = (depart[0], depart[1]) if depart[0] < arrivee[0] else (arrivee[0], arrivee[1])
            pas_ligne = 1 if arrivee[0] > depart[0] else -1
            pas_colonne = 1 if arrivee[1] > depart[1] else -1
            for i in range(1, abs(depart[0] - arrivee[0])):
                if self.obtenir_piece((ligne_debut + i*pas_ligne, colonne_debut + i*pas_colonne)) is not None:
                    return False
            return True
        elif depart[0] == arrivee[0] or depart[1] == arrivee[1]:
            if depart[0] == arrivee[0]:
                debut, fin = (depart[1], arrivee[1]) if arrivee[1] > depart[1] else (arrivee[1], depart[1])
                for i in range(debut+1, fin):
                    if self.obtenir_piece((depart[0], i)) is not None:
                        return False
            else:
                debut, fin = (depart[0], arrivee[0]) if arrivee[0] > depart[0] else (arrivee[0], depart[0])
                for i in range(debut+1, fin):
                    if self.obtenir_piece((i, depart[1])) is not None:
                        return False
            return True
    elif piece_depart.symbole == 'K':
        if abs(depart[0] - arrivee[0]) <= 1 and abs(depart[1] - arrivee[1]) <= 1:
            return True
        # Roque
        elif abs(depart[1] - arrivee[1]) == 2 and depart[0] == arrivee[0]:
            if self.echec():
                return False
            if arrivee[1] > depart[1]:
                roi_case = self.obtenir_case_roi(self.tour)
                tour_case = (depart[0], 7)
                nouvelle_roi_case = (roi_case[0], 6)
            else:
                roi_case = self.obtenir_case_roi(self.tour)
                tour_case = (depart[0], 0)
                nouvelle_roi_case = (roi_case[0], 2)
            roi = self.obtenir_piece(roi_case)
            tour = self.obtenir_piece(tour_case)
            for case in [roi_case, tour_case]:
                if self.attaque(case, self.tour):
                    return False
            if tour is None or tour.deplacement != 0 or roi.deplacement != 0:
                return False
            for i in range(min(arrivee[1], depart[1])+1, max(arrivee[1])):
                if self.obtenir_piece((depart[0], i)) is not None:
                    return False
            self.deplacer(roi_case, nouvelle_roi_case)
            self.deplacer(tour_case, (nouvelle_roi_case[0], (nouvelle_roi_case[1]+tour_case[1])//2))
            self.tour = not self.tour
            return True
        else:
            return False
    else:
        return False

