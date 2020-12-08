n = int(input("masukan tingkatan kotaknya (n): "))
x = 1
while x<=n:
    if x==1 or x==n:
        print(' * ' * n)
    else:
        print(' * ' + ('   '* (n-2)) + ' * ')
    x+=1