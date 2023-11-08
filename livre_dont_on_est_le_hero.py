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
paragraphe_d = Paragraphe("vous tuer le gobelin in extremis puis voyagé sur un chemin lugubre(i)")
paragraphe_e = Paragraphe("Vous êtes pitoyable, même le gobelin semble avoir pitié mais ne vous épargne pas pour autant. Il vous coupe la tête puis vous utilise comme siège ",1)
paragraphe_f = Paragraphe("Vous lui donnez un coca bien frais, pour vous récompenser, il vous téléporte hors de danger, vous ouvrez les yeux et remarquez que vous êtes en réalité à une soirée. Vous vous souvenez que vous êtes bourré à mort car votre femme vous a trompé.",0,1)
paragraphe_g = Paragraphe("Vous lui volez sa conso, il se met à hurler et se transforme en un horrible monstre avec des crânes de bébé accrochés à lui. Effrayé, vous courez, mais il vous rattrape et vous arrache les tripes en vous gardant vivant. Vous mourez dans d'atroces souffrances.",1)
paragraphe_h = Paragraphe("vous partez sans demander votre reste et voyagé sur un chemin lugubre(i)")
paragraphe_i = Paragraphe("Vous trouvez une épée magique cachée sous un rocher. Que faites-vous ?\n(j)La ramasser et partir à l'aventure\n(k)La laisser là où elle est")
paragraphe_j = Paragraphe("Vous avez pris l'épée magique. Elle brille d'une lueur puissante, et vous vous sentez invincible. Vous continuez à avancer. Soudain, vous rencontrez un dragon.\n(l)Le combattre\n(m)Fuir")
paragraphe_k = Paragraphe("Vous décidez de laisser l'épée magique sous le rocher et de continuer votre chemin. Vous arrivez dans une salle sombre. Il fait tellement noir que vous ne pouvez rien voir.\n(n)Allumer une torche\n(o)Continuer dans l'obscurité")
paragraphe_l = Paragraphe("Vous décidez de combattre le dragon avec l'épée magique. Vous vous battez courageusement, mais le dragon est bien trop puissant. Il vous crache du feu, et vous brûlez vif. Vous êtes mort.", 1)
paragraphe_m = Paragraphe("Vous choisissez de fuir le dragon. Vous courez à toute vitesse, mais il vous rattrape et vous dévore. Vous êtes mort.", 1)
paragraphe_n = Paragraphe("Vous allumez une torche. À la lumière, vous voyez un passage secret dans un coin de la salle. Vous décidez d'explorer le passage.\n(p)Entrer dans le passage secret\n(q)Revenir dans le couloir principal")
paragraphe_o = Paragraphe("Vous continuez à avancer dans l'obscurité. Vous trébuchez sur une pierre et tombez dans un piège mortel. Vous êtes mort.", 1)
paragraphe_p = Paragraphe("Vous entrez dans le passage secret. Il vous mène à une chambre au trésor remplie d'or et de joyaux. Vous avez réussi à terminer cette aventure avec succès !", 0, 1)
paragraphe_q = Paragraphe("Vous retournez dans le couloir principal. Vous êtes maintenant face à un choix crucial.\n(r)Prendre la porte de gauche\n(s)Prendre la porte de droite\n(t)Prendre une trappe caché sous le tapis")
paragraphe_r = Paragraphe("Vous choisissez de prendre la porte de gauche. Elle vous conduit à un jardin enchanté où vous vivez le reste de vos jours en paix. Vous avez réussi !", 0, 1)
paragraphe_s = Paragraphe("Vous choisissez de prendre la porte de droite. Elle vous conduit à un labyrinthe sans fin. Vous vous perdez et ne trouvez jamais la sortie. Vous êtes condamné à errer pour l'éternité.", 1)
paragraphe_t = Paragraphe("En prenant la trappe, vous vous trouvez dans une salle mystérieuse. Au centre de la salle, il y a une grande table avec un coffre verrouillé posé dessus. \n(u)Ouvrir le coffre\n(v)Revenir au couloir principal")
paragraphe_u = Paragraphe("Dans le coffre se trouvait une photo de votre ex avec écrit au dos 'force a toi mon reuf' de désespoir vous vous suicidé",1)
paragraphe_v = Paragraphe("En revenant au couloir principal, vous voyez une porte de sortie et une table avec un pichet de wisky \n(w)Prendre la port de sortie\n(x)Prendre le verre de wisky")
paragraphe_w = Paragraphe("vous passez la porte et vous retrouver dans un avion le 11 septempbre vous vous évanouissez",1)
paragraphe_fin = Paragraphe("")


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
histoire.ajouter_paragraphe("i", paragraphe_i)
histoire.ajouter_paragraphe("j", paragraphe_j)
histoire.ajouter_paragraphe("k", paragraphe_k)
histoire.ajouter_paragraphe("l", paragraphe_l)
histoire.ajouter_paragraphe("m", paragraphe_m)
histoire.ajouter_paragraphe("n", paragraphe_n)
histoire.ajouter_paragraphe("o", paragraphe_o)
histoire.ajouter_paragraphe("p", paragraphe_p)
histoire.ajouter_paragraphe("q", paragraphe_q)
histoire.ajouter_paragraphe("r", paragraphe_r)
histoire.ajouter_paragraphe("s", paragraphe_s)
histoire.ajouter_paragraphe("t", paragraphe_t)
histoire.ajouter_paragraphe("u", paragraphe_u)
histoire.ajouter_paragraphe("v", paragraphe_v)
histoire.ajouter_paragraphe("w", paragraphe_w)
histoire.ajouter_paragraphe("x", paragraphe_fin)


cle = histoire.get_paragraphes_keys()
print(cle)

# Début de l'histoire
id_actuelle = "intro"
while True:
    histoire.choix_joueur(id_actuelle)
    choix = input().lower()
    if choix in cle:
        id_actuelle = choix
        if id_actuelle=="x":
            print("")
            print("Vous buvez le verre et vous rendez compte qu'il se remplit comme par magie,\n vous décidé alors de vous installer dans cet endroit.\ncerte le danger est présent mais rien ne vaut du wisky gratuit\nVOILA UN HOMME UN VRAI")
            sys.exit()
    else:
        print("Choix invalide. Veuillez choisir parmi les possibilités.")

