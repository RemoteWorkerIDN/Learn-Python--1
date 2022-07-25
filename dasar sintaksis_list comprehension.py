print('\nPerintah del list comprehension')
daftar_buku = ['Lord of the Ring', 'Harry Potter', 'Solo Leveling', 'The god of Demon and Evil']
del daftar_buku[:]
# del daftar_buku[START:STOP]
# comprehension di sebelah kanan titik dua tidak dimulai dari 0 namun mulai dari 1
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del list comprehension [0:0]')
daftar_buku = ['Lord of the Ring', 'Harry Potter', 'Solo Leveling', 'The god of Demon and Evil']
del daftar_buku[0:0]
# harusnya tidak menghapus apa2
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])
# apabila menggunakan [0:-1] maka yang dihapus adalah dari elemen 0 hingga -1 (elemen terakhir dr list),
# di elemen terakhir tidak termasuk dalam elemen yang dihapus
print('\nPerintah del dengan list comprehension [0:-1]')
del daftar_buku[0:-1]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

"""
List comprehension sebenarnya terdiri dari 3 elemen
: yang pertama adalah START
: kedua adalah STOP
" ketiga adalah END (penjedaan) 
contoh:
del XXX[0::1] akan mendelete semua
del XXX[0::2] akan mendelete elemen dengan jeda 1 elemen
"""
print('\nPerintah del dengan list comprehension increment [:::]')
daftar_buku = ['Lord of the Ring', 'Harry Potter', 'Solo Leveling', 'The god of Demon and Evil']
del daftar_buku[0::2]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nList comprehension genap')
daftar_buku = ['Lord of the Ring', 'Harry Potter', 'Solo Leveling', 'The god of Demon and Evil']
del daftar_buku[0::2]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nList comprehension genap')
daftar_buku = ['Lord of the Ring', 'Harry Potter', 'Solo Leveling', 'The god of Demon and Evil']
del daftar_buku[1::2]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

# Untuk melakukan copy list tidak dapat dilakukan dengan perintah list_baru = list_lama
# Namun harus mencantumkan range list (list comprehentionnya)
# CONTOH
print('\nCopy list')
daftar_buku = ['Lord of the Ring', 'Harry Potter', 'Solo Leveling', 'The god of Demon and Evil']
daftar_buku_baru = daftar_buku [:]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nCopy list dengan list comprehension')
daftar_buku = ['Lord of the Ring', 'Harry Potter', 'Solo Leveling', 'The god of Demon and Evil']
daftar_buku_baru = daftar_buku [0::2]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nCopy list dengan list comprehension')
daftar_buku = ['Lord of the Ring', 'Harry Potter', 'Solo Leveling', 'The god of Demon and Evil']
daftar_buku_baru = daftar_buku [1:-1:2]
# Ambil data mulai dari data kedua dengan jeda 1 elemen dan tidak termasuk elemen terakhir
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])