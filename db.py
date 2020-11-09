import sqlite3

class SimpleDb:
    DB_LOCATION = "test.db"

    def __init__(self):
        self._con = sqlite3.connect(self.DB_LOCATION)
        self._cur = self._con.cursor()
        self.create_users_table()

    def __del__(self):
        self._con.close()

    def create_users_table(self):
        self._cur.execute("""
            CREATE TABLE IF NOT EXISTS USERS(
                FIRST_NAME CHAR(20),
                LAST_NAME CHAR(20),
                AGE INT
            )
        """)
        self._con.commit()

    def add_users(self, users):
        self._cur.executemany('INSERT INTO USERS VALUES (?,?,?)', users)
        self._con.commit()

    @property
    def users(self):
        self._cur.execute("SELECT * FROM users")
        return self._cur.fetchall()


if __name__ == "__main__":
    db = SimpleDb()
    test_users = [('Charles', 'Freck', 27), ('Bob', 'Arctor', 31)]
    users = db.users

    if len(users) == 0:
        print("adding test users")
        db.add_users(test_users)
        users = db.users

    for user in users:
        print(user)
