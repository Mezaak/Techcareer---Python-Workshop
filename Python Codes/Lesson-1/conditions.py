yas = 20

if yas >= 18:
    print("reşitsiniz")
else:
    print("reşit değilsiniz")


not_ = 75

if not_ >= 90:
    print("notunuz: AA")
elif not_ >= 80:
    print("notunuz: BA")
elif not_ >= 70:
    print("notunuz BB")
else:
    print("kaldiniz")


kullanici_adi="admin"
sifre = "1234"
if kullanici_adi =="admin":
    if sifre=="1234":
        print("giris basarili")
    else:
        print("sifre yanlis")
else:
    print("kullanici adi yanlis")


yas = 25
ehliyet_var_mi = True
if yas >= 18 and ehliyet_var_mi:
    print("araba kullanavilirsin")
else:
    print("araba kullanabilirsin")