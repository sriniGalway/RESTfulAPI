import sqlite3

class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username): #change self -> cls as we aren't using self in the method
        connection = sqlite3.connect(data.db)
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query, (username,))
        row = result.fetchone()
        if row:
            user = cls(*row) #cls is same as User()
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def find_by_id(cls, id):  # change self -> cls as we aren't using self in the method
        connection = sqlite3.connect(data.db)
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, (id,))
        row = result.fetchone()
        if row:
            user = cls(*row)  # cls is same as User()
        else:
            user = None

        connection.close()
        return user