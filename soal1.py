try :
    n = int(input("masukkan batas : "))
    x,y=1,2
    hasil = 0
    while x<=n:
        print (x, end=" ")
        hasil = hasil+x
        x,y=y,x+y
    print ("\ntotal",hasil)
except ValueError :
    print("Hanya Boleh Angka")