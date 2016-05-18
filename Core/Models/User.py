class User(object):
    """docstring for User"""
    def __init__(self):
        self._name = None
        self._firstName = None
        self._age = None

    #Methods
    def toString(self):
        print "User : {0} - {1} - {2} ans.".format(self.Name, self.FirstName, self.Age)

    #Properties
    @property
    def Name(self):
        return self._name

    @Name.setter
    def Name(self, value):
        self._name = value

    @property
    def FirstName(self):
        return self._firstName

    @FirstName.setter
    def FirstName(self, value):
        self._firstName = value

    @property
    def Age(self):
        return self._age

    @Age.setter
    def Age(self, value):
        self._age = value
