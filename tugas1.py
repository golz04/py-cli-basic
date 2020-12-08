try :
    n = int(input("Masukkan Batasnya (n) :"))
    i = 1
    while (i <= n) :
        print(i)
        i+=1
except ValueError :
    print("Hanya Boleh Angka!")