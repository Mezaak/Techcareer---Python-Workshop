def selamla():
    print("merhaba dünya")

selamla()

def selamla(isim):
    print(f"merhaba {isim}")

selamla("ahmet")


def topla(x,y):
    return x + y

sonuc = topla(5,6)

print(sonuc)



def topla(*sayilar):
    toplam = 0
    for sayi in sayilar:
        toplam += sayi
    return toplam

print(topla(1,2,3,4,5))

def bilgiler(**kisi):
    for anahtar, deger in kisi.items():
        print(f"{anahtar}: {deger}")
bilgiler(ad="ahmet",yas=38,sehir="mersin")   # buraya bak not
# key value


kare = lambda x:x*x   #bu da anlaşılmadı

print(kare(5))



def kullanici_topla():
    a = int(input("birinci sayiyi girin"))
    b = int(input("ikinc isayiyi giri"))
    print("toplam",a + b)
kullanici_topla()