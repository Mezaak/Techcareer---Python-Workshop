import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)

notlar = np.random.randint(0,101,1000)

print("öğrenci notları (ilk 10):",notlar[:10])

print("ortalama:",np.mean(notlar))
print("en yüksek not:",np.max(notlar))
print("en düşük not",np.min(notlar))
print("standart sapma",np.std(notlar))


gecenler = notlar[notlar >= 50]
kalanlar = notlar[notlar < 50]
print("geçen öğrnci sayısı",len(gecenler))
print("kalan öğrnci sayısı",len(kalanlar))

plt.figure(figsize=(10,5))
plt.hist(notlar,bins=10,edgecolor='black',alpha=0.7)
plt.xlabel("not aralıkları")
plt.ylabel("ogrenci sayisi")
plt.title("ogrencii not dagilimi")
plt.grid(True)
plt.show()

sirali_notlar = np.sort(notlar)

dusuk_dilim = sirali_notlar[:100]
yuksek_dilim = sirali_notlar[-100:]

print("en düşük %10 ortalaması",np.mean(dusuk_dilim))
print("en yüksek %10 dilim ortalaması",np.mean(yuksek_dilim))