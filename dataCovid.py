listPendatang = [["Muhammad Haidar", "Bondowoso", "30 Desember 2000", "159753486426", "Malang", "L", "Jl.Raya Maesan No.55"], ["Haidar", "Jember", "12 Februari 2000", "154785236584", "Malang", "L", "Jl.Ahmad Yani No.13"],["Stefanie", "Banyuwangi", "15 Juni 2001", "458956258751", "Kediri", "P", "Jl.Santawi No.70"],["Agahata", "Banyuwangi", "15 November 2001", "273645173652", "Solo", "P", "Jl.Diponegoro No.70"]]
listCountFind = 0
coreLoop = True

while coreLoop==True:
    print("======Data Pendatang Luar Kota Covid-19======")
    print("==============Wilayah Bondowoso==============")
    print("1. Tambah Data Pendatang")
    print("2. Lihat Semua Data Pendatang")
    print("3. Cari Pendatang")
    print("4. Urutkan Pendatang")
    print("5. Keluar")
    print("---------------------------------------------")

    menu = int(input("Silahkan Pilih Menu(1-5) :"))
    if(menu == 1):
        loopOne = True
        while loopOne==True:
            nama = input("Masukkan Nama :")
            tempatLahir = input("Masukkan Tempat Lahir :")
            tanggalLahir = input("Masukkan Tanggal Lahir (ex: 1 Januari 1945) :")
            noIdentitas = input("Masukkan No (KTP/SIM/Identitas Lainnya) :")
            asalKota = input("Masukkan Kota Asal :")
            jenisKelamin = input("Masukkan Jenis Kelamin (L/P) :")
            alamatTujuan = input("Masukkan Alamat Tujuan :" )
            if(nama != "" and tempatLahir != "" and tanggalLahir != "" and noIdentitas != "" and asalKota != "" and jenisKelamin != "" and alamatTujuan != ""):
                listPendatang.append([nama, tempatLahir, tanggalLahir, noIdentitas, asalKota, jenisKelamin, alamatTujuan])
                print("Berhasil Menambahkan Data Pendatang.")
                loopOne = False
            else:
                print("Gagal menambahkan Data Pendatang, Semua Data Wajib Diisi!")
    elif(menu == 2):
        print("======Data Semua Pendatang Covid-19======")
        for i in range(len(listPendatang)):
            print("Nama             :", listPendatang[i][0])
            print("Tempat Lahir     :", listPendatang[i][1])
            print("Tanggal Lahir    :", listPendatang[i][2])
            print("No Identitas     :", listPendatang[i][3])
            print("Asal Kota        :", listPendatang[i][4])
            if(listPendatang[i][5] == "L" or listPendatang[i][5] == "l"):
                print("Jenis Kelamin    : Laki-Laki")
            elif(listPendatang[i][5] == "P" or listPendatang[i][5] == "p"):
                print("Jenis Kelamin    : Perempuan")
            print("Alamat Tujuan    :", listPendatang[i][6])
            print("---------------------------------------")
    elif(menu == 3):
        keyword = input("Masukkan (Nama/No Identitas/Asal Kota) Pendatang Yang Ingin Dicari :")
        for i in range(len(listPendatang)):
            for j in range(len(listPendatang[i])):
                if keyword in listPendatang[i][j] :
                    listCountFind+=1
                    print("Nama             :", listPendatang[i][0])
                    print("Tempat Lahir     :", listPendatang[i][1])
                    print("Tanggal Lahir    :", listPendatang[i][2])
                    print("No Identitas     :", listPendatang[i][3])
                    print("Asal Kota        :", listPendatang[i][4])
                    if(listPendatang[i][5] == "L" or listPendatang[i][5] == "l"):
                        print("Jenis Kelamin    : Laki-Laki")
                    elif(listPendatang[i][5] == "P" or listPendatang[i][5] == "p"):
                        print("Jenis Kelamin    : Perempuan")
                    print("Alamat Tujuan    :", listPendatang[i][6])
                    print("---------------------------------------")
        print("o> Ditemukan Data Dengan Kata Kunci '"+keyword+"' Sebanyak :",listCountFind)
        listCountFind = 0
    elif(menu == 4):
        print("1. Urutkan Berdasarkan Nama (A-Z)")
        print("2. Urutkan Berdasarkan Nama (Z-A)")
        print("---------------------------------")
        menuFour = int(input("Pilih Menu :"))
        if(menuFour == 1):
            listTempSorting = listPendatang
            for i in range(len(listTempSorting)):
                for j in range(len(listTempSorting)-1):
                    if(listTempSorting[j][0]>listTempSorting[j+1][0]):
                        listTempSorting[j],listTempSorting[j+1] = listTempSorting[j+1],listTempSorting[j]
            print("======Data Semua Pendatang Covid-19======")
            print("===========Sorting Nama [A-Z]============")
            for i in range(len(listTempSorting)):
                print("Nama             :", listTempSorting[i][0])
                print("Tempat Lahir     :", listTempSorting[i][1])
                print("Tanggal Lahir    :", listTempSorting[i][2])
                print("No Identitas     :", listTempSorting[i][3])
                print("Asal Kota        :", listTempSorting[i][4])
                if(listTempSorting[i][5] == "L" or listTempSorting[i][5] == "l"):
                    print("Jenis Kelamin    : Laki-Laki")
                elif(listTempSorting[i][5] == "P" or listTempSorting[i][5] == "p"):
                    print("Jenis Kelamin    : Perempuan")
                print("Alamat Tujuan    :", listTempSorting[i][6])
                print("---------------------------------------")
        elif(menuFour == 2):
            listTempSorting = listPendatang
            for i in range(len(listTempSorting)):
                for j in range(len(listTempSorting)-1):
                    if(listTempSorting[j][0]<listTempSorting[j+1][0]):
                        listTempSorting[j],listTempSorting[j+1] = listTempSorting[j+1],listTempSorting[j]
            print("======Data Semua Pendatang Covid-19======")
            print("===========Sorting Nama [Z-A]============")
            for i in range(len(listTempSorting)):
                print("Nama             :", listTempSorting[i][0])
                print("Tempat Lahir     :", listTempSorting[i][1])
                print("Tanggal Lahir    :", listTempSorting[i][2])
                print("No Identitas     :", listTempSorting[i][3])
                print("Asal Kota        :", listTempSorting[i][4])
                if(listTempSorting[i][5] == "L" or listTempSorting[i][5] == "l"):
                    print("Jenis Kelamin    : Laki-Laki")
                elif(listTempSorting[i][5] == "P" or listTempSorting[i][5] == "p"):
                    print("Jenis Kelamin    : Perempuan")
                print("Alamat Tujuan    :", listTempSorting[i][6])
                print("---------------------------------------")
    elif(menu == 5):
        print("Terima Kasih Telah Menggunakan Program Sederhana Ini :)")
        coreLoop = False
    else:
        print("Hanya Boleh Memilih Angka 1-5 Saja!")