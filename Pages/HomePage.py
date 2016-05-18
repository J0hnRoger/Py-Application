import Tkinter as tk
import SubscribePage
import AllUsersPage

LARGE_FONT = ("Verdana", 12)

def qf(params):
    print params

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self,  text="Hello World", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        userName = "John Doe"
        btnSubscribe = tk.Button(self, text="S'inscrire",
                             command=lambda: controller.show_frame(SubscribePage.SubscribePage))
        btnSubscribe.pack()

        btnAllProfiles = tk.Button(self, text="Voir tous les profils",
                            command=lambda: controller.show_frame(AllUsersPage.AllUsersPage))
        btnAllProfiles.pack()
