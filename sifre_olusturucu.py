import random

karakter = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
şifre_uzunlugu = int (input("sifre uzunluğunu girin:"))
sifre = ""

for i in range(sifre_uzunlugu):
    sifre += random.choice(karakter)

print(sifre)    
