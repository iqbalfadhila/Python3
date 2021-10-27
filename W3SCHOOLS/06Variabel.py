# """
# ###Python Variable

# #Variabel
#     Variabel adalah wadah untuk menyimpan data

# #Membuat variabel
# python tidak memiliki perintah untuk mendlarasikan variabel.
# variabel dibuat saat anda pertama kali menetapkan nilai padanya
# contoh
# x = 5
# y = "Iqbal"

# print(x)
# print(y)

# #Casting Variable
# Jika kita ingin menentukan tipe data dari suatu variabel, ini dapat dilakukan dengan casting
# contoh
# x = str(3)
# y = int(3)
# z = float(3)

# #mendapatkan tipenya
# kita bisa mendapatkan tipe data variable dengan fungsi type()
# contoh
# x = 5
# y = "Iqbal"
# print(type(x))
# print(type(y))

# #kutip tunggal atau ganda?
# Variabel string dapat dideklarasikan dengan menggunakan tanda kutip tunggal dan ganda
# contoh
# x = "Iqbal"
# #sama dengan
# x = 'Iqbal'

# Hal sensitif
# nama variabel peka huruf besar/kecil
# contoh
# a = 4
# A = "Iqbal"
# #variabel A tidak akan menimpa a

# ### Penamaan variabel
# Sebuah variable dapat memiliki penamaan pendek(seperti x dan y) atau nama yang lebih deskriptif(umur, nama depan, nama belakang), Aturan untuk variabel python
#     *Nama variabel harus dimullai dengan huruf atau karakter garis bawah
#     *Nama Variabel tidak boleh diawali oleh angka
#     *Nama Variabel hanya boleh berisi karakter alfanumerik dan garis bawah(A-Z, 0-9, dan _)
#     *Nama Variabel peka huruf kecil / besar (usia, Usia, dan USIA adalah 3 variabel berbeda)
# Contoh
# Nama variabel legal:
# myvar = "Iqbal"
# my_var = "Iqbal"
# _my_var = "Iqbal"
# myVar = "Iqbal"
# MYVAR = "Iqbal"
# myvar2 = "Iqbal"

# nama variabel ilegal
# 2myvar = "Iqbal"
# my-var = "Iqbal"
# my var = "Iqbal"

# # nama variabel multi kata
# Nama variabel dengan lebih dari 1 kata bisa jadi sulit dibaca, Ada beberapa taknik yang dapat digunakan  untuk membuatnya mudah dibaca:
#     *Camel Case
#     Setiap kata, kecuali yang pertama, dimulai dengan huruf kapital
#     Contoh : myVariableName = "Iqbal"
#     *Pascal Case
#     Setiap kata dimulai dengan huruf kapital:
#     Contoh : MyVariableName = "Iqbal"
#     *Snake Case
#     Setiap kata dipisah oleh karacter underscore:
#     contoh : my_variabel_name = "Iqbal"

# """

# # # Python variabel - menetapkan beberapa nilai
# # banyak nilai ke beberapa variable
# # python dapat menetapkan nilai ke beberapa variabel dalam 1 baris:
# # Contoh
# x, y, z = "Orange", "Banana", "Cherry"
# print(x)
# print(y)
# print(z)
# # Note : Pastikan jumlah variabel sesuai dengan jumlah nilai atau kita akan mendapatkan kesalahan

# # # # Satu nilai kebeberapa variabel
# # dan kita dapat menetapkan nilai yang sama ke beberapa variabel dalam satu baris
# x = y = z = "Orange"
# print(x)
# print(y)
# print(z)

# # Unpack a collaction
# # Jika kita memiliki kumpulan nilai dalam list, tuple, dll. python memungkinkan anda mengekstrak nilai di dalam variabel. ini disebut unpacking
# # Contoh unpack list
# fruit = ['apple', 'banana', 'cherry']
# x, y, z = fruit
# print(x)
# print(y)
# print(z)


# # Python Output Variable

# # output variable
# # Pernyataan print python sering digunakan untuk menampilkan variabel.
# # Untuk menggabungkan teks dengan variable, python menggunakan karakter +
# # Contoh
# x = 'awesome'
# print('Python is ' + x)

# # kita juga dapat menggunakan karakter + untuk menambahkan variable ke variable lain
# x = 'Python is '
# y = 'awesome'
# z = x + y
# print(z)

# # untuk angka, karakter + berfungsi sebagai operator matematika:
# x = 5
# y = 10
# print(x + y)

# # Jika mencoba menggabungkan string dan angka,Python akan memberi kesalakan (error)
# # x = 5
# # y = 'iqbal'
# # print(x+y)


# # Global Variable
# # Variabel yang dibuat diluar function dikenal sebagai variabel global.global variable dapat digunakan oleh semua orang, baik didalam fungsi maupun diluar.
# # Contoh membuat variable dluar function dan digunakan didalam function:
# x = 'awesome'


# def myfunc():
#     print('Python is ' + x)


# myfunc()

# # Jika anda membuat variable dengan nama yang sama didalam function, variable ini bersifat lokal dan hanya dapat digunakan di dalam function tersebut. variable global dengan nama yang sama akan tetap seperti semula, global dan dengan nilai aslinya.
# # contoh membuar variabel dalam function dengan nama yang sama dengan variabel global
# x = 'awesome'


# def myfunc():
#     x = 'fantastic'
#     print('Python is ' + x)


# myfunc()

# print('Python is ' + x)

# # The global keyword

# # Biasanya, ketika membuat variable di dalam function, vartiabel itu bersifat lokal dan hanya dapat digunakan di dalam function
# # untuk membuat variabel global didalam suatu function, dapat menggunakan global keyword
# # Contoh, Jika menggunakan global keyword, variabel tersebut termasuk dalam lingkup global


# def myfunc():
#     global x
#     x = 'fantastic'


# myfunc()

# print('Python is ' + x)

# # Contoh, untuk mengubah nilai variable global di dalam function, variabel tersebut menggunakan global keyword

# x = 'awesome'


# def myfunc():
#     global x
#     x = 'fantastic'


# myfunc()

# print('Python is ' + x)
