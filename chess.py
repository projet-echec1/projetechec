class Piece:
            def __init__(self,couleur,symbole):
                self.symbole=symbole
                self.couleur=couleur
 



class ChessGame:
    
    def __init__(self):

       

        self.echiquier = [ [Piece('noir', 'R'), Piece('noir', 'N'), Piece('noir', 'B'), Piece('noir', 'Q'), Piece('noir', 'K'), Piece('noir', 'B'), Piece('noir', 'N'), Piece('noir', 'R')]
                      , [Piece('noir', 'P'), Piece('noir', 'P'), Piece('noir', 'P'), Piece('noir', 'P'), Piece('noir', 'P'), Piece('noir', 'P'), Piece('noir', 'P'), Piece('noir', 'P')],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None], 
                      [Piece('blanc', 'P'), Piece('blanc', 'P'), Piece('blanc', 'P'), Piece('blanc', 'P'), Piece('blanc', 'P'), Piece('blanc', 'P'), Piece('blanc', 'P'), Piece('blanc', 'P')],
                      [Piece('blanc', 'R'), Piece('blanc', 'N'), Piece('blanc', 'B'), Piece('blanc', 'Q'), Piece('blanc', 'K'), Piece('blanc', 'B'), Piece('blanc', 'N'), Piece('blanc', 'R')] ]
        
        self.echiquierbinaire=self.echiquierbinaire(self.echiquier)               

                      

    
        self.tour='blanc'
        self.compteur=1

    def echiquierbinaire(self,t):
        a=[]
        for i in range(8):
            b=[]
            a.append(b)
            for j in range(8):
                x=t[i][j]
                if x==None:
                    b.append(0)
                elif x!=None and x.couleur=='noir':
                    b.append(-1)
                else:
                    b.append(1)



    def changement_tour(): #projet-echec1
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
                piece=self.obtenir_piece(i,j)
                if piece.couleur==couleur and piece.symbole=='R':
                    return(i,j)
            
            
    def echec(self):
        roi_case=self.case_roi(self.tour)
        for i in range(8):
            for j in range(8):
                piece=self.obtenir_piece(i,j)
                if piece != None and piece.couleur!= self.tour:  #on s'assure que la piece qui met en echec est de la bonne couleur et qu'elle existe
                    if self.coup_legal((i,j),roi_case):          #on utilise la fonction qui verifie si le mouvement de la piece est autorisé
                        return True
        return False     
            


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
#Mouvements


 
    def choix_piece(self):
       ligne=int(input("Ligne de la pièce à jouer"))
       colonne=int(input("Colonne de la pièce à jouer"))
       return [ligne,colonne]
    
    def deplacer_piece(self,départ,arrivée):
        piece=self.obtenir_piece(départ)
        self.echiquier[départ[0]][départ[1]]=None
        self.echiquier[arrivée[0]][arrivée[1]]=piece

        

    def choixmouvementjoueur (self):
            ligne=int(input("Ligne de jeu"))
            colonne=int(input("Colonne de jeu"))
            return [ligne,colonne]

        
    
    def mouvement_type(self,piecedepart,piecearrivée,positiondépart,positionarrivée): #position de départ
            x=piecedepart
            if x.symbole==N:
                return self.cavalier(piecedepart,piecearrivée,positiondépart,positionarrivée)
            elif x.symbole==R:
                return self.rook(piecedepart,piecearrivée,positiondépart,positionarrivée)
            elif x.symbole==B:
                return self.fou(piecedepart,piecearrivée,positiondépart,positionarrivée)
            elif x.symbole==K:
                return self.roi(piecedepart,piecearrivée,positiondépart,positionarrivée)
            elif x.symbole==Q:
                return self.reine(piecedepart,piecearrivée,positiondépart,positionarrivée)
            elif x.symbole==P:
                return self.pion(piecedepart,piecearrivée,positiondépart,positionarrivée)
                       
    def echec_et_mat(self):
        if self.echec==False:  #cas le plus simple où il n'y a pas d'échec au roi
            return False
        for i in range(8):
            for j in range(8):
                piece=self.obtenir_piece(i,j)
                if piece !=None and piece.couleur==self.tour:
                    for x in range(8):
                        for y in range(8):
                            if self.coup_legal((i,j),(x,y))==True:
                                piece_arrivee_enregistré=self.obtenir_piece(x,y)
                                self.deplacer_piece((i,j),(x,y))
                                echec=self.echec()
                                if echec==False:
                                        return False

                                
        return True
                                                
    """                            



  
    
    def pion(self,position):
        if self.couleur=='blanc':
            if self.compteur==1:
                possible=[[position[0],position[1]+2],[position[0],position[1]+1],]
            else:
                possible=[position[0],position[1]+1]
        
        else:
            if self.compteur==2:
                   possible=[[position[0],position[1]-2],[position[0],position[1]-1],]
            else:
                possible=[position[0],position[1]-1]
        

        for i in range(len(possible)): #En faire une fonction pour plus tard 
            if possible[i]==None:
                continue
            elif possible[i].couleur==self.couleur:
                possible.pop(i)
            else:
                continue

        return possible"""

    def coup_legal(self,positiondépart,positionarrivée):
        piecedépart=self.obtenir_piece(positiondépart)
        piecearrivée=self.obtenir_piece(positionarrivée)
        if piecedépart==None: #On ne peut pas sélectionner une case vide
            return False
        elif piecedépart.couleur!=self.tour: #Impossible de déplacer une pièce adverse
            return False
        elif piecedépart.couleur==piecearrivée.couleur: #Impossible de jouer sur une case occupée par ses propres pièces
            return False
        else:
            return self.mouvement_type(piecedépart,piecearrivée,positiondépart,positionarrivée)

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
                        if couleur.self.echiquier[x][i]!=couleur.piecedépart:
                            return False
                    else:
                        return True
                    
            if positiondépart[1]>positionarrivée[1]:
                for i in range (positionarrivée[1],positiondépart[1]-1):
                    if self.echiquier[x][i]!=None:
                        if couleur.self.echiquier[x][i]!=couleur.piecedépart:
                            return False
                    else:
                        return True
        else:
            if positiondépart[0]< positionarrivée[0]:
                for i in range (positiondépart[0]+1,positionarrivée[0]):
                    if self.echiquier[i][y]!=None:
                        if couleur.self.echiquier[i][y]!=couleur.piecedépart:
                            return False
                    else:
                        return True
                    
            if positiondépart[0]>positionarrivée[0]:
                for i in range (positionarrivée[0],positiondépart[0]-1):
                    if self.echiquier[i][y]!=None:
                        if couleur.self.echiquier[i][y]!=couleur.piecedépart:
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
                            if couleur.self.obtenir_piece(x1+i,y2+i)!=couleur.piecedépart:
                                return False
                        else:
                            return True    
                else:
                    for i in range (1,abs(y1-y2)):
                        if self.obtenir_piece(x1+i,y2-i)!=None:
                            if couleur.self.obtenir_piece(x1+i,y2-i)!=couleur.piecedépart:
                                return False
                        else:
                            return True    
            else:
                if y1<y2:
                    for i in range (1,abs(y1-y2)):
                        if self.obtenir_piece(x1-i,y2+i)!=None:
                            if couleur.self.obtenir_piece(x1-i,y2+i)!=couleur.piecedépart:
                                return False
                        else:
                            return True    
                else:
                    for i in range (1,abs(y1-y2)):
                        if self.obtenir_piece(x1-i,y2-i)!=None:
                            if couleur.self.obtenir_piece(x1-i,y2-i)!=couleur.piecedépart:
                                return False
                        else:
                            return True    
    
        
        
        


    def obtenir_tous_les_coups(self):
        a=[]
        for i in range(8):
            for j in range(8):
                if self.obtenirpiece(i,j) is not None:
                    for x in range(8):
                        for y in range(8):
                            if coup_legal((i,j),(x,y))==True:
                                a.append[[x,y]]
                            else:
                                continue
        return a
        
    def copier(self):
        copie=Chessgame()
        copie.etat=[l for l in self.echiquier]
        return copie
    
#ordi
class joueur:
    def __init__(self,couleur):
        self.couleur=couleur

    def jouercoup(self,Chessgame):
        pass
class minmax(joueur):
    def __init__(self,couleur,profondeur_max):
        super().__init__(couleur)
        self.profondeur_max=profondeur_max

    def jouer_coup(self,ChessGame):
        meilleur_coup=None
        meilleur_score=float('-inf')
        for coups in Chessgame.obtenir_tous_les_coups(self.couleur):
            
