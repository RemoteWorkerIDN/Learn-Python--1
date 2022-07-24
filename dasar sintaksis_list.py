"""
list dasar python
"""

daftar_buku = ['Lord of the Ring', 'Harry Potter', 'Solo Leveling']
# print(daftar_buku)
print('daftar seluruh buku')
for buku in daftar_buku:
    print(buku)

"""
list dapat berupa data string maupun int (integral)
data pada list bersifat dinamis
artinya kita dapat merubah data pada list secara keseluruhan 
hanya dengan membuat definisi baru atas list tersebut
"""

print('\njudul buku pada index tertentu')
print(daftar_buku[2])

print('\nprint dengan for in range')
# digunakan untuk print list yang panjangnya dinamik
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

# nama variabel.append() akan menambahkan data yang ada list tersebut
print('\nMenambahkan data ke dalam list')
daftar_buku.append('The god of demon and evil')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])
