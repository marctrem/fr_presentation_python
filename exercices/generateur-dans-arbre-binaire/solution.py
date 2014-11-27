#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# On fait usage de PEP 380. :)

class ArbreBinaire:

    class Noeud:
        def __init__(self, valeur):
            self.valeur = valeur

            self.gauche = None
            self.droite = None

        def __str__(self):
            return str(self.valeur)


    def __init__(self):
        self.racine = None

    def __inserer_inner(self, valeur, noeud):

        if noeud.valeur == valeur:
            return

        elif noeud.valeur < valeur:
            if noeud.droite is None:
                noeud.droite = self.Noeud(valeur)
                return
            else:
                self.__inserer_inner(valeur, noeud.droite)

        elif noeud.valeur > valeur:
            if noeud.gauche is None:
                noeud.gauche = self.Noeud(valeur)
                return
            else:
                self.__inserer_inner(valeur, noeud.gauche)


    def inserer(self, valeur, noeud=None):

        if noeud is None:
            if self.racine is None:
                self.racine = self.Noeud(valeur)
                return
            else:
                noeud = self.racine

        if noeud.valeur == valeur:
            # Ici, nous sommes tombé sur un noeud contenant la valeur que nous tentons d'insérer.
            # Nous n'avons rien à faire.
            return

        elif noeud.valeur < valeur:
            # Ici, nous sommes tombés sur un noeud contetant une valeur inférieure à celle que nous insérons.
            if noeud.droite is None:
                noeud.droite = self.Noeud(valeur)
                return
            else:
                self.inserer(valeur, noeud.droite)

        elif noeud.valeur > valeur:
            # Ici, nous sommes tombés sur un noeud contetant une valeur supérieure à celle que nous insérons.
            if noeud.gauche is None:
                noeud.gauche = self.Noeud(valeur)
                return
            else:
                self.inserer(valeur, noeud.gauche)


    def parcours_gen(self, noeud=None):

        if noeud is None:
            if self.racine is None:
                return
            else:
                noeud = self.racine

        if noeud.gauche is not None:
            yield from self.parcours_gen(noeud.gauche)

        yield noeud.valeur

        if noeud.droite is not None:
            yield from self.parcours_gen(noeud.droite)


a = ArbreBinaire()

for x in [5, 3, 5, 6, 9, 4]:
    a.inserer(x)

g = a.parcours_gen()

# On consomme le générateur dans une liste
li = list(g)

# On vérifie!
if li == [3, 4, 5, 6, 9]:
    print("Bravo!", li)
else:
    print("Nope", li)


