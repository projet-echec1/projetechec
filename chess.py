class ChessGame:
    
    def __init__(self):

        class Piece:
            def __init__(self,couleur,symbole):
            self.symbole=symbole
            self.couleur=couleur
 

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


    def movesjoueur (self):
        ligne=int(input("Ligne de jeu"))
        colonne=int(input("Colonne de jeu"))
        return [ligne,colonne]

    def choixpiece(self):
        pieceligne=input(int("Position en ligne de la pièce à jouer")) #Pour éviter confusions  demander la case actuelle de la pièce
        piececolonne=input(int("Position de la pièce en colonne à jouer"))
        
        return [pieceligne,piececolonne]


    def cavalier(self): #Le cavalier se déplace en L s'est à dire +/- 2 en largeur et +/- 1 en longueur et inversement
        
            cavalier=[[self.choixpiece[0]+2,self.choixpiece[0]+1],[self.choixpiece[0]+2,self.choixpiece[0]-1],[self.choixpiece[0]-2,self.choixpiece[0]-1],[self.choixpiece[0]-2,self.choixpiece[0]+1],[self.choixpiece[0]+1,self.choixpiece[0]+2],[self.choixpiece[0]+1,self.choixpiece[0]-2],[self.choixpiece[0]-1,self.choixpiece[0]-2],[self.choixpiece[0]-1,self.choixpiece[0]+2]]]
    
 
   def pion(self):
        if self.turn==1 or self.turn==2: 
            pion=[[self.choixpiece[0]+1,self.choixpiece[0]+1],[self.choixpiece[0]+2,self.choixpiece[0]+2]]
        else:
            pion=[[self.choixpiece[0]+1,self.choixpiece[0]+1]]
        return pion
    
    def tour(self):
        tour
        for i in range (1,8):
        

           





