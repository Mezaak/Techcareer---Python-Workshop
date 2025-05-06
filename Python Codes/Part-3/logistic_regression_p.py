import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier

print("logistic regresyon için veri seti oluşturuluyor")

data_classification = {
    "Age":[22,25,47,52,46,56,55,60,62,61],
    "Income":[25000,32000,47000,52000,46000,58000,60000,62000,64000,63000],
    "Purchased":[0,0,1,1,1,1,1,1,1,1]
}
df_classification = pd.Dataframe(data_classification)
print("lojistik regresyon veri seti")
print(df_classification.head())

print("lojistik regresyon için veri eğitim ve test setine ayrılıyor")

x_cls = df_classification[["Age","Income"]] # bağımsız değişkenleri yaz
y_cls = df_classification["Purchased"]

x_train,x_test,y_train,y_test = train_test_split(x_cls,y_cls,test_size=0.2,random_state=42)

print(f"eğitim set iboyutu: {x_train.shape}")
print(f"test seti boyutu : {x_test.shape}")

model_logistic = LogisticRegression()

model_logistic.fit(x_train,y_train)
print("logistic regresyon modeli eğitildi")
print("katsayılar:")
print(model_logistic.coef_)
print(f"ıntercept : {model_logistic.intercept_}")

print("loistik regresyon modeli test verisi ile tahmin yapıyor")

y_pred_logistic = model_logistic.predict(x_test)

print("gerçek ve tahmin edilen değerler:")
for gerçek,tahmin in zip(y_test,y_pred_logistic):
    print(f"gerçek: {gerçek} -> tahmin {tahmin}")

print("lojistik regresyon modeli performansı ölçülüyor")

accuracy_logistic = accuracy_score(y_test,y_pred_logistic)
print(f"doğruluk skoru: {accuracy_logistic:.4f}")

print("knn modeli eğitiliyor")

model_knn = KNeighnorsClassifier(n_neighbors=3)

model_knn.fit(x_train,y_train)

print("knn modeli test verisi ile tahmin yapıyor")

y_pred_knn = model_knn.predict(x_test)

for gerçek,tahmin in zip(y_test,y_pred_knn):
    print(f"gerçek: {gerçek} - > tahmin{tahmin}")

print("knn modeli performansı ölçülüyor")

accuracy_knn = accuracy_score(y_test,y_pred_knn)

print(f"doğruluk skoru: {accuracy_knn:.4f}")