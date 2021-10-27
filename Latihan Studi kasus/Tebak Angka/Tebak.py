'''membuat tebak angka range 1-10 dengan 3 kali kesempatan'''
from random import randint

occasion = 1
while occasion < 3:
    guess = input("Tebak angka range(1-10) : ")

    for i in range(10):
        comp = randint(1, 10)

        print(comp)
    occasion += 1
