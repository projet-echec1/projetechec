
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
    
   """ 
   def pion(self):
        if self.turn==1 or self.turn==2: 
            pion=[[self.choixpiece[0]+1,self.choixpiece[0]+1],[self.choixpiece[0]+2,self.choixpiece[0]+2]]
        else:
            pion=[[self.choixpiece[0]+1,self.choixpiece[0]+1]]
        return pion
    
    def tour(self):
        tour
        for i in range 1,8
        
       """ 
