import tkinter as tk
from tkinter import ttk

import pandas as pd
from PIL import Image, ImageTk
from tkinter.messagebox import showinfo

from PIL.ImageTk import PhotoImage


class VarApp(tk.Toplevel):
    def __init__(self):
        super().__init__()

        #méta paramètes


        # Configuration de la fenêtre
        self.title("Description de données")
        self.geometry("800x800")


        #Introduction
        tk.Label(self, text="Ici, les données concernant la fraude chez les assurés", font=("Arial", 16, "bold")).pack()

        #graphes
        canvas = tk.Canvas(self, height=500,)
        canvas.pack(anchor="ne", fill=tk.X)
        self.img = PhotoImage(Image.open('Images/FraudFound.png'))
        canvas.create_image(0, 0, image=self.img, anchor="nw")

        #Infos générrales
        data = {
            'Loi de probabilité': 'Bernouilli (p = 6%)',
            'Moyenne': 0.06,
            'Ecart-type': 0.237,
            'Nombre de cas de fraude': 923,
            'Nombre de cas sans fraude': 14497
        }

        info_frame = tk.Frame(self, pady=5)
        info_frame.pack(side=tk.LEFT, anchor="nw")
        for i in data:
            tk.Label(info_frame, text= f"{i :-<60} {data[i]}", justify="left", font=("Arial", 16, "normal")).pack(anchor="nw")













if __name__ == "__main__":
    app = VarApp()
    app.mainloop()


