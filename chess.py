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

    
        self.tour=='blanc'

    def changement_tour(): #projet-echec1
        if self.tour=='blanc':
            self.tour='noir'
        else:
            self.tour='blanc' #Deux valeurs possibles uniquement 'noir' ou 'blanc'
    


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

def choixpiece(self):
    pieceligne=input(int("Position en ligne de la pièce à jouer")) #Pour éviter confusions  demander la case actuelle de la pièce
    piececolonne=input(int("Position de la pièce en colonne à jouer"))
        
    return [pieceligne,piececolonne]
    
def piecemouvementpossible(self,position): #position de départ
        x=obtenir_piece(self,position)
        if x.symbole==N:
            return cavalier(self,position)
        elif x.symbole==R:
            return rook(self,position)
        elif x.symbole==B:
            return fou(self,position)
        elif x.symbole==K:
            return roi(self,position)
        elif x.symbole==Q:
            return reine(self,position)
        elif x.symbole==P:
            return pion(self,position)
        else:
            print("Case vide recommencez")
            piecemouvementpossible(self,position)
                       
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
                                                
                                
def cavalier(self,position):
    #Cavalier se déplace en L donc en colonne (+/-1) ou (+/-2) et en largeur (+/-1) ou (+/-2)
    possible=[[position[0]+1,position[1]+2], [position[0]-1,position[1]-2],[position[0]+1,position[1]-2],[position[0]-1,position[1]+2],[position[0]+2,position[1]+1],[position[0]-2,position[1]-1],[position[0]-2,position[1]+1],[position[0]+2,position[1]-1]]

    for i in range(len(possible)):
        if possible[i].couleur==self.couleur:
            possible.pop(i)
        else:
            continue
    return possible
