try :
    n = int(input("Masukkan Batasnya (n >= 33) :"))
    i = 33
    if (n >= i) :
        while (i <= n) :
            print(i)
            i+=3
    else :
        print("Minimal inputan 33!")
except ValueError :
    print("Hanya Boleh Angka!")