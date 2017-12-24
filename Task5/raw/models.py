class Model:
    table_name = None


class ModelManager:
    def __init__(self, connection, model):
        self.connection = connection
        self.model = model

    def all(self):
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM {};'.format(self.model.table_name))
        result = cursor.fetchall()
        cursor.close()
        return result

    def get(self, **kwargs):
        cursor = self.connection.cursor()
        clause = ', '.join(['{} = {}'.format(k, v) for k, v in kwargs.items()])
        cursor.execute('SELECT * FROM {} WHERE {};'.format(self.model.table_name, clause))
        result = cursor.fetchone()
        cursor.close()
        return result

    def drop(self):
        cursor = self.connection.cursor()
        cursor.execute('TRUNCATE {};'.format(self.model.table_name))
        cursor.close()


class Group(Model):
    table_name = 'groups'

    def __init__(self, connection, index):
        self.connection = connection.connection
        self.index = index
        self.objects = ModelManager(self.connection, self) # Pseudo model manager, depends on connection

    def save(self):
        cursor = self.connection.cursor()
        cursor.execute('INSERT IGNORE INTO {}(group_index) VALUES (%s);'.format(self.table_name), (self.index,))
        self.connection.commit()
        cursor.close()


class Student(Model):
    table_name = 'students'

    def __init__(self, connection, first_name, last_name, group_id):
        self.connection = connection.connection
        self.first_name = first_name
        self.last_name = last_name
        self.group_id = group_id
        self.objects = ModelManager(self.connection, self)  # Pseudo model manager, depends on connection

    def save(self):
        cursor = self.connection.cursor()
        cursor.execute('INSERT INTO {}(first_name, last_name, group_id) VALUES (%s, %s, %s);'.format(self.table_name),
                       (self.first_name, self.last_name, self.group_id))
        self.connection.commit()
        cursor.close()

