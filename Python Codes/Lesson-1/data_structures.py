meyveler = ["elma","armut","muz"]

print(meyveler[-1])   # son verinin ne olduğunu yazabiliriz indeksine -1 yazarak

meyveler.append("çilek")

meyveler.insert(1,"kiraz")

meyveler.remove("armut")

print(len(meyveler)) #dizinin uzunluğu


meyveler.sort() #listeyi sıralıyor
print(meyveler)

# tuple


koordinat = (10,20)

print(koordinat[0])

koordinat[0] = 50 # bu yapılamaz çünkü sıralı ama değiştirilemez dizilerdir
# aylar sabit ayarlar vs için kullanırız

sayilar = {1,2,3,3,4,4,5,6}
demo = {"ali","veli","ayşe","armut"} # sırasız yapılardır setler meslea bunu print etsen rastgele sırayla göstericel
print(sayilar)

#print(sayilar[0]) hata verir

sayilar.add(6)
sayilar.remove(2)
print(sayilar)


a = {1,2,3}
b = {3,4,5}
print(a - b)   # set için tekrar yapılcak



#dictionary

ogrenci = {
    "ad":"ahmet",
    "yas":38,
    "sehir":"Mersin"
}

print(ogrenci["ad"])

ogrenci["yas"] = 22

ogrenci["okul"] = "ytü"

print(ogrenci.keys()) # key valuleri yazdırdı okul sehir vs gibi

print(ogrenci.values()) # bu da değerleri dönüyor ytü mersin vs gibi




