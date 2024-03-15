from tkinter import *
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from time import strftime

root = Tk()
root.title("Sales Analysis Predictor")
root.configure(background="black")
root.geometry("800x450+100+100")
root.resizable(0, 0)
bg = PhotoImage(file="sales.png")
f = ("Cambria", 20)

Lim = Label(root, image=bg)
Lim.place(x=0, y=0)

L1 = Label(root, text="SALES ANALYSIS PREDICTOR", font=f)
L1.grid(row=0, column=0, columnspan=2, pady=20)


def time():
    string = strftime('%I:%M:%S %p')
    Ltm.config(text=string)
    Ltm.after(1000, time)


Ltm = Label(root, font=f, bg="lightblue", fg="black")
Ltm.grid(row=0, column=2, columnspan=2, pady=10)
time()


def find():
    try:
        data = pd.read_csv("C:\\Users\\Purnima\\OneDrive\\Desktop\\ML project 1\\ML Task1\\Stores.csv")
        data['Interaction_Term'] = data['Store_Area'] * data['Daily_Customer_Count']
        features = data[["Store_Area", "Items_Available", "Daily_Customer_Count", "Interaction_Term"]]
        target = data["Store_Sales"]

        scaler = StandardScaler()
        features_scaled = scaler.fit_transform(features)

        x_train, x_test, y_train, y_test = train_test_split(features_scaled, target, test_size=0.2, random_state=42)

        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(x_train, y_train)

        # Get input values from Entry widgets
        Area = float(ent_Area.get())
        Items = float(ent_Items.get())
        Customers = float(ent_Customers.get())
        Interaction_Term = Area * Customers  # Calculate Interaction_Term using input values

        # Predict sales using the model
        Sales = model.predict([[Area, Items, Customers, Interaction_Term]])

        msg = "Store Sales is = " + str(round(Sales[0], 2)) + "₹"
        lab_Sales.configure(text=msg)
    except ValueError:
        msg = "Please enter numeric values only"
        lab_Sales.configure(text=msg)

lab_Area = Label(root, text="Enter Store Area", font=f)
ent_Area = Entry(root, font=f)
lab_Items = Label(root, text="Enter Items in Store", font=f)
ent_Items = Entry(root, font=f)
lab_Customers = Label(root, text="Enter Daily Customer Count", font=f)
ent_Customers = Entry(root, font=f)
btn_predict = Button(root, text="Predict Store Sales", font=f, command=find, relief="raised")
lab_Sales = Label(root, font=f, bg="lightblue", fg="black")

lab_Area.grid(row=1, column=0, pady=20)
ent_Area.grid(row=1, column=1)
lab_Items.grid(row=2, column=0, pady=20)
ent_Items.grid(row=2, column=1)
lab_Customers.grid(row=3, column=0, pady=20)
ent_Customers.grid(row=3, column=1)
btn_predict.grid(row=4, column=0, columnspan=2)
lab_Sales.grid(row=5, column=0, columnspan=2, pady=20)

root.mainloop()
