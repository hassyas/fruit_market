# init harga dan stock
priceApel = 10000
priceJeruk = 15000
priceAnggur = 20000

stockApel = 10
stockJeruk = 15
stockAnggur = 8

#Deklarasi fungsi hitung buah
def input_fruit(name, stock, price)
    while True:
        n = int(input(f' Input jumlah {name.capitalize()}:'))
        if n <= stock:
            price = n*price
            break
        else print(f"Jumlah terlalu banyak. {name.capitalize()} sisa{stock}")

# init jumlah buah
while True:
    nApel = int(input("Input jumlah apel: "))
    if nApel <= stockApel:
        break
    else:
        print(f'Jumlah terlalu banyak. Apel sisa {stockApel}')

while True:
    nJeruk = int(input("Input jumlah jeruk: "))
    if nJeruk <= stockJeruk:
        break
    else:
        print(f'Jumlah terlalu banyak. Jeruk sisa {stockJeruk}')

while True:
    nAnggur = int(input("Input jumlah anggur: "))
    if nAnggur <= stockAnggur:
        break
    else:
        print(f'Jumlah terlalu banyak. Anggur sisa {stockAnggur}')

# hitung harga per buah
totalPriceApel = nApel * priceApel
totalPriceJeruk = nJeruk * priceJeruk
totalPriceAnggur = nAnggur * priceAnggur

# hitung harga total buah
priceTotal = totalPriceAnggur + totalPriceApel + totalPriceJeruk

# show detail belanjaan
print(
    f'''
Detail Belanja 

Apel     :  {nApel} x {priceApel}
Jeruk    :  {nJeruk} x {priceJeruk}
Anggur   :  {nAnggur} x {priceAnggur}
Total    :  {priceTotal}
'''
)

# proses pembayaran
while True:
    pay = int(input('Masukkan jumlah uang: '))
    delta = pay - priceTotal
    if delta >= 0:
        print(f'Terima kasih. Uang kembalian {delta}')
        break
    else:
        print(f'Uang anda kurang sebesar {abs(delta)}')