# open("demo.txt","x")

# with open("demo.txt","w") as dosya:
#     dosya.write("merhaba dünya")
#     dosya.write("bugün hava güzel")
#  w içinde yazzıolsa bile silip üstüne yazar


# with open("demo","a") as dosya:
#     dosya.write("Selam\n")
#     dosya.write("iyiyim\n")


with open("demo","a") as dosya:
    veri = dosya.read()
    dosya.write("iyiyim\n")
    print(veri)


# with open("demo","a") as dosya:
#     veri = dosya.readline()
#     dosya.write("iyiyim\n")
#     print(veri)



# not_ = input("notunuzu girin")
# with open("notlar.txt","a") as dosya:
#     dosya.write(not_ + "\n")
# print("not kaydedildi")


# try:
#     with open("olmayan_dosya.txt","r") as dosya:
#         print(dosya.read())
# except FileNotFoundError:
#     print("dosya bulunamadı")


