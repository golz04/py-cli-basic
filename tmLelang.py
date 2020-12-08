count = 1
hargaMaksimal = int(input("Masukkan Harga Maksimal : Rp."))
tempHargaMaksimal = 0
while count <= 5 :
    hargaPenawaran = int(input("Masukkan Harga Penawar : Rp."))
    if (tempHargaMaksimal < hargaPenawaran) :
        tempHargaMaksimal = hargaPenawaran
    if (hargaPenawaran > hargaMaksimal) :
        break
    count += 1
print("Barang terjual dengan harga : Rp.", tempHargaMaksimal)