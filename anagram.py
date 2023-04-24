#!/usr/bin/env python3
import itertools
import sys

nom,*argv = sys.argv
mot,fichier = argv

def usage():
    print(f"Usage :{nom} <mot> <fichier>\nPlace dans le <fichier> la liste des anagrames de <mot>")

if len(argv)!=2:
    usage()
else:
    A=["".join(e)for e in itertools.permutations(argv[0],len(argv[0]))]
    fichier = open(fichier, "w")
    for a in A:
        fichier.write(f"{a}\n")
    fichier.close()
