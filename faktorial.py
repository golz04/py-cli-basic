f = int(input("Masukkan faktorialnyaa (n) : "))
hasil = 1
if (f != 0) :
    while f > 1:
        hasil = hasil * f
        f = f - 1
    print("Hasilnya adalah ", hasil)
else :
    print("Hasilnya adalah 1")