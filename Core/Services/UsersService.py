from ..Models.User import User;
from MySqlService import MySqlService

class UsersService(object):
    #Constants
    USERS_TABLE_NAME = "Utilisateurs"

    """docstring for UsersService"""
    def __init__(self):
        self.db = MySqlService()

    def saveUser(self, user):
        self.db.insert(self.USERS_TABLE_NAME, nom=user.Name, prenom=user.FirstName, age=user.Age )
        user.toString()
        print "User Saved!"

    def getAllUsers(self):
        return self.db.selectAll(self.USERS_TABLE_NAME)
