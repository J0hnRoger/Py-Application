import Tkinter as tk
import HomePage
from ..Services.UsersService import UsersService;

BLUE = "#5588ff"
LARGE_FONT = ("Verdana", 16, "bold")
HEADER_FONT = ("Verdana", 12, "bold")
MEDIUM_FONT = ("Verdana", 10)

class AllUsersPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        usersService=UsersService()
        users=usersService.getAllUsers()

        label = tk.Label(self,  text="Liste de tous les utilisateurs", font=LARGE_FONT).grid(row=0,columnspan=3)

        labelHeaderName = tk.Label(self,text="Nom", font=HEADER_FONT, fg=BLUE).grid(row=1,column=0)
        labelHeaderFirstName = tk.Label(self,text="Prenom", font=HEADER_FONT, fg=BLUE).grid(row=1,column=1)
        labelHeaderName = tk.Label(self,text="Age", font=HEADER_FONT, fg=BLUE).grid(row=1,column=2)

        for idx, user in enumerate(users):
            labelName = tk.Label(self,text=user[1], font=MEDIUM_FONT).grid(row=idx+2,column=0)
            labelFirstName = tk.Label(self,text=str(user[2]), font=MEDIUM_FONT).grid(row=idx+2,column=1)
            labelAge = tk.Label(self,text=str(user[3]), font=MEDIUM_FONT).grid(row=idx+2,column=2)

        btnBackToHome = tk.Button(self, text="Back To Home",command=lambda: controller.show_frame(HomePage.HomePage)).grid(columnspan=4, sticky="S")
