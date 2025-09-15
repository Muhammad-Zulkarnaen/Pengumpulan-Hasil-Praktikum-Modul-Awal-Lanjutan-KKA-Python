def persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    return luas, keliling

luas, keliling = persegi_panjang(20, 5)
print("Luas:", luas)
print("Keliling:", keliling)