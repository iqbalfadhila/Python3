from random import random
# User pilih
while True:

    p = input("Pilih : Gunting, Kertas, Batu : ")

    comp = random()
    if comp < 0.34:
        comp = "Gunting"
    elif 0.34 <= comp < 0.67:
        comp = "Kertas"
    else:
        comp = "Batu"

    if p == comp:
        print("SERI!")
    elif p == "Gunting":
        print("Menang") if comp == "Kertas" else print("kalah")
    elif p == "Kertas":
        print("Menang") if comp == "Batu" else print("Kalah")
    elif p == "Batu":
        print("Menang") if comp == "Gunting" else print("Kalah")
    else:
        print("memilih pilihan yang salah")

    print(f"anda memilih {p} dan komputer memilih {comp}")
    ulang = input("Apakah mau lanjut?")
    if ulang == "ya":
        ulang == True
    else:
        ulang == False
