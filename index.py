import Tkinter as tk
from ttk import *

from Core.Pages.HomePage import HomePage
from Core.Pages.SubscribePage import SubscribePage
from Core.Pages.AllUsersPage import AllUsersPage

class LoveMachineApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (HomePage, SubscribePage, AllUsersPage) :
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()

if __name__ == "__main__":
    app = LoveMachineApp()
    app.mainloop()
