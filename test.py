def lire_fichier(fichier):
    m = []
    with open(fichier, "r") as f:
        for ligne in f:
            m.append(tuple(ligne.strip().split(' ')))
    return m

print(lire_fichier('pieces/piece1'))