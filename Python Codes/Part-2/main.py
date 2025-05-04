from preprocessing import handle_missing_values,encode_categorial_data,scale_data,split_data
import pandas as pd
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression

if __name__ == "__main__":
     data = pd.DataFrame({
    "Yaş":[25,45,30,35,40],
    "Cinsiyet":["Kadın","Erkek","Erkek","Kadın",None],
    "Maaş":[3000,7000,None,5000,6000],
    "Deneyim":[2,20,5,10,15],
    "Departman":["IT","Yönetim","Muhasebe","IT","Yönetim"],
    "Terfi":[0,1,0,1,1]
    })
     
     data = handle_missing_values(data)

     data = encode_categorial_data(data)

     scaler = StandardScaler()
     data[["Yaş","Maaş","Deneyim"]] = scaler.fit_transform(data[["Yaş","Maaş","Deneyim"]])

     x = data.drop(["Terfi"],axis=1)
     y = data["Terfi"]
     x_train,x_test,y_train,y_test = split_data(data)

    model = LogisticRegression()
    model.fit(x_train,y_train)


