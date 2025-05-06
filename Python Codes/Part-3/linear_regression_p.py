import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import  mean_squared_error,r2_score
import matplotlib.pyplot as plt

print("veri seti oluşturuluyor")

data = {
    "TV":[230,44,17,151,180,8,57,120,100,220],
    "Radio":[37,39,45,41,10,2,20,35,15,23],
    "Newspaper":[69,45,78,20,15,10,25,14,50,20],
    "Sales":[22,10,9,18,19,5,8,15,12,21]
}
df = pd.DataFrame(data)

print("Lineer Regresyon Seti:")
print(df.head())


print("veri eğitim ve test setine ayrılıyor")

x = df[["TV","Radio","Newspaper"]]
y = df[["Sales"]]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

print(f"EĞTİM seti boyutu: {x_train.shape}")
print(f"test seti boyutu : {x_test.shape}")

print("linear regresyon modeli eğitiliyor")

model = LinearRegression()

model.fit(x_train,y_train)

print("linear regresyon modeli eğitildi")
print("katsayılar:")
print(model.coef_)
print(f"intercept : {model.intercept_}")

print("model test verisi ile tahmin yapılıyor")

y_pred = model.predict(x_test)

print("tahmin ve gerçek değerler")

for gerçek, tahmin in zip(y_test,y_pred):
    print(f"gerçek: {gerçek:.2f} -> tahmin : {tahmin:.2f}")

print("model performansı değerlendiriliyor")

mse = mean_squared_error(y_test,y_pred)

r2 = r2_score(y_test,y_pred)

print("model performans sonuçları")
print(f"mse:{mse:.4f}")
print(f"r2 skoru: {r2:.4f}")

print("model tahminleri görselleştiriliyor")

plt.scatter(y_test,y_pred,color='blue')
plt.xlabel("gerçek değerler")
plt.ylabel("tahmin edilen değerler")
plt.title("lineer regresyon")
plt.grid(true)
plt.savefig# eksikler var tamamlarsın