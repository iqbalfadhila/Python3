# Python String

# String
'''
String Dalam Python Dikelilingi oleh tanda kutip tunggal atau tanda kutip ganda.
'Halo ' sama dengan "Halo"
Kita dapat menampilkan string literal dengan print() fungsi:
Contoh :
'''
print('Hello')
print("Hello")

# Menetapkan string ke variable
# Menetapkan string ke variable dilakukan dengan nama variable diikuti dengan tanda sama dengan dan string:
# Contoh
a = 'Hello'
print(a)

# String multiline
# Kita dapat menetapkan string multiline ke variable dengan menggunakan tiga tanda kutip
# Contoh : menggunakan tiga tanda kutip
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Contoh : tanda kutip tunggal
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

# String adalah Array
'''
Seperti banyak bahasa pemrograman popular lainnya, string dalam python adalah array byte yang mewakili karakter unicode

namun, python tidak memiliki tipe data karakter, karena tunggal hanyalah string dengan panjang 1.

Tanda kurung siku dapat digunakan untuk mengakses elemen string.

Contoh String adalah Array
'''
print('\n-Contoh String adalah array')

a = 'Hello, World!'
print('-', a[1])

# Looping melalui String
# Karena String adalah array, kita dapat mengulang karakter dalam string, dengan for loop

# Contoh Loop melalui string
print('\n-Loop String')

for x in 'banana':
    print(' ', x)

# Panjang String
# untuk mendapatkan panjang string, , gunakan len() fungsi
# Contoh : len() mengembalikan panjang string

print('\n-String dengan len()')
a = 'Hello, world!'
print(len(a))


# Check String
# uNtuk dapat memeriksa apakah ada frasa atau karakter tertentu dalam sebuah string, kita dapat menggunakan kata kunci `in`
# Contoh : memeriksa apakah 'free' ada dalam teks
print('\n-Check String menggunakan `in`')
txt = 'The best things in life are free!'
print(txt)
print(' free' in txt)

# Menggunakan If statement
print('\n-Check String menggunakan `in`, dengan statement if')
txt = 'The best things in life are free!'
print(txt)
if ' free' in txt:
    print('Ya, `free` ada ')

# Cek String dengan `not in`
print('\n-Check String menggunakan `not in`')
txt = 'The best things in life are free!'
print(txt)
print('expensive' not in txt)

# Menggunakan statement if
print('\n-Check String menggunakan `not in`, dengan statement if')
txt = 'The best things in life are free!'
print(txt)
if 'expensive' not in txt:
    print('Tidak, `expensive` tidak ada')


# Slicing Strings

print('\n-Slicing Strings')
b = 'Hello, World!'
print(b[2:5])

print('\n-Slice dari awal')
b = 'Hello, World!'
print(b[:5])

print('\n-Slice sampai akhir')
b = 'Hello, World!'
print(b[2:])

print('\n-Slice dengan Negatif indeks')
b = 'Hello, World!'
print(b[-5:-2])


# Modify String
print('\n\n---Modify String')

# Upper Case (Huruf Besar)
print('\n-Upper Case')
a = 'Hello, World!'
print(a.upper())

# Lower Case (Huruf Kecil)
print('\n-Lower Case')
a = 'Hello, World!'
print(a.lower())

# Remove Whitespace(Mengghapus Spasi)
print('\n-Remove Whitespace (Menghapus Spasi)')
a = 'Hello, World!'
print(a.strip())

# Replace String
print('\n-Replace String (Mengganti String)')
a = 'Hello, World!'
print(a.replace('H', 'J'))

# Split String
print('\n-Split String (Membelah String)')
a = 'Hello, World!'
print(a.split(','))


# String Concetenation (Penggabungan String)
print('\n\n---String Concetenation (Penggabungan String)')

a = 'Hello'
b = 'World'
c = a + b
print(c)
# Or
c = a + ' ' + b
print(c)

# Format String
print('\n\n---Format String')

# Example 1
print('\n-Example 1')
age = 36
txt = 'My name is Iqbal Fadhila Rahman, and i am {}'
print(txt.format(age))

# Example 2
print('\n-Example 2')
quantity = 3
itemno = 567
price = 49.95
myorder = 'I want {} pieces of item {} for {} dollars.'
print(myorder.format(quantity, itemno, price))

