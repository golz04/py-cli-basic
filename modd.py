from collections import Counter
listArray = []
totalCase = int(input())
for iCount in range (1,(totalCase+1)):
    totalBilangan = int(input())
    angka = [int(angka) for angka in input().split()]
    if len(angka) == totalBilangan:
        listArray.append(angka)
    else:
        break
print(listArray)
countCase = 1
for jCount in range (0,totalCase):
    listModulus = []
    c = Counter(listArray[jCount])
    angkaTerbanyak = max(c.values())
    listModulus = [lCount for lCount, banyak in sorted(c.items()) if banyak==angkaTerbanyak]
    print("Case #{} :".format(countCase),max(listModulus))
    countCase+=1