meyveler = ["elma","armut","muz"]

for meyve in meyveler:
    print(meyve)

for i in range(5):  # sıfırdan başlar 5 dahil değil
    print(i)


for i in range(1,10,2):
    print(i)

sayi = 1
while sayi <= 5:
    print(sayi)
    sayi += 1

while True:
    komut = input("çıkmak için q tuşuna basın")

    if komut =="q":
        print("programdan çıkıldı")
        break
    else:
        print("devam ediliyor")

for i in range(10):
    if i == 5:
        break
    print(i)


for i in range(5):
    if i == 2:
        continue  # 2 yi atlıyo
    print(i)


for i in range(3):
    pass        # şu an yapıcak bir şey yok kısmında pass kullanırız



