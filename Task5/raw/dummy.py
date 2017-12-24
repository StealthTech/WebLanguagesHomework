import MySQLdb as mysql


def run(hostname, user, password, database):
    database = mysql.connect(host=hostname, user=user, passwd=password, db=database)
    cursor = database.cursor()

    database.set_character_set('utf8')

    cursor.execute('INSERT INTO books (name, description) VALUES (%s, %s);', ('Книга', 'Описание книги'))

    database.commit()

    cursor.execute('SELECT * FROM books;')

    entries = cursor.fetchall()

    for entry in entries:
        print('> dummy :: {}'.format(entry))

    cursor.execute('TRUNCATE books;')

    cursor.close()
    database.close()

