import Tkinter as tk
import HomePage

LARGE_FONT = ("Verdana", 12)

class SubscribePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self,  text="Hello Subscribe", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        btnBackToHome = tk.Button(self, text="Back To Home",
                            command=lambda: controller.show_frame(HomePage.HomePage))
        btnBackToHome.pack()
