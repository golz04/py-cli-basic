data = [1,1,1,1,5,9,9,9,9,9]
data.sort()
dataLoop = []
top = 0
bot = len(data)-1
print("Angkanya :",data)
search = int(input("Cari Angka : "))
while(top<=bot):
    mid = (top+bot)//2
    if(data[mid]==search):
        dataLoop.append(mid)
        midNext = mid+1
        midBefore = mid-1
        if(midNext<=bot):
            while(data[midNext] == search):
                if(data[midNext]==search):
                    dataLoop.append(midNext)
                midNext+=1
                break
            if(data[midNext] == search):
                dataLoop.append(midNext)
        if(midBefore>=top):
            while(data[midBefore] == search):
                if(data[midBefore]==search):
                    dataLoop.append(midBefore)
                midBefore-=1
        dataLoop.sort()
        for z in range(len(dataLoop)):
            print("angka {} berada pada index ke-{}".format(search, dataLoop[z]))
        break
    elif(data[mid]<search):
        top = mid+1
    elif(data[mid]>search):
        bot = mid-1
    else:
        print("Angka {} tidak ditemukan.".format(search))