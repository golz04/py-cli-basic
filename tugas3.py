try :
    n=int(input("masukan tingkatan segitiga (n) :"))
    t=1
    while t<=n:
        print('* '*t)
        t+=1
except ValueError :
    print("Hanya Boleh Angka!")