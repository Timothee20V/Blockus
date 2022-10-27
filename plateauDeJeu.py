def creationPlateau(n):

    grille = []
    for line in range(n):
        nvline = []
        for col in range(n):
         nvline.append((0))
        grille.append(nvline)
    for line in grille:
        print(line)
    return grille


carre = []
for cLine in range (2):
    cnvline =[]
    for ccol in range (2):
        cnvline.append(("c"))
    carre.append(cnvline)
for cline in carre:
    print(cline)
print('UwUUwUUwUUwUUwUUwUUwUUwUUwUUwUUwUUwUUwUUwUUwUUwUUwU')

#listeA = ["Ronds-", "Coffres-", "Porte-"]
#listeB = ['points', 'forts', 'bonheur']
#print ("Liste A :", listeA)
#print ("Liste B :", listeB)
# Utilisez le zip
#résultat = [i j for  j in zip (listeA, listeB)]
# Résultat
#print ("Les listes concaténées:", résultat)



def placementPiece(grille,piece,coordonne,):
    #grilleResult=grille
    for cLine in range (0,len(grille)):
        cnvline = grille
        for ccol in range (0,len(grille)):
            if (grille[ccol] != 0):
                cnvline.append(("c"))
        grille.append(cnvline)


    for i in range (0,len(grille)) :
        if (grille [i]!=0) :
            grille.append(piece[i])
    
    return grille  
    
    
grille = placementPiece(grille, carre)   


for line in grille:
    print(line)
