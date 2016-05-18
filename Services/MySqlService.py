import MySQLdb

class MySqlService(object):
    """
        Service for interact with MySQL DB
        Usage : from MySqlService import MySqlService
                db = MySqlService("localhost", "root", "")
                db.insert("Utilisateurs", nom="Doe", prenom="John", Age=25)
                db.selectAll("Utilisateurs")
    """
    __connection = None
    __version = None

    def __init__(self, hostname, username, mdp):
        super(MySqlService, self).__init__()
        self.__connection = MySQLdb.connect(host="localhost", user="root", passwd="", db="lmdb")
        cur = self.__connection.cursor()
        self.__version = cur.execute("SELECT VERSION()")

    def getversion(self):
     print "Database version : %s " % self.__version
     return self.__version

    def insert(self, table, *args, **kwargs):
        cur = self.__connection.cursor()
        query = "INSERT INTO %s " % table
        if kwargs:
            keys = kwargs.keys()
            values = tuple(kwargs.values())
            query += "(" + ",".join(["`%s`"] * len(keys)) %  tuple (keys) + ") VALUES (" + ",".join(["%s"]*len(values)) + ")"
        elif args:
            values = args
            query += " VALUES(" + ",".join(["%s"]*len(values)) + ")"

        cur = self.__connection.cursor()
        cur.execute(query, values)
        self.__connection.commit()
        return cur.lastrowid

    def selectAll(self, table):
        return self.select(table, "*")

    def select(self, table, *args ):
        query = 'SELECT'
        keys = args
        l = len(keys) - 1

        if keys[0] == '*':
            query += " * "
        else:
            for i, key in enumerate(keys):
                query += "`"+key+"`"
                if i < l:
                    query += ","
        query += 'FROM %s' % table
        cur = self.__connection.cursor()
        print query
        cur.execute(query)
        number_rows = cur.rowcount
        number_columns = len(cur.description)
        if number_rows >= 1 and number_columns > 1:
            result = [item for item in cur.fetchall()]
        else:
            result = [item[0] for item in cur.fetchall()]

        return result
