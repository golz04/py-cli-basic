try :
    x = int(input("Masukkan angka : (1-20)"))
    xTemp = 0
    count = 1
    if (x == 1) :
        print("The World")
    elif (x == 2) :
        print("Hello World")
    elif (x<1 or x>20) :
        print("Invalid")
    else :
        while (count <= x) :
            xTemp+=1
            if (xTemp >= 0 and xTemp <= 5) :
                if (count%2 == 1) :
                    print("=", end='')
                else :
                    print("|", end='')
            if (xTemp >= 6 and xTemp <= 10) :
                if (count%2 == 1) :
                    print("=", end='')
                else :
                    print("*", end='')    
            if (xTemp >=11 and xTemp <=20) :
                if (count%2 == 1) :
                    print("^", end='')
                else :
                    print("=", end='')
            count+=1
except ValueError :
    print("Hanya Boleh Angka")