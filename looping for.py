print('='*50)
print("bayu alfadryan - 191011400835 - UTS KECERDASAN BUATAN")
print('='*50)


Nama = ['bayu alfadryan','ujang','supri','juanmin','suprapman']

alamat = ['benda baru','pamulang','bandung','jogja','riau']





for i,data in enumerate(Nama):
    print(i,':',data)

print('='*50)
for nama,data in zip(Nama,alamat):
    print(nama,'alamat rumahnya di:',data)
