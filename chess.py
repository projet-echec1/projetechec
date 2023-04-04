class Piece: #BACDS
            def __init__(self,couleur,symbole):
                self.symbole=symbole
                self.couleur=couleur

class ChessGame: #BACDS
    
    def __init__(self):

       

        self.echiquier = [ [Piece('noir', 'R'), Piece('noir', 'N'), Piece('noir', 'B'), Piece('noir', 'Q'), Piece('noir', 'K'), Piece('noir', 'B'), Piece('noir', 'N'), Piece('noir', 'R')]
                      , [Piece('noir', 'P'), Piece('noir', 'P'), Piece('noir', 'P'), Piece('noir', 'P'), Piece('noir', 'P'), Piece('noir', 'P'), Piece('noir', 'P'), Piece('noir', 'P')],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None], 
                      [Piece('blanc', 'P'), Piece('blanc', 'P'), Piece('blanc', 'P'), Piece('blanc', 'P'), Piece('blanc', 'P'), Piece('blanc', 'P'), Piece('blanc', 'P'), Piece('blanc', 'P')],
                      [Piece('blanc', 'R'), Piece('blanc', 'N'), Piece('blanc', 'B'), Piece('blanc', 'Q'), Piece('blanc', 'K'), Piece('blanc', 'B'), Piece('blanc', 'N'), Piece('blanc', 'R')] ] 

        self.tour = 'blanc'





    def obtenir_piece(self, position):

        ligne, colonne = position 

        return self.echiquier[ligne][colonne]
    

   
    
        def case_roi(self):
            for i in range(8):
                for j in range(8):
                    piece=self.obtenir_piece(i,j)
                    if piece.couleur==couleur and 


#Mouvements


    def choixmouvementjoueur (self): #Projet-echec1
        ligne=int(input("Ligne de jeu"))
        colonne=int(input("Colonne de jeu"))
        return [ligne,colonne]

    def choixpiece(self): #projet-echec1
        pieceligne=input(int("Position en ligne de la pièce à jouer")) #Pour éviter confusions  demander la case actuelle de la pièce
        piececolonne=input(int("Position de la pièce en colonne à jouer"))
        
        return [pieceligne,piececolonne]
    
    def mouvementpiece(self,position): #position de départ -projet-echec1
        x=self.obtenir_piece(self,position)
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
            print("Case vide")
            piecemouvementpossible(self,position)
        

    def cavalier(self,position): #projet-echec
                return cavalier=[[position[0]+2,position[1]+1],[position[0]+2,position[0]-1],[position[0]-2,position[0]-1],[position[0]-2,position[0]+1],[position[0]+1,position[0]+2],[position[0]+1,position[0]-2],[position[0]-1,position[0]-2],[position[0]-1,position[0]+2]]
         
        
