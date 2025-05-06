import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = pd.read_csv("Mall_Customers.csv")

x = data[['Annual Income (k$)','Spending Score (1-100)']]

print(x.head())

wcss = []

for k in range(1,11):
    kmeans = KMeans(n_clusters=k,init='k-means++',random_state=42)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)
plt.plot(range(1,11),wcss,marker='o')
plt.title("Elbow yöntemi")
plt.xlabel("kume sayisi")
plt.ylabel("wcss")
plt.grid(True)
