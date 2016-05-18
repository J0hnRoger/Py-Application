import Tkinter as tk
import HomePage
from ..Models.User import User;
from ..Services.UsersService import UsersService;


LARGE_FONT = ("Verdana", 16)
MEDIUM_FONT = ("Verdana", 12)

class SubscribePage(tk.Frame):
    __user = None
    __usersService = UsersService()
    def __init__(self, parent, controller):
        self.__user = User()
        tk.Frame.__init__(self, parent)
        label = tk.Label(self,  text="Subscribe", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        lbName = tk.Label(self,  text="Nom : ", font=MEDIUM_FONT)
        lbName.pack()
        txtName = tk.Entry(self)
        txtName.pack()
        lbFirstName = tk.Label(self,  text="Prenom : ", font=MEDIUM_FONT)
        lbFirstName.pack()
        txtFirstName = tk.Entry(self)
        txtFirstName.pack()

        lbAge = tk.Label(self,  text="Age : ", font=MEDIUM_FONT)
        lbAge.pack()
        txtAge = tk.Entry(self)
        txtAge.pack()

        btnSaveUser = tk.Button(self, text="Save Me!",
                            command=lambda: self.click_saveUser(txtName.get(), txtFirstName.get(), txtAge.get()))
        btnSaveUser.pack()

        btnBackToHome = tk.Button(self, text="Back To Home",
                            command=lambda: controller.show_frame(HomePage.HomePage))
        btnBackToHome.pack()
    def click_saveUser(self, name, firstName, age):
        self.__user.Name = name
        self.__user.FirstName = firstName
        self.__user.Age = age
        self.__usersService.saveUser(self.__user)
