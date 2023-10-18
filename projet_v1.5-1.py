class Joueur:
    '''
    Classe Joueur : représente un joueur.

    Attributs d'instance :
    - self.nom (str): Le nom du joueur.
    - self.__pv (int): Les points de vie du joueur (par défaut à 100).
    - self.__degat (int): Les dégâts du joueur (par défaut à 6).

    Méthode constructeur :
    - __init__(self, pNom (str), pPv=100 (int), pDegat=6 (int, entier)): Initialise un objet Joueur avec un nom, des points de vie et des dégâts.

    Méthodes :
    - set_pv(self, new_pv): Mutateur permettant de changer les points de vie du joueur.
    - set_degat(self, new_degat): Mutateur permettant de changer les dégâts du joueur.
    - __str__(self): Retourne une représentation sous forme de chaîne de caractères du joueur.
    '''

    def __init__(self, pNom, pPv=100, pDegat=6):
        self.nom = pNom
        self.__pv = pPv
        self.__degat = pDegat

    def set_pv(self, new_pv):
        self.__pv = new_pv

    def set_degat(self, new_degat):
        self.__degat = new_degat

    def __str__(self):
        return f"Joueur: {self.nom} pv: {self.__pv} dégât: {self.__degat}"

utilisateur = Joueur(input ("quel est votre nom  " ))
print(utilisateur)


class Paragraphe:
    '''
    Classe Paragraphe : gère la création de paragraphes et l'affichage de l'histoire.

    Méthode constructeur :
    - __init__(self, paragraphe (str)): Initialise un objet Paragraphe avec une description.

    Méthodes :
    - afficher(self): Permet d'afficher la description du paragraphe.
    '''

    def __init__(self, paragraphe):
        self.description = paragraphe

    def afficher(self):
        print(self.description)


class Histoire:
    '''
    Classe Histoire : permet à l'histoire de se dérouler et au joueur de faire des choix.

    Méthode constructeur :
    - __init__(self): Initialise un objet Histoire avec une liste de paragraphes.

    Méthodes :
    - ajouter_paragraphe(self, id (str), paragraphe (Paragraphe)): Ajoute un paragraphe à l'histoire.
    - choix_joueur(self, id (str)): Permet au joueur de faire un choix et affiche le paragraphe correspondant.
    '''

    def __init__(self):
        self.paragraphes = {}

    def ajouter_paragraphe(self, id, paragraphe):
        self.paragraphes[id] = paragraphe

    def choix_joueur(self, id):
        if id not in self.paragraphes:
            print("Ce paragraphe n'existe pas.")
        else:
            self.paragraphes[id].afficher()
    
    def get_paragraphes_keys(self):
        return self.paragraphes.keys()


# Création des paragraphes
paragraphe_intro = Paragraphe("Vous êtes dans un couloir avec deux portes devant vous. \n (a)aller à droite\n (b)aller à gauche\n")
paragraphe_b = Paragraphe("Vous avez pris la porte de droite.\nDevant vous se trouve un gobelin,vous le défier il vous coupe un bras . \n(c)fuire \n(d)continuer le combat \n(e)le supplier")
paragraphe_c = Paragraphe("Vous avez pris la porte de gauche.\nDevant vous se trouve un dieu , il ressemble  à  un crackead.\n Il vous demande a boire\n(f)lui donner \n(g)lui voler sa conso \n(h)fuir")
paragraphe_d = Paragraphe("vous vous retournez pour vous enfuire mais le gobelin vous rattrape et vous tue")
paragraphe_e = Paragraphe("Le goblin vous fonce dessus vous l'esquivez et le tuez ,\nvous sortez de la pièce et découvrez que vous êtes dans un donjon,\nvous regarder au loin et remarqué une étrange forme se déplaçant en rampant tel un chien s'étant fait faucher .Vous le fixer si intensément qu'il sentit votre regard \ncontinuer à le fixer \npartir en courant \nse cacher")
paragraphe_f= Paragraphe("vous êtes pitoyable même le gobelin le semble avoir pitié mais ne vous épargne pas pour autant.\nil vous coupe la tête puis vous utilise comme siège ")
paragraphe_g = Paragraphe("vous lui donnez un coca bien frais chacal\n pour vous récompenser il vous téléporte hors de danger\nvous ouvrez les yeux et remarquer que vous êtes en réalité à une soirée \n vous vous souvenez vous êtres bourré à mort car votre femme vous a trompé ")
paragraphe_h = Paragraphe("vous lui volez sa conso , \nil se met à hurler et se transforme en un horrible monstre avec des crane de bébé accrocher à lui \n éffrayer vous courez mais il vous rattrape et vous arrache les tripes en vous gardant vivants vous mourrez dans d'attroce souffrance")
paragraphe_i =Paragraphe("vous partez à toute vitesse sans demander votre reste .\nvous sortez de la pièce et découvrez que vous êtes dans un donjon,\nvous regarder au loin et remarqué une étrange forme se déplaçant en rampant tel un chien s'étant fait faucher .Vous le fixer si intensément qu'il sentit votre regard \ncontinuer à le fixer \npartir en courant \nse cacher")
# Ajout des paragraphes à l'histoire
histoire = Histoire()
histoire.ajouter_paragraphe("intro", paragraphe_intro)
histoire.ajouter_paragraphe("a", paragraphe_b)
histoire.ajouter_paragraphe("b", paragraphe_c)
histoire.ajouter_paragraphe("c", paragraphe_d)
histoire.ajouter_paragraphe("d", paragraphe_e)
histoire.ajouter_paragraphe("e",paragraphe_f)
histoire.ajouter_paragraphe("f",paragraphe_g)
histoire.ajouter_paragraphe("g",paragraphe_h)
histoire.ajouter_paragraphe("h",paragraphe_i)


cle = histoire.get_paragraphes_keys()
print(cle)
# Début de l'histoire
id_actuelle = "intro"
while True:
    histoire.choix_joueur(id_actuelle)
    choix = input().lower()
    if choix in cle:
        id_actuelle = choix
        if id_actuelle == "fin":
            break
    else:
        print("Choix invalide. Veuillez choisir parmi les possibilités.")
        #finir de mettre les choix
        #pas de retour en arriere si index de l'id actuelle ne peut pas appeler un id precedent
        #probleme ce sont des dictionnaire donc pas d'index
        #stocké les endroit visite ou alors supprimé les items deja passé et si une situation rejoint un ancien item 
        #c'est pas grave car l'histoir est faite main donc un copié collé est possible mais double le nombre de chose a écrire
