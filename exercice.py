#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_first_part_of_name(name):
	liste = name.split('-')
	prenom = liste[0].capitalize()
	return "Bonjour " + prenom

def get_random_sentence(animals, adjectives, fruits):
	phrase = "Aujourd’hui, j’ai vu un %s s’emparer d’un panier %s plein de %s."
	liste_mots = []
	for word_set in (animals, adjectives, fruits):
		liste_mots += [word_set[random.randrange(0,len(word_set))]] 
	return phrase % tuple(liste_mots) 

def encrypt(text, shift):
	return ""

def decrypt(encrypted_text, shift):
	return ""


if __name__ == "__main__":
	parrot = "jEaN-MARC"
	print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

	animals = ("chevreuil", "chien", "pigeon")
	adjectives = ("rouge", "officiel", "lourd")
	fruits = ("pommes", "kiwis", "mangue")
	print(get_random_sentence(animals, adjectives, fruits))
	
	print(encrypt("ABC", 1))
	print(encrypt("abc 123 XYZ", 3))
	print(decrypt("DEF 123 ABC", 3))
