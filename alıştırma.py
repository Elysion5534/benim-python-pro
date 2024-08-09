import random



karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

parolaUzunlugu = int(input("parolanın uzunluğu ne kadar olsun= "))

parola = ""
for i in range(parolaUzunlugu):
    parola=parola+random.choice(karakterler)



print("parolanız: ", parola)
