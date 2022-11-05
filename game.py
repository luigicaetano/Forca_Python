import random

lista = open("palavras.txt").read().split()
print(random.choice(lista))
