"""
perulangan pada python
"""
print('Ibu berkata, "baca semua buku-bukumu')
book_count = 1000
jumlah_buku_sudah_dibaca = 0
print('baik ibu')

while jumlah_buku_sudah_dibaca < book_count:
    jumlah_buku_sudah_dibaca = jumlah_buku_sudah_dibaca + 1
    print(f'buku ke {jumlah_buku_sudah_dibaca} sudah dibaca')


print(f'jumlah buku yang sudah dibaca {jumlah_buku_sudah_dibaca}')
