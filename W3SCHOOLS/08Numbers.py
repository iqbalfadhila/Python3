# Python Numbers
# ada 3 numerik dalam python
# int
# float
# complex

# Variabel tipe numerik dibuat saat anda menetapkan nilai padanya
# contoh
import random
x = 1   # int
y = 2.8  # float
z = 1j  # complex
# untuk memverifikasi jenis objek apa pun dengan python, gunakan fungsi type
# contoh
print(type(x))
print(type(y))
print(type(z))

# Int

# int, atau integer, adalah bilangan bulat, positif atau negatif, tanpa desimal, dengan panjang tak terbatas
# contoh integer
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

# Float
# Float, or "floating point number" is a number, positive or negative,yang mengandung satu atau lebih decimal
# contoh flaot
x = 1.10
y = 1.0
z = -33.59

print(type(x))
print(type(y))
print(type(z))

# Float juga bisa berupa angka ilmiah dengan 'e' untuk menunjukkan kekuatan 10
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

# Complex
# Bilangan komleks ditulis dengan 'j' sebagai bagian imajiner
# contoh
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))


# Type Convertion
# kita dapat mengkonversi dari 1 jenis ke jenis lainnya dengan metode int(), flaot(), dan kompleks():
# Contoh
x = 1  # int
y = 2.8  # float
z = 1j  # complex

# convert dari int ke float
a = float(x)

# convert dari float ke int
b = int(y)

# convert int ke complex
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# Note : kita tidak dapat menkonversi bilangan konpleks menjadi jenis bilangan lain

# Random number
# Python tidak memiliki fungsi random() untuk membuat angka acak, tetapi python memiliki modul bawaan yang disebut random yang dapat digunakan untuk membuat angka acak

# contoh, import madul acak, dan menampil nomor acak antara 1 dan 9


print(random.randrange(1, 10))
