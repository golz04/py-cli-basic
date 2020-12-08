listPassword = ['muhammad', 'haidar', 'muhammadhaidar', 'muhammadhaidar862', 'mHaidar']
password = input("Masukkan Password : ")
for i in range(len(listPassword)):
   if(password == listPassword[i]):
       print("Betul")
       break
else:
    print("Salah")