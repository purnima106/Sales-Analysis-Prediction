import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

file_path = "C:\\Users\\Purnima\\OneDrive\\Desktop\\ML project 1\\ML Task1\\Stores.csv"
data = pd.read_csv(file_path)
print(data)
print(data.isnull().sum())

features = data[["Store_Area", "Items_Available", "Daily_Customer_Count"]]
target = data["Store_Sales"]


x_train, x_test, y_train, y_test = train_test_split(features, target)

model = LogisticRegression()
model.fit(x_train, y_train)

print(x_test)
print(y_test)
y_pred = model.predict(x_test)
print(y_pred)

input()

cr = classification_report(y_test, y_pred)
print(cr)


Store_Area = float(input("Enter Store Area = "))
Items_Available = float(input("Enter Items available in no. = "))
Daily_Customer_Count = float(input("Enter Daily Customer count = "))
Store_Sales = model.predict([[Store_Area, Items_Available, Daily_Customer_Count ]])
print("Sales Analysis is = ", Store_Sales[0])
