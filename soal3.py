try :
    x = int(input("Masukkan Angka Pertama :"))
    y = int(input("Masukkan Angka Kedua :"))
    if (x == y) :
        if (x%2 == 0) :
            print("Hasilnya 0")
        elif (x%2 == 1) :
            print("Hasilnya 1")
    elif (x%2==0 and y%2==1) :
        hasil = (x*y)+y
        print("Hasilnya",hasil)
    elif (x%2==1 and y%2==1) :
        hasil = x*y
        print("Hasilnya",hasil)
except ValueError :
    print("Hanya Boleh Angka")