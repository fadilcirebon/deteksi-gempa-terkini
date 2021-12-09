def luas_persegi(sisi):
    luas = sisi * sisi
    return luas

# pemanggilan fungsi
print ("Luas Persegi", luas_persegi(6))

# Membuat fungsi dengan parameter
def luas_segitiga(alas, tinggi):
    luas = (alas * tinggi) / 2
    print ("Luas segitiga: %f" % luas)
    return luas

# Pemanggilan fungsi
luas_segitiga(4, 6)