import joblib
import tkinter as tk
from tkinter import ttk
import numpy as np


#chargement du modèle
filename = 'models/logistic_regression_model.joblib'
loaded_model = joblib.load(filename)

#CONSTANTES
MAKE = ('Honda', 'Toyota', 'Ford', 'Mazda', 'Chevrolet', 'Pontiac',
       'Accura', 'Dodge', 'Mercury', 'Jaguar', 'Nisson', 'VW', 'Saab',
       'Saturn', 'Porche', 'BMW', 'Mecedes', 'Ferrari', 'Lexus')

FONT = ("Times New Roman", 15, "normal")

PADY = 30
MEANS = np.array([np.float64(0.0),
 np.float64(-6.090366306515145e-17),
 np.float64(1.218073261303029e-16),
 np.float64(6.090366306515145e-17),
 np.float64(-4.0602442043434296e-17),
 np.float64(-1.0150610510858574e-17),
 np.float64(-3.0451831532575724e-17)])

STDS = np.array([1.0,
 1.0,
 0.9999999999999989,
 0.9999999999999997,
 1.0000000000000002,
 0.9999999999999998,
 1.0])

def normalize(x, mean, std):
    return (x - mean) / std




class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x700")
        tk.Label(self, text="Remplissez les champs ci-dessous pour prévoir si votre client fraude ou pas!", font=("Arial", 16, "bold")).grid(row=0, column=1)

        #Variables
        sex = tk.StringVar()
        sex.set("masculin")
        accident_area = tk.StringVar()
        accident_area.set("urbain")
        make = tk.StringVar()
        make.set("Honda")
        maritalStatus = tk.StringVar()
        maritalStatus.set("marié")
        fault = tk.StringVar()
        fault.set("oui")
        deductible = tk.DoubleVar()
        deductible.set(2000.0)
        pastNumberOfClaims = tk.StringVar()
        pastNumberOfClaims.set("jamais")







        frame = tk.Frame(self)
        frame.grid(row=1, column=1)

        tk.Label(frame, text = "Quel est le sexe de l'assuré?", font=FONT).grid(column=1, row=0, pady=PADY)
        combo1 = ttk.Combobox(frame, textvariable=sex, font=FONT)
        combo1['values'] = ("masculin", "féminin")
        combo1["state"] = "readonly"
        combo1.grid(column=2, row=0)



        tk.Label(frame, text="Quelle est la marque de la voiture?", font=FONT).grid(column=1, row=1, pady=PADY)
        combo2 = ttk.Combobox(frame, textvariable=make, font=FONT)
        combo2['values'] = MAKE
        combo2["state"] = "readonly"
        combo2.grid(column=2, row=1)

        tk.Label(frame, text="Dans quelle zone a lieu l'accident?", font=FONT).grid(column=1, row=2, pady=PADY)
        combo3 = ttk.Combobox(frame, textvariable=accident_area, font=FONT)
        combo3['values'] = ('urbain', 'rurale')
        combo3["state"] = "readonly"
        combo3.grid(column=2, row=2)

        tk.Label(frame, text="Quelle est sa situation matrimoniale?", font=FONT).grid(column=1, row=3, pady=PADY)
        combo4 = ttk.Combobox(frame, textvariable=maritalStatus, font=FONT)
        combo4['values'] = ('marié', 'célibataire')
        combo4["state"] = "readonly"
        combo4.grid(column=2, row=3)

        tk.Label(frame, text="A-t-il eu raison de l'accident?", font=FONT).grid(column=1, row=4, pady=PADY)
        combo5 = ttk.Combobox(frame, textvariable=fault, font=FONT)
        combo5['values'] = ('oui', 'non')
        combo5["state"] = "readonly"
        combo5.grid(column=2, row=4)

        tk.Label(frame, text="Combien a-t-il payé lui même pour se dédomager?", font=FONT).grid(column=1, row=5, pady=PADY)
        combo6 = tk.Entry(frame, textvariable=deductible, font=FONT)
        combo6.grid(column=2, row=5)

        tk.Label(frame, text="Combien de fois votre assuré a-t-il réclamé de l'assurance?", font=FONT).grid(column=1, row=6, pady=PADY)
        combo7 = ttk.Combobox(frame, textvariable=pastNumberOfClaims, font=FONT)
        combo7['values'] = ('jamais', 'une fois', 'deux à quatre fois', 'plus de quatre fois')
        combo7["state"] = "readonly"
        combo7.grid(column=2, row=6)

        def predire():

            varaibles = [make, accident_area, sex, maritalStatus, fault, deductible, pastNumberOfClaims]


            code = {
                "masculin":1,
                "féminin":0,
                "oui":1,
                "non":0,
                "urbain":1,
                "rurale":0,
                'jamais':0,
                'une fois':1,
                'deux à quatre fois':3,
                'plus de quatre fois':5,
                'marié':1,
                'célibataire':0
            }
            [code.update({MAKE[i]:i}) for i in range(len(MAKE))]

            test_set = []
            for i in range(7):
                if i != 5:
                    test_set.append(code[varaibles[i].get()])
                else:
                    test_set.append(varaibles[i].get())

            test_set = np.array(test_set)
            test_set = normalize(test_set, MEANS, STDS)
            test_set = test_set.reshape((1,7))

            result = loaded_model.predict(test_set)
            if result == 0:
                return "Pas de fraude"
            return "Cas de fraude!"




        frame1 = tk.Frame(self)
        frame1.grid(row=1, column=2)
        tk.Label(frame1, text="Résultat", font=FONT).pack()
        result = tk.Label(frame1, font=FONT)
        result.pack()

        def validate():
            result["text"] = (predire())

        tk.Button(frame, text="Valider", bg="green", command=validate, font=FONT).grid(row=7, column=1)


if __name__ == "__main__":
    App()
    tk.mainloop()

