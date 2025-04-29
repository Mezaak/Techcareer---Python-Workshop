try:
    sayi = int(input("sayi girin"))
    print(10/sayi)
except ValueError:
    print("lütfen sadece sayı girin")
except ZeroDivisionError:
    print("sıfıra bölme hatası")
except Exception as e:
    print("beklenmeyen bir hata oldu",e)
else:
    print("başarıyla bölündü")
finally:   #bu her zaman çalışır
    print("işlem tammlandı")
# bu yöntemlerle uygulamanın çökmesini engellemiş oluyoruz