import numpy as np

# print("numpy versiyonu",np.__version__)


liste = [1,2,3,4,5]
numpy_dizi = np.array(liste)
print("türü:",type(numpy_dizi))

numpy_dizi2 = np.array([10,20,30,40,50])

print("numpy dizi:",numpy_dizi)

dizi_aralik = np.arange(0,10,2)
print("aralikli numpy dizisi",dizi_aralik)

dizi_sifirlar = np.zeros(5)
print("sifir numpy dizisi",dizi_sifirlar)

dizi_birler = np.ones(5)
print("birler dizisi",dizi_birler)

dizi_linspace = np.linspace(0,20,5)
print("eşit parça dizi",dizi_linspace)

dizi_random = np.random.rand(5)# 5 elemanlı rastgele sayı üretiyo 0 la 1 arasında
print("rastgele dizi",dizi_random)

dizi = np.array([10,20,30,40,50])

print("dizi",dizi)
print("toplam",np.sum(dizi))
print("ortalama",np.mean(dizi))
print("maksimum değer",np.max(dizi))
print("minimum değer",np.min(dizi))
print("standart sapma",np.std(dizi))# standart sapma ortalamaya olan uzaklık
print("varyans",np.var(dizi))# bir veri kümesindeki değerlerin ....

matris =  np.random.randint(1,10,(2,3))
print("matris:\n",matris)

transpoz = matris.T
print("transpoz:\n",transpoz) #matrisin satırlarını sütuna sütunlarını satırlara çevirdik

A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
carpim = np.dot(A,B)
print("matris carpimi:\n",carpim) # satırlarla sütunları çarpıyoruz( buraya biraz bak)