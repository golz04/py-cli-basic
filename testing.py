import csv

nim = []
nama = []

def tambah():
  nim_inputan = input("Masukan Nim : ")
  nama_inputan = input("Masukan Nama : ")
  nim.append(nim_inputan)
  nama.append(nama_inputan)


def cari():
  inputan_pencarian = input("Masukan yang ingin dicari")
  if inputan_pencarian in nim:
    indexx = nim.index(inputan_pencarian)
    print(inputan_pencarian,"\t",nama[indexx])
  elif inputan_pencarian in nama:
    indexx = nama.index(inputan_pencarian)
    print(nim[indexx],"\t",inputan_pencarian)
  else:
    print("DATA TIDAK DITEMUKAN")


def delete():
  inputan_delete = input("Masukan Yang mau di delete : ")
  if inputan_delete in nim:
    indexx = nim.index(inputan_delete)
    nim.pop(indexx)
    nama.pop(indexx)
    print("Delete Berhasil")
  elif inputan_delete in nama:
    indexx = nama.index(inputan_delete)
    nim.pop(indexx)
    nama.pop(indexx)
    print("Delete Berhasil")


def save_data():
  with open ("DaftarNama.csv","w") as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=";")

    for i in range(len(nim)):
      csv_writer.writerow([nim[i],nama[i],""])




#Main Program
with open('DaftarNama.csv') as csv_file:
  csv_reader = csv.reader(csv_file,delimiter=';')
  for row in csv_reader:
    nim.append(row[0])
    nama.append(row[1])


print(
"""
1. Tampilkan
2. Tambah
3. Cari
4. Delete
5. Exit
"""
)

while(True):
  pilihan = int(input("Masukan Pilihan Menu : "))
  if (pilihan == 1):
    print("NIM \t Nama")
    for i in range(len(nim)):
      print(nim[i],"\t",nama[i])

  elif (pilihan == 2):
    tambah()
  elif (pilihan == 3):
    cari()
  elif (pilihan == 4):
    delete()
  else:
    save_data()
    break      


# https://docs.google.com/forms/u/0/d/e/1FAIpQLSdab72DbbtRXMJV0oUH_ZoAaQ_OQUPvSomiNb3JrfYJCwKyxA/formResponse