# Example 3
print('\n-Example 3')
quantity = 3
itemno = 567
price = 49.95
myorder = 'I want to pay {2} dollars for {0} pieces of item {1}'
print(myorder.format(quantity, itemno, price))

# Excape Characters
print('\n\n Excape Character')

# Contoh menggunakan backslash
print('Contoh menggunakan Backslash')
txt = 'We are the so-called\'Viking\'from the north.'
print(txt)
# Excape character lainnya
'''
\'      Single Quote
\\      Backslash
\n      New Line
\r      Carriage return
\t      Tab
\b      Backspace
\f      Form feed
\ooo    Octal value
\xhh    Hex value
'''

# String Method
'''
Deskripsi           Metode
capitalize()        Mengonversi karakter pertama menjadi huruf besar
casefold()          Mengubah string menjadi huruf kecil
center()            Mengembalikan string terpusat
count()             Mengembalikan berapa kali nilai tertentu muncul dalam string
encode()            Mengembalikan versi string yang disandikan
endwith()           Mengembalikan nilai true jika string diakhiri dengan nilai yang ditentukan
expandtabs()        Mengatur ukuran tab string
find()              Mencari string untuk nilai yang ditentukan dan mengembalikan posisi di mana ia ditemukan
format()            Memformat nilai yang ditentukan dalam string
format_map()        Memformat nilai yang ditentukan dalam string
index()             Mencari string untuk nilai tertentu dan mengembalikan posisi di mana ia ditemukan
isalnum()           Mengembalikan True jika semua karakter dalam string adalah alfanumerik
isalpha()           Mengembalikan True jika semua karakter dalam string ada dalam alfabet
isdecimal()         Mengembalikan True jika semua karakter dalam string adalah desimal
isdigit()           Mengembalikan True jika semua karakter dalam string adalah angka
isidentifier()      Mengembalikan True jika string adalah pengidentifikasi
islower()           Mengembalikan True jika semua karakter dalam string adalah huruf kecil
isumeric()          Mengembalikan True jika semua karakter dalam string adalah numerik
isprintable()       Mengembalikan True jika semua karakter dalam string dapat dicetak
isspace()           Mengembalikan True jika semua karakter dalam string adalah spasi putih
istitle()           Mengembalikan True jika string mengikuti aturan judul
isupper()           Mengembalikan True jika semua karakter dalam string adalah huruf besar
join()              Menggabungkan elemen-elemen dari iterable ke akhir string
ljust()             Mengembalikan versi string yang dibenarkan kiri
lower()             Mengubah string menjadi huruf kecil
lstrip()            Mengembalikan versi trim kiri dari string
maketrans()         Mengembalikan tabel terjemahan untuk digunakan dalam terjemahan
partisi()           Mengembalikan tuple di mana string dipecah menjadi tiga bagian
replace()           Mengembalikan string di mana nilai tertentu diganti dengan nilai tertentu
rfind()             Mencari string untuk nilai yang ditentukan dan mengembalikan posisi terakhir di mana ia ditemukan
rindex()            Mencari string untuk nilai tertentu dan mengembalikan posisi terakhir di mana ia ditemukan
rjust()             Mengembalikan versi string yang dibenarkan dengan benar
rpartition()        Mengembalikan tuple di mana string dibagi menjadi tiga bagian
rsplit()            Membagi string pada pemisah yang ditentukan, dan mengembalikan daftar
rstrip()            Mengembalikan versi trim kanan dari string
split()             Membagi string pada pemisah yang ditentukan, dan mengembalikan daftar
splitlines()        Membagi string pada jeda baris dan mengembalikan daftar
startwith()         Mengembalikan nilai true jika string dimulai dengan nilai yang ditentukan
strip()             Mengembalikan versi string yang dipangkas
swapcase()          Tukar kasus, huruf kecil menjadi huruf besar dan sebaliknya
title()             Mengonversi karakter pertama setiap kata menjadi huruf besar
translate()         Mengembalikan string yang diterjemahkan
upper()             Mengubah string menjadi huruf besar
zfill()             Mengisi string dengan sejumlah nilai 0 yang ditentukan di awal
'''
