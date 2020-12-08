jumlahHari = 0
jumlahBulan = 12
bulanAwal = 1

tahun = int(input("Masukkan Tahunnya : "))
while (bulanAwal <= jumlahBulan) :
    if (bulanAwal % 2 == 0) :
        jumlahHari  = jumlahHari + 30
    elif (bulanAwal % 2 == 1) :
        jumlahHari = jumlahHari + 31
    elif (tahun % 4 == 0) : 
        jumlahHari = jumlahHari + 29
    else :
        jumlahHari = jumlahHari + 28
    
    bulanAwal = bulanAwal + 1

print(jumlahHari)