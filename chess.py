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

        self.tour = 'blanc'
py




    def obtenir_piece(self, position):

        ligne, colonne = position 

        return self.echiquier[ligne][colonne]
    

    class Piece:
        def __init__(self,couleur,symbole):
            self.symbole=symbole
        self.couleur=couleur    
    
        def case_roi(self):
            for i in range(8):
                for j in range(8):
                    piece=self.obtenir_piece(i,j)
                    if piece.couleur==couleur and 

#Mouvements

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
            print("Case vide recommencer")
            piecemouvementpossible(self,position)
        

           





