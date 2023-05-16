import random

def attribuer_couleurs():
    couleurs = ["blanc", "noir"]
    random.shuffle(couleurs)

    couleur_humain = couleurs[0]

    return couleur_humain
class Piece(): 

    def __init__(self,couleur,symbole):
        self.symbole=symbole
        self.couleur=couleur
 
class ChessGame():
    
    def __init__(self):
        self.echiquier = [ [Piece('noir', 'R'), Piece('noir', 'N'), Piece('noir', 'B'), Piece('noir', 'Q'), Piece('noir', 'K'), Piece('noir', 'B'), Piece('noir', 'N'), Piece('noir', 'R')]
                      , [Piece('noir', 'P'), Piece('noir', 'P'), Piece('noir', 'P'), Piece('noir', 'P'), Piece('noir', 'P'), Piece('noir', 'P'), Piece('noir', 'P'), Piece('noir', 'P')],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None], 
                      [Piece('blanc', 'P'), Piece('blanc', 'P'), Piece('blanc', 'P'), Piece('blanc', 'P'), Piece('blanc', 'P'), Piece('blanc', 'P'), Piece('blanc', 'P'), Piece('blanc', 'P')],
                      [Piece('blanc', 'R'), Piece('blanc', 'N'), Piece('blanc', 'B'), Piece('blanc', 'Q'), Piece('blanc', 'K'), Piece('blanc', 'B'), Piece('blanc', 'N'), Piece('blanc', 'R')] ]
        
      

    


        self.printboard=self.print_board()    

        self.joueur=attribuer_couleurs()          

    
        self.tour='blanc'
        self.compteur=1
    


    def print_board(self):
        a=[]
        for i in range(8):
            b=[]
            a.append(b)
        
            for j in range(8):
                p=self.obtenir_piece([i,j])
                if p==None:
                    b.append("")
                else:
                    if p.couleur=='blanc':
                        b.append("w"+str(p.symbole))

                    else: 
                        b.append("b"+str(p.symbole))
        return a
    

    def changement_tour(self): #projet-echec1
        if self.tour=='blanc':
            self.tour='noir'
            self.compteur+=1
        else:
            self.tour='blanc' #Deux valeurs possibles uniquement 'noir' ou 'blanc'
            self.compteur+=1
  
    def obtenir_piece(self, position):

        ligne, colonne = position 
        
        return self.echiquier[ligne][colonne]
    
    def case_roi(self,couleur):
        for i in range(8):
            for j in range(8):
                piece=self.obtenir_piece([i,j])
                if piece is not None:
                    if piece.couleur==couleur and piece.symbole=='R':
                        return(i,j)    
                  

    def est_capturable(self,position):
        piece2=self.obtenir_piece(position)
        for i in range(8):    
            for j in range(8):
                piece1=self.obtenir_piece([i,j])
                if piece1 is not None and piece1.couleur!=piece2.couleur:
                    if self.coup_valide((i,j),position) is True:
                        return [piece2.symbole, True]

    def peut_capturer(self,position):
        a=[]
        for i in range(8):
            for j in range(8):
                if self.coup_valide(position,[i,j]) is True:
                    c=self.obtenir_piece([i,j])
                    a.append(c)
                    
                    return a                            

    def echec(self):
        roi_case=self.case_roi(self.tour)
        if self.est_capturable(roi_case) is True:          #on utilise la fonction qui verifie si le mouvement de la piece est autorisé
            return True
        return False     
            


    def jouer(self):
        print("Bienvenue au jeu d'échecs!")
        while self.echec_et_mat() is False:
            print(self.echiquier)
            self.deroulement()
    
    def deroulement(self):
        if self.tour=='blanc':
            if self.joueur=='blanc':
                print("C'est au tour des blancs")
                depart=self.choix_piece()
                arrivee=self.choixmouvementjoueur()
                if self.echec():
                    print("Vous êtes en échec")
                if self.coup_valide(depart,arrivee) is True:
                    self.deplacer_piece(depart, arrivee)
                    self.changement_tour()
                
                else:
                    print("Coup impossible, veuillez rejouez")
                    self.deroulement()
                    
            else:
                depart,arrivee=self.minmax('blanc',2,self.echiquier)
                self.deplacer_piece(depart, arrivee)
                self.changement_tour()
                    
        else:
            print("C'est au tour des noirs")
            if self.joueur=='noir':
                depart=self.choix_piece()
                arrivee=self.choixmouvementjoueur()
                if self.echec():
                    print("Vous êtes en échec")
                if self.coup_valide(depart,arrivee)==True:
                    self.deplacer_piece(depart, arrivee)
                    self.changement_tour()

                else:
                    print("Coup impossible, veuillez rejouez")
                    self.deroulement()
            else:
                depart,arrivee=self.minmax('blanc',2,self.echiquier)
                self.deplacer_piece(depart, arrivee)
                self.changement_tour()

        


            if self.echec_et_mat() is True:
                print("C'est finito pour toi, révise tes leçons")
        

    def sauvegarder_etat_echiquier(self,echiquier):
        a=[]
        for i in range(8):
            for j in range (8):
                a.append(echiquier[i][j])
        return a


 
    def choix_piece(self):
        ligne=int(input("Ligne de la pièce à jouer de 1 à 8 "))-1
        colonne=int(input("Colonne de la pièce à jouer de 1 à 8 "))-1
        print(self.obtenir_piece([ligne,colonne]).couleur, self.obtenir_piece([ligne,colonne]).symbole)

        if self.obtenir_piece([ligne,colonne]).couleur!=self.tour: #Impossible de déplacer une pièce adverse
            print("Pièce adverse !")
            return self.choix_piece()
        else:    
            return [ligne,colonne]
    
    def deplacer_piece(self,depart,arrivee):
        piece=self.obtenir_piece(depart)
        self.echiquier[depart[0]][depart[1]]=None
        self.echiquier[arrivee[0]][arrivee[1]]=piece

        

    def choixmouvementjoueur(self):
        ligne=int(input("Ligne de jeu"))
        colonne=int(input("Colonne de jeu"))
        return [ligne,colonne]

        
    
    def mouvement_type(self,piecedepart,piecearrivee,positiondepart,positionarrivee): #position de départ
        x=piecedepart
        if x.symbole=='N':
            return self.cavalier(positiondepart,positionarrivee)
        elif x.symbole=='R':
            return self.rook(piecedepart,positiondepart,positionarrivee)
        elif x.symbole=='B':
            return self.fou(piecedepart,positiondepart,positionarrivee)
        elif x.symbole=='K':
            return self.roi(positiondepart,positionarrivee)
        elif x.symbole=='Q':
            return self.reine(piecedepart,positiondepart,positionarrivee)
        elif x.symbole=='P':
            return self.pion(piecedepart,piecearrivee,positiondepart,positionarrivee)
                       
    def coup_legal(self,positiondepart,positionarrivee):
        piecedepart=self.obtenir_piece(positiondepart)
        piecearrivee=self.obtenir_piece(positionarrivee)    
        if piecedepart==None: #On ne peut pas sélectionner une case vide
            print("Case vide")
            return False
        
        elif  piecearrivee!=None and piecedepart.couleur==piecearrivee.couleur: #Impossible de jouer sur une case occupée par ses propres pièces
            print("Case occupée par une de vos pièces")
            return False
        else:
            return self.mouvement_type(piecedepart,piecearrivee,positiondepart,positionarrivee)
        
    def echec_et_mat(self):
        if self.echec() is False:  #cas le plus simple où il n'y a pas d'échec au roi
            return False
        for i in range(8):
            for j in range(8):
                piece=self.obtenir_piece([i,j])
                if piece is not None and piece.couleur==self.tour:
                    for x in range(8):
                        for y in range(8):
                            if self.coup_valide((i,j),(x,y)) is True:
                                self.deplacer_piece((i,j),(x,y))
                                echec=self.echec()
                                if echec is False:
                                    return False

                                
        return True

    def coup_valide(self,positiondepart,positionarrivee,):
        
        if self.coup_legal(positiondepart,positionarrivee)==True:
            self.deplacer_piece(positiondepart,positionarrivee)
            if self.echec()==True or self.echec_et_mat()==True:
                return False
            else:
                return True
        else:
            return False    
    
    

    def cavalier(self,positiondepart,positionarrivee):
        if abs(positiondepart[0]-positionarrivee[0])==2 and abs(positiondepart[1]-positionarrivee[1])==1:
            return True
        if abs(positiondepart[0]-positionarrivee[0])==1 and abs(positiondepart[1]-positionarrivee[1])==2:
            return True
        else:
            return False
        
    
    def virtuel(self):
        virt=self.echiquier
        return virt

    



    def rook(self,piecedepart,positiondepart,positionarrivee):
        x=positiondepart[0]
        y=positiondepart[1]
        if positiondepart[0]!=positionarrivee[0] and positiondepart[1]!=positionarrivee[1]:
            return False
        elif positiondepart[0]==positionarrivee[0]:
            if positiondepart[1]< positionarrivee[1]:
                for i in range (positiondepart[1]+1,positionarrivee[1]):
                    if self.echiquier[x][i]!=None:
                        if self.echiquier[x][i].couleur!=piecedepart.couleur:
                            return False
                    else:
                        return True
                    
            if positiondepart[1]>positionarrivee[1]:
                for i in range (positionarrivee[1]+1,positiondepart[1]):
                    if self.echiquier[x][i]!=None:
                        if self.echiquier[x][i].couleur!=piecedepart.couleur:
                            return False
                    else:
                        return True
        else:
            if positiondepart[0]< positionarrivee[0]:
                for i in range (positiondepart[0]+1,positionarrivee[0]):
                    if self.echiquier[i][y]!=None:
                        if self.echiquier[i][y].couleur!=piecedepart.couleur:
                            return False
                    else:
                        return True
                    
            if positiondepart[0]>positionarrivee[0]:
                for i in range (positionarrivee[0]+1,positiondepart[0]):
                    if self.echiquier[i][y]!=None:
                        if self.echiquier[i][y].couleur!=piecedepart.couleur:
                            return False
                    else:
                        return True

    def fou(self,piecedepart,positiondepart,positionarrivee):
        x1=positiondepart[0]
        y1=positiondepart[1]
        x2=positionarrivee[0]
        y2=positionarrivee[1]

        if abs(x2-x1)!=abs(y2-y1):
            return False
        else:
            if x1 < x2:
                if y1<y2:
                    for i in range (1,abs(y1-y2)):
                        if self.obtenir_piece([x1+i,y2+i])!=None:
                            if self.obtenir_piece([x1+i,y2+i]).couleur!=piecedepart.couleur:
                                return False
                        else:
                            return True    
                else:
                    for i in range (1,abs(y1-y2)):
                        if self.obtenir_piece([x1+i,y2-i])!=None:
                            if self.obtenir_piece([x1+i,y2-i]).couleur!=piecedepart.couleur:
                                return False
                        else:
                            return True    
            else:
                if y1<y2:
                    for i in range (1,abs(y1-y2)):
                        if self.obtenir_piece([x1-i,y2+i])!=None:
                            if self.obtenir_piece([x1-i,y2+i]).couleur!=piecedepart.couleur:
                                return False
                        else:
                            return True    
                else:
                    for i in range (1,abs(y1-y2)):
                        if self.obtenir_piece([x1-i,y2-i])!=None:
                            if self.obtenir_piece([x1-i,y2-i]).couleur!=piecedepart.couleur:
                                return False
                        else:
                            return True   
                
        
    def reine(self,piecedepart,positiondepart,positionarrivee):
        return self.rook(piecedepart,positiondepart,positionarrivee) or self.fou(piecedepart,positiondepart,positionarrivee)        

    def pion(self,piecedepart,piecearrivee,positiondepart,positionarrivee):
        x1=positiondepart[0]
        y1=positiondepart[1]
        x2=positionarrivee[0]
        y2=positionarrivee[1]
        
        if piecedepart.couleur=='noir':
            if y1==y2:
                if x1==1:
                    if x2==x1+1 or x2==x1+2:
                        return True
                    else:
                        return False
                else:
                    if x2==x1+1:
                        return True
                    else:
                        return False
                    
            elif y2-y1==1 and abs(x1-x2)==1:
                if piecearrivee!=None and piecearrivee.couleur!=piecedepart.couleur:
                    return True
                else:
                    return False
            else:
                return False
        
        if piecedepart.couleur=='blanc':
            if y1==y2:
                if x1==6:
                    if x2==x1-1 or x2==x1-2:
                        return True
                    else:
                        return False
                else:
                    if x2==x1-1:
                        return True
                    else:
            
                        return False
                    
            elif y2-y1==-1 and abs(x1-x2)==1:
                if piecearrivee!=None and piecearrivee.couleur!=piecedepart.couleur:
                    return True
                else:
                    return False
            else:
                return False

                     

           

    
    
    def roi(self,positiondépart,positionarrivée):
        if abs(positionarrivée[0]-positiondépart[0])==1 and (positionarrivée[1]-positiondépart[1])==1:
            return True
        else:
            return False
         
                

    def checkpromotion(self):
        for i in range(8):
            
            a=self.obtenir_piece(self.echiquier[7][i])
            p=self.echiquier[7][i]
            
            if a.couleur=='blanc' and a.symbole=='P':
                self.promotion(p,a)
            
            c=self.obtenir_piece(self.echiquier[0][i])
            p1=self.echiquier[0][i]
            
            if c.couleur=='blanc' and a.symbole=='P':
                self.promotion(p1,c)
            
            


    def promotion(self,p,c):
        b=['P','Q','K','B','N','R']
        i=input("Promotion ! Quelle pièce choisissez vous ?")
        if i not in b:
            print("Erreur, la pièce n'existe pas")
            self.promotion(p,c)
        
        else:
            p=Piece(c.couleur,i)



    def obtenir_tous_les_coups(self):
        coup_possible=[]
        position_piece=[]
        for i in range(8):
            for j in range(8):
                piece=self.echiquier[i][j]
                if piece is not None and piece.couleur==self.tour:
                    for x in range(8):
                        for y in range(8):
                            if self.coup_valide((i,j),(x,y))==True:
                                coup_possible.append([x,y])
                                position_piece.append([i,j])
                            else:
                                continue
        return position_piece,coup_possible
        
    


    def evaluer_echiquier(self,echiquier):
        
        valeur_pieces={
            'P': 1,
            'N': 3,
            'B':3,
            'R':5,
            'Q':9,
            'K':10 }
        score_total = 0

        for ligne in range(8):
            for colonne in range (8):
                piece=echiquier[ligne][colonne]

                if piece is not None:
                    score_total+=valeur_pieces[piece]
                    if piece in ['P','N','B','R','Q']:
                        score_total+=0.1
                    if piece =='K':
                        if self.est_capturable((ligne,colonne)):
                            score_total -=0.5
        return score_total





   

    def minmax(self,joueur,profondeur,echiquier):
        if profondeur==0 or self.echec_et_mat:
            score=self.evaluer_echiquier(echiquier)
            return None,None,score

        meilleur_mouvement=None
        if joueur=='noir':
            meilleur_score=float('inf')
        else:
            meilleur_score = float('-inf')
        
        for coup in self.obtenir_tous_les_coups()[0]:
            depart,arrivee=coup
            piece_deplacee=echiquier[depart[0]][depart[1]]
            piece_capturee=echiquier[arrivee[0]][arrivee[1]]
            
            echiquier[arrivee[0]][arrivee[1]]=piece_deplacee
            echiquier[depart[0]][depart[1]]=None
            score=self.minmax(self.joueur,profondeur-1,echiquier)

            echiquier[arrivee[0]][arrivee[1]]=piece_capturee
            echiquier[depart[0]][depart[1]]=piece_deplacee

            if joueur=='noir':
                if score< meilleur_score:
                    meilleur_score = score
                    meilleur_mouvement= coup
            else:
                if score>meilleur_score:
                    meilleur_score=score
                    meilleur_mouvement=coup
        return meilleur_mouvement,meilleur_score



            


             
             
A=ChessGame()
A.jouer()
