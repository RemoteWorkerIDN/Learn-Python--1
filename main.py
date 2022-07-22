"""
ini adalah trial python pertama dengan pycharm
"""
# sekuensial
print('Ibu berkata, "pergi ke toko"')
print('Budi menjawab, "baik, apa yang harus dibeli"')
print('Ibu menjawab,"belikan ibu sebotol susu, dan jika ada telor beli 6"')
print('Budi berangkat ke toko')
print('dan mulai berbelanja')
# percabangan
milk_bottle_count = 200
egg_count = 140
print(f'jumlah susu tersedia {milk_bottle_count}')
print(f'jumlah telur tersedia {egg_count}')
if milk_bottle_count > 0:
    print('budi memeriksa uangnya cukup')
    if egg_count == 0:
        print('budi hanya membeli 1 btl susu')
    else:
        print('budi membeli 1 btl susu dan 6 butir telor')
    print('budi membeli 1 botol susu' )
else:
    print('budi tidak membeli susu')
print('budi pulang ke rumah')
print('budi menyerahkan hasil belanja ke ibu')