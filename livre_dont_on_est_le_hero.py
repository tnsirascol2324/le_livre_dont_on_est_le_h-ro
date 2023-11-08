import sys

class Joueur:
    '''
    Classe Joueur : représente un joueur.

    Attributs d'instance :
    - self.nom (str): Le nom du joueur.

    Méthode constructeur :
     __init__(self, pNom (str)): Initialise un objet Joueur avec un nom.

    Méthodes :
     __str__(self): Retourne une représentation sous forme de chaîne de caractères du joueur.
    '''

    def __init__(self, pNom):
        self.nom = pNom
   
    def __str__(self):
        return f"Joueur: {self.nom}"

# Création d'un joueur avec son nom
utilisateur = Joueur(input("Quel est votre nom ?"))
print(utilisateur)
etat = 0

class Paragraphe:
    '''
    Classe Paragraphe : gère la création de paragraphes et l'affichage de l'histoire.

    Attributs d'instance :
    - self.__description (str): La description du paragraphe.
    - self.__mortel (int): Un indicateur de mortalité (0 pour non mortel, 1 pour mortel).

    Méthode constructeur :
    __init__(self, paragraphe (str), pmortel=0): Initialise un objet Paragraphe avec une description et un indicateur de mortalité.

    Méthodes :
    afficher(self): Permet d'afficher la description du paragraphe et gère les situations mortelles.
    '''

    def __init__(self, paragraphe, pmortel=0,pfin=0):
        self.__description = paragraphe
        self.__mortel = pmortel
        self.__fin = pfin

    def afficher(self):
        print(self.__description)
        if self.__mortel == 1:
            etat = 1
            print("Vous êtes mort.")
            sys.exit()
        if self.__fin==1:
            print("fin chelou")
            sys.exit()

class Histoire:
    '''
    Classe Histoire : permet à l'histoire de se dérouler et au joueur de faire des choix.

    Attributs d'instance :
    - self.paragraphes (dict): Un dictionnaire de paragraphes avec des identifiants en tant que clés.
    - self.paragraphes_visites (set): Un ensemble de paragraphes déjà visités.

    Méthode constructeur :
    __init__(self): Initialise un objet Histoire avec une liste de paragraphes et un suivi des paragraphes visités.

    Méthodes :
    ajouter_paragraphe(self, id (str), paragraphe (Paragraphe)): Ajoute un paragraphe à l'histoire.
    choix_joueur(self, id (str)): Permet au joueur de faire un choix et affiche le paragraphe correspondant, gérant les paragraphes visités.
    get_paragraphes_keys(self): Retourne les identifiants des paragraphes disponibles.
    '''

    def __init__(self):
        self.paragraphes = {}
        self.paragraphes_visites = set()

    def ajouter_paragraphe(self, id, paragraphe):
        self.paragraphes[id] = paragraphe

    def choix_joueur(self, id):
        if id not in self.paragraphes:
            print("Ce paragraphe n'existe pas.")
        elif id in self.paragraphes_visites:
            print(f"{utilisateur.nom}, impossible de rebrousser chemin.")
        else:
            self.paragraphes[id].afficher()
            self.paragraphes_visites.add(id)
    
    def get_paragraphes_keys(self):
        return self.paragraphes.keys()

# Création des paragraphes
paragraphe_intro = Paragraphe("Vous êtes dans un couloir avec deux portes devant vous. \n (a)aller à droite\n (b)aller à gauche\n")
paragraphe_a = Paragraphe("Vous avez pris la porte de droite.\nDevant vous se trouve un gobelin,vous le défiez il vous coupe un bras . \n(c)fuire \n(d)continuer le combat \n(e)le supplier")
paragraphe_b = Paragraphe("Vous avez pris la porte de gauche.\nDevant vous se trouve un dieu, il ressemble à un crackead.\n Il vous demande à boire\n(f)lui donner \n(g)lui voler sa conso \n(h)fuir")
paragraphe_c = Paragraphe("Vous vous retournez pour vous enfuir mais le gobelin vous rattrape et vous tue",1)
paragraphe_d = Paragraphe("Le gobelin vous fonce dessus, vous l'esquivez et le tuez, vous sortez de la pièce et découvrez que vous êtes dans un donjon, vous regardez au loin et remarquez une étrange forme se déplaçant en rampant tel un chien s'étant fait faucher. Vous le fixez si intensément qu'il sentit votre regard \ncontinuer à le fixer \npartir en courant \nse cacher")
paragraphe_e = Paragraphe("Vous êtes pitoyable, même le gobelin semble avoir pitié mais ne vous épargne pas pour autant. Il vous coupe la tête puis vous utilise comme siège ")
paragraphe_f = Paragraphe("Vous lui donnez un coca bien frais, pour vous récompenser, il vous téléporte hors de danger, vous ouvrez les yeux et remarquez que vous êtes en réalité à une soirée. Vous vous souvenez que vous êtes bourré à mort car votre femme vous a trompé.",0,1)
paragraphe_g = Paragraphe("Vous lui volez sa conso, il se met à hurler et se transforme en un horrible monstre avec des crânes de bébé accrochés à lui. Effrayé, vous courez, mais il vous rattrape et vous arrache les tripes en vous gardant vivant. Vous mourez dans d'atroces souffrances.",1)
paragraphe_h = Paragraphe("Vous partez à toute vitesse sans demander votre reste. Vous sortez de la pièce et découvrez que vous êtes dans un donjon, vous regardez au loin et remarquez une étrange forme se déplaçant en rampant tel un chien s'étant fait faucher. Vous le fixez si intensément qu'il sentit votre regard \ncontinuer à le fixer \npartir en courant \nse cacher")

# Ajout des paragraphes à l'histoire
histoire = Histoire()
histoire.ajouter_paragraphe("intro", paragraphe_intro)
histoire.ajouter_paragraphe("a", paragraphe_a)
histoire.ajouter_paragraphe("b", paragraphe_b)
histoire.ajouter_paragraphe("c", paragraphe_c)
histoire.ajouter_paragraphe("d", paragraphe_d)
histoire.ajouter_paragraphe("e", paragraphe_e)
histoire.ajouter_paragraphe("f", paragraphe_f)
histoire.ajouter_paragraphe("g", paragraphe_g)
histoire.ajouter_paragraphe("h", paragraphe_h)

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
