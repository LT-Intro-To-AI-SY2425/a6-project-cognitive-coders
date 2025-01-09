import pandas as pd
import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

#Greater thn 50k = 1
#Less than 50k = 0
data = pd.read_csv("data.csv")
#print(data.columns.tolist()) 
#print(data)
data["income"].replace(["<=50K", ">50K"], [0,1], inplace=True)
#print(data)
x = data[["Age","fnlwgt","education-num","capital-gain","capital-loss","hours-per-week"]].values
y = data[["income"]]
print(y.iloc[1])

scaler = StandardScaler().fit(x)
x = scaler.transform(x)

x_train, x_test, y_train, y_test = train_test_split(x, y)

model = linear_model.LogisticRegression().fit(x_train, y_train)

correct = 0
incorrect = 0
for index in range(len(x_test)):
    x = x_test[index]
    
    x = x.reshape(-1, 6)
    y_pred = int(model.predict(x))
    
    """
    print("//////////////////////////////////////////////")
    
    print(type(int(y_test.iloc[index])))
    print("//////////////////////////////////////////////")
    """

    if y_pred == int(y_test.iloc[index]):
        correct+=1
    else:
        incorrect+=1


    if y_pred == 0:
        y_pred = "<=50K"
    elif y_pred == 1:
        y_pred = ">50K"
  
    
    actual = int(y_test.iloc[index])
    
    if actual == 0:
        actual = "<=50K"
    elif actual == 1:
        actual = ">50K"
  
    print("Predicted income: " + y_pred + " Actual income: " + actual)
    print("")
    
    print("Correct:", correct)
    print("Incorrect:", incorrect)