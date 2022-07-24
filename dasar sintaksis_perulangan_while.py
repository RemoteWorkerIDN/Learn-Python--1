"""
perulangan pada python
"""
print('Ibu berkata, "baca semua buku-bukumu')
book_count = 10
understood_count = 0
read_count = 0
print('baik ibu')

while read_count < book_count * 2:
    read_count = read_count + 1
    if understood_count == 9:
        print(f' buku ke {understood_count + 1} belum dipahami')
    else:
        understood_count = understood_count + 1
        print(f'buku ke {understood_count} sudah dibaca')

if understood_count < 10:
    print(f' ibu aku baru membaca dan memahami {understood_count}')
else:
    print(f'ibu aku sudah membaca dan memahami semua bukuku')
#print(f'jumlah buku yang sudah dibaca dan dipahami {jumlah_buku_sudah_dibaca_dan_dipahami}')
