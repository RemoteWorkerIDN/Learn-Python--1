"""
perulangan pada python
"""
print('Ibu berkata, "baca semua buku-bukumu')
book_count = 10
jumlah_buku_sudah_dibaca_dan_dipahami = 0
total_jumlah_baca_buku = 0
print('baik ibu')

while total_jumlah_baca_buku < book_count * 2:
    total_jumlah_baca_buku = total_jumlah_baca_buku + 1
    if jumlah_buku_sudah_dibaca_dan_dipahami == 9:
        print(f' buku ke {jumlah_buku_sudah_dibaca_dan_dipahami + 1} belum dipahami')
    else:
        jumlah_buku_sudah_dibaca_dan_dipahami = jumlah_buku_sudah_dibaca_dan_dipahami + 1
        print(f'buku ke {jumlah_buku_sudah_dibaca_dan_dipahami} sudah dibaca')

if jumlah_buku_sudah_dibaca_dan_dipahami < 10:
    print(f' ibu aku baru membaca dan memahami {jumlah_buku_sudah_dibaca_dan_dipahami}')
else:
    print(f'ibu aku sudah membaca dan memahami semua bukuku')
#print(f'jumlah buku yang sudah dibaca dan dipahami {jumlah_buku_sudah_dibaca_dan_dipahami}')
