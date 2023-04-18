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
        
      

        self.virtuel=self.echiquier


                      

    
        self.tour='blanc'
        self.compteur=1

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
                if piece1 is not None:
                    if self.coup_valide((i,j),position) is True:
                        return [piece2.symbole, True]

    def peut_capturer(self,piece,position):
        a=[]
        for i in range(8):
            for j in range(8):
                if coup_valide(position,[i,j]) is True:
                    b=self.obtenir_piece([i,j])
                    a.append(c.couleur)
                    
                    return c                            

    def echec(self):
        roi_case=self.case_roi(self.tour)
        for i in range(8):
            for j in range(8):
                piece=self.obtenir_piece([i,j])
                if piece is not None and piece.couleur!= self.tour:  #on s'assure que la piece qui met en echec est de la bonne couleur et qu'elle existe
                    if self.coup_valide((i,j),roi_case) is True:          #on utilise la fonction qui verifie si le mouvement de la piece est autorisé
                        return True
        return False     
            


    def jouer(self):
        print("Bienvenue au jeu d'échecs!")
        while self.echec_et_mat() is False:
            print(self.echiquier)
            self.deroulement()
    
    def deroulement(self):
        if self.tour=='blanc':
            print("C'est au tour des blancs")
            depart=self.choix_piece()
            arrivee=self.choixmouvementjoueur()
            if self.coup_valide(depart,arrivee) is True:
                self.deplacer_piece(depart, arrivee)
                a=self.sauvegarder_etat_echiquier(self.echiquier)
                self.virtuel=a
                self.changement_tour()
                print("C'est au tour des noirs")
                if self.echec():
                    print("Vous êtes en échec")
            else:
                print("Coup impossible, veuillez rejouez")
                self.deroulement()

        else:
            print("C'est au tour des noirs")
            depart=self.choix_piece()
            arrivee=self.choixmouvementjoueur()
            if self.coup_valide(depart,arrivee)==True:
                self.deplacer_piece(depart, arrivee)
                a=self.sauvegarder_etat_echiquier(self.echiquier)
                self.virtuel=a
                self.changement_tour()
                print("C'est au tour des blancs")
                if self.echec():
                    print("Vous êtes en échec")
            else:
                print("Coup impossible, veuillez rejouez")
                self.deroulement()
        


            if self.echec_et_mat() is True:
                print("C'est finito pour toi, révise tes leçons")
        

    def sauvegarder_etat_echiquier(self,echiquier):
        a=[]
        for i in range(8):
            for j in range (8):
                a.append(echiquier[i][j])
        return a


 
    def choix_piece(self):
        ligne=int(input("Ligne de la pièce à jouer"))
        colonne=int(input("Colonne de la pièce à jouer"))
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
            return self.cavalier(piecedepart,piecearrivee,positiondepart,positionarrivee)
        elif x.symbole=='R':
            return self.rook(piecedepart,piecearrivee,positiondepart,positionarrivee)
        elif x.symbole=='B':
            return self.fou(piecedepart,piecearrivee,positiondepart,positionarrivee)
        elif x.symbole=='K':
            return self.roi(positiondepart,positionarrivee)
        elif x.symbole=='Q':
            return self.reine(piecedepart,piecearrivee,positiondepart,positionarrivee)
        elif x.symbole=='P':
            return self.pion(piecedepart,piecearrivee,positiondepart,positionarrivee)
                       
    def coup_legal(self,positiondepart,positionarrivee):
        piecedepart=self.obtenir_piece(positiondepart)
        piecearrivee=self.obtenir_piece(positionarrivee)    
        if piecedepart==None: #On ne peut pas sélectionner une case vide
            return False
        elif piecedepart.couleur!=self.tour: #Impossible de déplacer une pièce adverse
            return False
        elif piecedepart.couleur==piecearrivee.couleur: #Impossible de jouer sur une case occupée par ses propres pièces
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

    def coup_valide(self,positiondépart,positionarrivée):
        virt=self.virtuel
        if self.coup_legal(positiondépart,positionarrivée)==True:
            virt.deplacer_piece(positiondépart,positionarrivée)
            if virt.echec==True or virt.echec_et_mat==True:
                return False
            else:
                return True
    
    

    def cavalier(self,piecedépart,piecearrivée,positiondépart,positionarrivée):
        if abs(positiondépart[0]-positionarrivée[0])==2 and abs(positiondépart[1]-positionarrivée[1])==1:
            return True
        if abs(positiondépart[0]-positionarrivée[0])==1 and abs(positiondépart[1]-positionarrivée[1])==2:
            return True
        else:
            return False
    



    def rook(self,piecedépart,piecearrivée,positiondépart,positionarrivée):
        x=positiondépart[0]
        y=positiondépart[1]
        if positiondépart[0]!=positionarrivée[0] and positiondépart[1]!=positionarrivée[1]:
            return False
        elif positiondépart[0]==positionarrivée[0]:
            if positiondépart[1]< positionarrivée[1]:
                for i in range (positiondépart[1]+1,positionarrivée[1]):
                    if self.echiquier[x][i]!=None:
                        if self.echiquier[x][i].couleur!=piecedépart.couleur:
                            return False
                    else:
                        return True
                    
            if positiondépart[1]>positionarrivée[1]:
                for i in range (positionarrivée[1],positiondépart[1]-1):
                    if self.echiquier[x][i]!=None:
                        if self.echiquier[x][i].couleur!=piecedépart.couleur:
                            return False
                    else:
                        return True
        else:
            if positiondépart[0]< positionarrivée[0]:
                for i in range (positiondépart[0]+1,positionarrivée[0]):
                    if self.echiquier[i][y]!=None:
                        if self.echiquier[i][y].couleur!=piecedépart.couleur:
                            return False
                    else:
                        return True
                    
            if positiondépart[0]>positionarrivée[0]:
                for i in range (positionarrivée[0],positiondépart[0]-1):
                    if self.echiquier[i][y]!=None:
                        if self.echiquier[i][y].couleur!=piecedépart.couleur:
                            return False
                    else:
                        return True

    def fou(self,piecedépart,piecearrivée,positiondépart,positionarrivée):
        x1=positiondépart[0]
        y1=positiondépart[1]
        x2=positionarrivée[0]
        y2=positionarrivée[1]

        if abs(x2-x1)!=abs(y2-y1):
            return False
        else:
            if x1 < x2:
                if y1<y2:
                    for i in range (1,abs(y1-y2)):
                        if self.obtenir_piece(x1+i,y2+i)!=None:
                            if self.obtenir_piece(x1+i,y2+i).couleur!=piecedépart.couleur:
                                return False
                        else:
                            return True    
                else:
                    for i in range (1,abs(y1-y2)):
                        if self.obtenir_piece(x1+i,y2-i)!=None:
                            if self.obtenir_piece(x1+i,y2-i).couleur!=piecedépart.couleur:
                                return False
                        else:
                            return True    
            else:
                if y1<y2:
                    for i in range (1,abs(y1-y2)):
                        if self.obtenir_piece(x1-i,y2+i)!=None:
                            if self.obtenir_piece(x1-i,y2+i).couleur!=piecedépart.couleur:
                                return False
                        else:
                            return True    
                else:
                    for i in range (1,abs(y1-y2)):
                        if self.obtenir_piece(x1-i,y2-i)!=None:
                            if self.obtenir_piece(x1-i,y2-i).couleur!=piecedépart.couleur:
                                return False
                        else:
                            return True   
                
        
    def reine(self,piecedépart,piecearrivée,positiondépart,positionarrivée):
        return self.rook(piecedépart,piecearrivée,positiondépart,positionarrivée) or self.fou(piecedépart,piecearrivée,positiondépart,positionarrivée)        

    def pion(self,piecedépart,piecearrivée,positiondépart,positionarrivée):
        x1=positiondépart[0]
        y1=positiondépart[1]
        x2=positionarrivée[0]
        y2=positionarrivée[1]
        
        if piecedépart.couleur=='blanc':
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
        
        if piecedépart.couleur=='noir':
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
           

    
    
    def roi(self,positiondépart,positionarrivée):
        if abs(positionarrivée[0]-positiondépart[0])==1 and (positionarrivée[1]-positiondépart[1])==1:
            return True
        else:
            return False
         
                

    def checkpromotion(self):
        for i in range(8):
            
            a=self.obtenir_piece(self.echiquier[7][i])
            p=self.echiquier[7][i]
            
            if a.couleur=='blanc' and a.symbole=='P'and self.tour:
                self.promotion(p,a)
            
            c=self.obtenir_piece(self.echiquier[0][i])
            p1=self.echiquier[0][i]
            
            if c.couleur=='blanc' and a.symbole=='P'and self.tour:
                self.promotion(p1,c)
            
            


    def promotion(self,p,c):
        b=['P','Q','K','B','N','R']
        i=input("Promotion ! Quelle pièce choisissez vous ?")
        if i not in b:
            print("Erreur, la pièce n'existe pas")
            self.promotion(p,c)
        
        else:
            p=Piece(c.couleur,p)



    def obtenir_tous_les_coups(self):
        a=[]
        for i in range(8):
            for j in range(8):
                if self.obtenirpiece(i,j) is not None:
                    for x in range(8):
                        for y in range(8):
                            if self.coup_valide((i,j),(x,y))==True:
                                a.append[[x,y]]
                            else:
                                continue
        return a
        
    
"""#ordi
class joueur:
    def __init__(self,couleur):
        self.couleur=couleur

    def jouercoup(self,Chessgame):
        pass
class minmax(joueur):
    def __init__(self,couleur,profondeur_max):
        self.tour='blanc'




    def valeur(self,Chessgame,piece.symbole):
        u=0
        A={'R':5,'P':1,'N':3,'B':3,'Q':9,'K':50}
        for i in A:
            if piece.symbole==i:
                u=i
        return A


    def jouer_coup(self,ChessGame):
        meilleur_coup=None
        meilleur_score=0
        for coups in Chessgame.obtenir_tous_les_coups(self.couleur):
            if self.valeur(self.peut_capturer(coups))>meilleur_score:
                meilleur_coup=self.valeur(self.peut_capturer(coups))
        return meilleur_score

    def minmaxmet(self,ChessGame,profondeur):
        if profondeur==0




            


             """
A=ChessGame()
A.jouer()
