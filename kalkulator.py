print("=======================")
print("=====Kalkulator v1=====")
print("=======================")
print("Menu :")
print("1. Penjumlahan  ||  3.Perkalian")
print("2. Pengurangan  ||  4.Pembagian")
print("-------------------------------")
x = int(input("Masukkan Pilihan Anda : "))

if (x > 0 and x <= 4) :
    angka1 = int(input("Masukkan Angka Pertama : "))
    angka2 = int(input("Masukkan Angka Kedua : "))

    if (x == 1) :
        total = angka1 + angka2
    elif (x == 2) : 
        total = angka1 - angka2
    elif (x == 3) :
        total = angka1 * angka2
    elif (x == 4) :
        total = angka1 / angka2
    print("Hasilnya adalah", total)
else :
    print("Hanya dapat memilih menu 1-4 saja")