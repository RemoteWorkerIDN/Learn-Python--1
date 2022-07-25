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
python memiliki fungsi untuk menambah dan mengurangi data pada list secara otomatis
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

print('\nClear list')
daftar_buku.clear()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nKembalikan nilai pada list')
daftar_buku =['Lord of the Ring', 'Harry Potter', 'Solo Leveling', 'The god of Demon and Evil']
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nGanti elemen pertama pada list')
daftar_buku[0] = 'Legendary Mechanic'
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPop Satu data')
# Pop adalah perintah untuk mengambil dan menyimpan satu elemen pada sebuah list
buku = daftar_buku.pop(1)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPrint elemen yang diambil')
buku = daftar_buku.pop(2)
print(buku)
# Pop() artinya mengambil elemen terakhir pada satu list, atau bisa juga dituliskan .pop(-1)

print('\nPop baris terakhir')
daftar_buku.pop(-1)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\n,Pop()')
daftar_buku = ['Lord of the Ring', 'Harry Potter', 'Solo Leveling', 'The god of Demon and Evil']
daftar_buku.pop()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

"""
function del bisa digunakan untuk menghapus elemen pada list
"""

print('\nPrint del')
daftar_buku = ['Lord of the Ring', 'Harry Potter', 'Solo Leveling', 'The god of Demon and Evil']
del daftar_buku[0]
# 0 digunakan untu mendelete elemen pertama pada list
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])


