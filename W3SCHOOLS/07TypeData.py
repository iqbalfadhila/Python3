# Python Type Data

# Tipe data bawaan
# Dalam Pemrograman, tipe data merupakan konsep penting
# Variabel dapat menyimpan data dari tipe yang berbeda dan tipe yang berbeda dapat melakukan hal yang berbeda.
# Python memiliki tipe data bawaan, berikut secara default, dalam ketegori ini
# Tipe teks : str(string)
# Tipe numerik : int(integer), float, dan kompleks
# Tipe Urutan(sequence) : list, tuple, range
# Tipe mapping : dict
# Tipe Set : set, frozenset
# Tipe Boolean  : bool
# Tipe biner : bytes, bytearray, memoryview

# Getting type data
# kita bisa mendapatkan tipe data objek apa pun dengan menggunakan fungsi type():
# Contoh, Cetak type data variable x:
x = 5
print(type(x))

# Setting the data type
# Di python tipe data diatur saat anda menetapkan nilai ke variable:

# String
x = "Hello World"
# display x:
print(x)
# display the data type of x:
print(type(x))

# int (Integer)
x = 20
# display x:
print(x)
# display the data type of x:
print(type(x))

# float
x = 20.5
# display x:
print(x)
# display the data type of x:
print(type(x))

# Complex
x = 1j
# display x:
print(x)
# display the data type of x:
print(type(x))

# List
x = ['apple', 'banana', 'cherry']
# display x:
print(x)
# display the data type of x:
print(type(x))

# Tuple
x = ('apple', 'banana', 'cherry')
# display x:
print(x)
# display the data type of x:
print(type(x))

# Range
x = range(6)
# display x:
print(x)
# display the data type of x:
print(type(x))

# Dict
x = {'name': 'Iqbal', 'age': 19}
# display x:
print(x)
# display the data type of x:
print(type(x))

# Set
x = {'apple', 'banana', 'cherry'}
# display x:
print(x)
# display the data type of x:
print(type(x))

# Frozenset
x = frozenset({'apple', 'banana', 'cherry'})
# display x:
print(x)
# display the data type of x:
print(type(x))

# Boolean
x = True
# display x:
print(x)
# display the data type of x:
print(type(x))

# bytes
x = b"Hello"
# display x:
print(x)
# display the data type of x:
print(type(x))

# Bytearray
x = bytearray(5)
# display x:
print(x)
# display the data type of x:
print(type(x))

# Mamoryview
x = memoryview(bytes(5))
# display x:
print(x)
# display the data type of x:
print(type(x))

# Setting the specific Data Type
# Jika anda ingin menentukan tipe data, anda dapat menggunakan fungsi kontruktor berikut:

# String
x = str("Hello World")
# display x:
print(x)
# display the data type of x:
print(type(x))

# Integer
x = int(20)
# display x:
print(x)
# display the data type of x:
print(type(x))

# Float
x = float(20.5)
# display x:
print(x)
# display the data type of x:
print(type(x))

# Complex
x = complex(1j)
# display x:
print(x)
# display the data type of x:
print(type(x))

# List
x = list(('apple', 'banana', 'cherry'))
# display x:
print(x)
# display the data type of x:
print(type(x))

# Tuple
x = tuple(('apple', 'banana', 'cherry'))
# display x:
print(x)
# display the data type of x:
print(type(x))

# Range
x = range(6)
# display x:
print(x)
# display the data type of x:
print(type(x))

# Dict
x = dict(name='john', age=19)
# display x:
print(x)
# display the data type of x:
print(type(x))

# Set
x = set(('apple', 'banana', 'cherry'))
# display x:
print(x)
# display the data type of x:
print(type(x))

# frozenset
x = frozenset(('apple', 'banana', 'cherry'))
# display x:
print(x)
# display the data type of x:
print(type(x))

# Boolean
x = bool(5)
# display x:
print(x)
# display the data type of x:
print(type(x))

# Bytes
x = bytes(5)
# display x:
print(x)
# display the data type of x:
print(type(x))

# bytearray
x = bytearray(5)
# display x:
print(x)
# display the data type of x:
print(type(x))

# memoryview
x = memoryview(bytes(5))
# display x:
print(x)
# display the data type of x:
print(type(x))
