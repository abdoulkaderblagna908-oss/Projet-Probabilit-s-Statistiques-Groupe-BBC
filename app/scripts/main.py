import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter.messagebox import showinfo
import fraudfound_visualization_window as fvw
import vehicleprice_visualizaton_window as vvw
import pastnumberofclaims_window as pvw
import fault_window as flvw
import prediction


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        #Meta-paramètres


        #Configuration de la fenêtre
        self.title("Assurance Automobile")
        self.geometry("800x800")



        #Image de fond
        self.background_image = Image.open("Images/background_img.png")

        canvas = tk.Canvas(self)
        canvas.pack(fill="both", expand=True)

        def resize_image(event):
            # Redimensionner l'image à la taille de la fenêtre
            resized = self.background_image.resize((event.width, event.height))
            bg = ImageTk.PhotoImage(resized)
            canvas.bg = bg  # éviter suppression par Python
            canvas.create_image(0, 0, image=bg, anchor="nw")

        # Lier le redimensionnement
        canvas.bind("<Configure>", resize_image)

        # Aller à une variable
        def goto_fraud():
            fvw.VarApp()

        def goto_price():
            vvw.VarApp()

        def goto_claims():
            pvw.VarApp()

        def goto_fault():
            flvw.VarApp()

        def goto_predict():
            prediction.App()

        # Configuration du menu
        menu_bar = tk.Menu(self)
        self.config(menu=menu_bar)

        variables_menu = tk.Menu(menu_bar, tearoff=False)
        variables_menu.add_command(label="Fraude", underline=0, command=goto_fraud)
        variables_menu.add_command(label="VehiclePrice", command=goto_price)
        variables_menu.add_command(label="PastNumberOfClaims", command=goto_claims)
        variables_menu.add_command(label="Fault", command=goto_fault)
        variables_menu.add_separator()
        menu_bar.add_cascade(label="Variables", menu=variables_menu)

        predict_menu = tk.Menu(menu_bar, tearoff=False)
        predict_menu.add_command(label="Régression Logistique", command=goto_predict)
        menu_bar.add_cascade(menu=predict_menu, label="Prédire")





if __name__ == "__main__":
    App()
    tk.mainloop()
