print("MENGHITUNG DISKON")
bayar= int(input("bayar:"))
diskon= int(input("diskon%:"))

potongan_harga=bayar*diskon/100
print("total yang harus di bayar", bayar-potongan_harga,)
print("anda mendapat diskon", diskon, "%")
print("potongan harga yang anda dapat", potongan_harga)

