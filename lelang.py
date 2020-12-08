ulang = 1
hargaBarang = int(input("Masukkan Harga Barang : "))
hargaBarangTertinggi = 0
while ulang <= 5 :
    hargaPenawaran = int(input("Masukkan Harga Penawar : "))
    if (hargaBarangTertinggi < hargaPenawaran) :
        hargaBarangTertinggi = hargaPenawaran
    if (hargaPenawaran > hargaBarang) :
        print("Barang terjual dengan harga : ", hargaPenawaran)
        break
    ulang += 1
print("Barang terjual dengan harga : ", hargaBarangTertinggi)