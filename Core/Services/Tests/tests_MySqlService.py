import unittest
from MySqlService import MySqlService

class MySqlServiceTests(unittest.TestCase):
    __db = None
    def setUp(cls):
        cls.__db = MySqlService("localhost", "root", "")

    def test_mustConnectToDb(self):
        self.assertEqual(self.__db.getversion(), True)

    def test_insertUser(self):
        lastRow = self.__db.insert("Utilisateurs", nom="Doe", prenom="John", Age=25)
        self.assertTrue(lastRow != None)

    def test_selectAllUsers(self):
        rows = self.__db.selectAll("Utilisateurs")
        self.assertEqual(rows, 2)

if __name__ == '__main__':
    unittest.main()
