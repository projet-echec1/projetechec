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

    
        self.tour='blanc'
        self.compteur=1

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
            

#Mouvements


 
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
    def cavalier(self,position): #projet-echec1
        #Cavalier se déplace en L donc en colonne (+/-1) ou (+/-2) et en largeur (+/-1) ou (+/-2)
        possible=[[position[0]+1,position[1]+2], [position[0]-1,position[1]-2],[position[0]+1,position[1]-2],[position[0]-1,position[1]+2],[position[0]+2,position[1]+1],[position[0]-2,position[1]-1],[position[0]-2,position[1]+1],[position[0]+2,position[1]-1]]

        for i in range(len(possible)): #En faire une fonction pour plus tard 
            if possible[i]==None:
             continue
            elif possible[i].couleur==self.couleur:
                possible.pop(i)
            else:
                continue
        return possible

    def fou(self,position):
        #On crée un système de diagonale et d'antidiagonale d'unité 1
        diagonale=[[position[0]+1,position[1]+1]]
        antidiagonale=[[position[0]+1,position[1]-1]]

        t=[0,1,2,3,4,5,6,7]
        x1=self.position[0]-7 #On cherche à décaler l'incrémentation ici
        x2=self.position[1]-7
    


        t1=[]
        t2=[]
        for i in range(len(t)):
            t1=t1+[t[i]+x1[i],]
            t2=t2+[t[i]+x2[i],]

        p1=[]
        p2=[]    

        for j in range (len(t)): 

            p1=p1+[t1[i]+diagonale[0],t2[i]+diagonale[1]]
            p2=p2+[t1[i]+antidiagonale[0],t2[i]+antidiagonale[1]]
    
        possible=p1+p2

        for i in range(len(possible)): #En faire une fonction pour plus tard 
            if possible[i]==None:
                continue
            elif possible[i].couleur==self.couleur:
                possible.pop(i)
            else:
                continue
    
            return possible



    def rook(self, position):
        #On crée un système ligne colonne de longueur/largeur 1
        ligne=[position[0]+1,position[1]]
        colonne=[position[0],position[1]+1]

        t1=[]
        t2=[]
        for i in range(len(t)):
            t1=t1+[t[i]+x1[i],]
            t2=t2+[t[i]+x2[i],]

        p1=[]
        p2=[]    

        for j in range (len(t)): 

            p1=p1+[t1[i]+ligne[0],t2[i]+ligne[1]]
            p2=p2+[t1[i]+colonne[0],t2[i]+colonne[1]]
    
        possible=p1+p2

        for i in range(len(possible)): #En faire une fonction pour plus tard 
            if possible[i]==None:
                continue
            elif possible[i].couleur==self.couleur:
                possible.pop(i)
            else:
                continue

        return possible
 

    def reine(self,position):
        possible=[rook(self,position)+fou(self,position),]
        return possible

    def roi(self,position):
        ligne=[[position[0]+1,position[1]],[position[0]+1,position[1]]]
        colonne=[[position[0],position[1]+1],position[0],position[1]-1] 
        diagonale=[[position[0]+1,position[1]+1],[position[0]-1,position[1]-1]]
        antidiagonale=[[position[0]+1,position[1]-1],[position[0]+1,position[1]-1]]
     
        possible=ligne+colonne+diagonale+antidiagonale
        for i in len(possible):
            for j in len(possible):
                if possible[i][j]==-1 or possible[i][j]==8:
                    possible.pop(i)
    
        #Condition sur l'échiquier virtuel
        #if virt.echec()==True:
        #   possible.pop(positionechec)


        for i in range(len(possible)): #En faire une fonction pour plus tard 
            if possible[i]==None:
                continue
            elif possible[i].couleur==self.couleur:
                possible.pop(i)
            else:
                continue

        return possible
    
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
