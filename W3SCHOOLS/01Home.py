# print("Hello World!")

x = int(input('Input Panjang Deret : '))

fibo = [0, 1]

for i in range(2, 6):
    index1 = i - 2
    index2 = i - 1
    index3 = index1 + index2
    print(
        f'Deret ke {i + 1} adalah index-{index1} + index-{index2} = {index3}')
    fibo.append(index3)

print(fibo)
# List_harga_barang = [50000, 60000, 100000, 150000]
# List_diskon = [0.1, 0.2, 0.3, 0.4]

# hasil1 = [List_harga_barang[0] - (List_harga_barang[0] * List_diskon[0])]

# hasil2 = [List_harga_barang[1] - (List_harga_barang[1] * List_diskon[1])]

# hasil3 = [List_harga_barang[2] - (List_harga_barang[2] * List_diskon[2])]

# hasil4 = [List_harga_barang[3] - (List_harga_barang[3] * List_diskon[3])]

# hasil = hasil1 + hasil2 + hasil3 + hasil4
# print(hasil)
# len_data = len(List_harga_barang)

# for i in range(len_data):
#     diskon = List_harga_barang[i] * List_diskon[i]
#     hasil = List_harga_barang[i] - diskon
#     print(
#         f'Harga Barang {List_harga_barang[i]} diskon {List_diskon[i]} jadi {hasil}')
# string = ""
# bar = 1

# # Looping Baris
# while bar <= 5:
#     kol = bar

#     # Looping Kolom
#     while kol > 0:
#         string = string + "*"
#         kol = kol - 1

#     string = string + "\n"
#     bar = bar + 1
# print(string)

# a, b, c = 1, 1, 0
# for i in range(1, 11):
#     print(a)
#     c = a+b
#     a = b
#     b = c
# tahun = int(input('Input tahun  : '))
# if tahun > 2010:
#     if tahun % 4 == 0:
#         print(f'Tahun yang anda input : {tahun} adalah tahun Kabisat')
#     else:
#         print(f'Tahun yang anda input : {tahun} adalah tahun Basit')
# else:
#     print('Anda Harus input tahun lebih dari tahun 2010')
# konversi = input('Konversi(R/F/K) : ').upper()
# elif konversi == 'F':
#     hasil = 9 / 5 * c + 32
#     print('Hasil : ', hasil)
# elif konversi == 'K':
#     hasil = c + 237.15
#     print('Hasil : ', hasil)
