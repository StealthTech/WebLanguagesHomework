import MySQLdb as mysql
import warnings

warnings.filterwarnings('ignore')


class Connection:
    def __init__(self, hostname, user, password, database):
        self.user = user
        self.password = password
        self.database = database
        self.hostname = hostname
        self._connection = None

    def __enter__(self):
        self.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @property
    def connection(self):
        return self._connection

    def connect(self):
        if not self._connection:
            self._connection = mysql.connect(host=self.hostname, user=self.user, passwd=self.password, db=self.database)
            self._connection.set_character_set('utf8')

    def close(self):
        if self._connection:
            self._connection.close()


def create_tables(hostname, user, password, database):
    database = mysql.connect(host=hostname, user=user, passwd=password, db=database)
    cursor = database.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INT(11) NOT NULL AUTO_INCREMENT, 
            name CHAR(30) NOT NULL, 
            description CHAR(255) NOT NULL, 
            PRIMARY KEY(id)
        );
    """)
    database.commit()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS groups (
            id INT NOT NULL AUTO_INCREMENT,
            group_index CHAR(30) NOT NULL,
            PRIMARY KEY(id),
            UNIQUE (group_index)
        );
    """)
    database.commit()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INT NOT NULL AUTO_INCREMENT,
            first_name CHAR(255) NOT NULL,
            last_name CHAR(255) NOT NULL,
            group_id INT NOT NULL,
            PRIMARY KEY(id),
            FOREIGN KEY(group_id) REFERENCES groups(id)
        );
    """)
    database.commit()

    cursor.close()
    database.close()
