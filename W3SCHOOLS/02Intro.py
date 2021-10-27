"""
What is python?
Python adalah bahasa pemrograman popular, Itu di buat oleh Goido Vaan rossum dan rilis pada 1991

ini dapat digunakan untuk :
    *Web Development(server-side),
    *Software Development,
    *mathematics,
    *system scripting

Apa yang bisa python lakukan?
    *Python dapat digunakan di server untuk membuat web aplikasi
    *Python dapat digunakan bersama perangkat lunak untuk membuat alur kerja
    *Python dapat terhubung ke sistem database, Itu juga dapat membaca dan memodifikasi file
    *Python dapat digunakan untuk menangani data besar dan melakukan metematika dengan kompleks,
    *Python dapat digunakan untuk pembuatan prototype cepat, atau mengambangan perangkat lunak siap produksi

Mengapa Python?
    *Python bekarja pada platform yang berbeda(windows, Mac, linux, Raspberry pi, dll)
    *Python memiliki sintaks yang sederhana yang mirip dengan bahasa inggris
    *Python memiliki sintaks yang memungkinkan pengembangan untuk menulis program dengan lebih sedikit barus daripada beberapa bahasa pemrograman lainnya
    *Python berjalan dengan interpreter, artinya kode dapat diekskusi segera setelah ditulis, ini berarti bahwa pembuatan prototipe bisa sangat cepat
    *Python dapat di perlakukan dengan cara prosedural, cara berorientasi objek atau cara fungsional.

Sintaks python dibanding dengan bahasa pemrograman lain
    *Python dirancang agar mudah dibaca, dan memiliki beberapa kesamaan dengan bahasa inggris dengan pengaruh dari matematika
    *Python menggunakan barus baru untuk menyelesaikan perintah, berbeda dengan bahasa pemrograman lain yang sering menggunakan titik koma atau tanda kurung
    *Python bergantung pada lekukan, penggunaan spasi, untuk mendefinisikan scope, seperti loop, function class.bahasa lain sering menggunakan kurung kurawal untuk tujuan ini.
"""
while True:
    a = int(input("A : "))

    if a >= 1 and a <= 200:
        b = int(input("B : "))

        if b >= 1 and b <= 200:
            c = int(input("C : "))
            if c >= 1 and c <= 200:
                break
            else:
                print("range angka hanya boleh 1 - 200 saja")
        else:
            print("range angka hanya boleh 1 - 200 saja")
    else:
        print("range angka hanya boleh 1 - 200 saja")

total = a + b + c

if total is not 180:
    print("Bukan Segitiga")
else:
    if a > 180 or b > 180 or c > 180:
        print("Bukan Segitiga")
        quit()
    else:
        if a is not b is not c:
            print("Segitiga tak beraturan")
        elif a is b is c:
            print("Segitiga sama sisi")
        elif a is b or a is c or b is c:
            print("Segitiga sama kaki")
