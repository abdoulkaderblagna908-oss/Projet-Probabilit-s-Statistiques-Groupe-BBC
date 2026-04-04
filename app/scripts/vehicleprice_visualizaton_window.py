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

        # graphes
        canvas = tk.Canvas(self, height=500)

        self.img1 = PhotoImage(Image.open('Images/VehiclePrice_hist.png'))
        self.img2 = PhotoImage(Image.open('Images/VehiclePrice_kdeplot.png'))
        self.img_id = canvas.create_image(0, 0, image=self.img1, anchor="nw")

        def set_img(*args):
            print(selected.get())
            if selected.get() == "hist":
                canvas.itemconfig(self.img_id, image=self.img1)
            else:
                canvas.itemconfig(self.img_id, image=self.img2)


        # choix de graphes
        control_frame = tk.Frame(self, bg="gray100")
        control_frame.pack(fill=tk.Y, side=tk.LEFT)
        tk.Label(control_frame, text="Paramétrage")

        selected = tk.StringVar()
        selected.set("hist")
        tk.Radiobutton(control_frame, text="histograme", value="hist", variable=selected, bg="gray100", command=set_img).pack(anchor="nw")
        tk.Radiobutton(control_frame, text=" courbe de distribution", value="dist", variable=selected, bg="gray100", command=set_img).pack(anchor="nw")

        # Introduction
        tk.Label(self, text="Ici, les données concernant le prix des automiles des assurés",
                 font=("Arial", 16, "bold")).pack()
        control_frame.pack(fill=tk.Y, side=tk.LEFT)
        canvas.pack(anchor="ne", fill=tk.X)

        # Configuration de la fenêtre
        self.title("Description de données")
        self.geometry("800x800")




        #Infos générrales
        data = {
            'Loi de probabilité': 'somme de distributions normales',
            'Moyenne': 28838.715953,
            'Premier quartile': 24500.000000,
            'Deuxième quartile (médiane)': 24500.000000,
            'Troisième quartile': 34500.000000,
            'Minimum': 10000.000000,
            'Maximum': 64500.000000
        }

        info_frame = tk.Frame(self, pady=5)
        info_frame.pack(side=tk.LEFT, anchor="nw")
        for i in data:
            tk.Label(info_frame, text= f"{i :.<60} {data[i]}", font=("Arial", 14, "normal")).pack(anchor="nw")


















if __name__ == "__main__":
    app = VarApp()
    app.mainloop()


