from ..Models.User import User;
from MySqlService import MySqlService

class UsersService(object):
    #Constants
    USERS_TABLE_NAME = "Utilisateurs"

    """docstring for UsersService"""
    def __init__(self):
        self.db = MySqlService()

    def saveUser(self, user):
        print "TODO - Boss un peu :D - User Saved!"

    def getAllUsers(self):
        print " TODO - Boss un peu :D - Return All Users"
