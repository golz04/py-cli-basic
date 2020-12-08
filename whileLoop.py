level = 1
maxLevel = int(input("Masukkan Jumlah Level : "))

while(maxLevel>=1):
    counter = 1
    lineString = ""
    while(counter<=maxLevel):
        lineString += "="
        counter += 1
    maxLevel -= 1
    bintang = 2*level-1
    simbol = bintang*"*"
    level += 1
    print(lineString, simbol)