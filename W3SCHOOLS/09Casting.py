# Casting

# Tentukan Tipe Variabel

# Mungkin ada saatnya kita ingin menentukan tipe data pada variable Ini bisa dilakukan dengan casting. Python adalah bahasa berorientasi objek, dan karena itu menggunakan class untuk mendefinisakan tipe data, termasuk tipe primitifnya.

# Casting dengan python dilakukan dengan menggunakan fungsi konstruktor :
# int() - Membangun bilangan bulat dari literal bilangan bulat, literal float (dengan menghapus semua desimal), atau literal string (menyediakan string mewakili bilangan bulat)
# float() - membangun angka float dari literal integer, literal float atau string(menyediakan string mewakili float dan integer)
# str() - membangun string dari berbagai tipe data, termasuk string, literal integer, dan literal float

# Contoh : Integer

print('='*5, 'Integer', '='*5)
x = int(1)
y = int(2.8)
z = int('3')

# Contoh : Float
print('='*5, 'Float', '='*5)
x = float(1)
y = float(2.8)
z = float('3')
w = float('4.2')

# Contoh : String
print('='*5, 'String', '='*5)
x = str('s1')
y = str(2)
z = str(3.0)
