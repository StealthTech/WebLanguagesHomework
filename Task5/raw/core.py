import dummy
from database import create_tables, Connection
from models import Student, Group

mysql_auth = {
    'hostname': 'localhost',
    'user': 'edu',
    'password': 'qweRTY#2',
    'database': 'edu_raw',
}

# Creating tables if not exist
create_tables(**mysql_auth)

# Adding a book, fetching 'em all, truncate table
dummy.run(**mysql_auth)

# Working with models
conn = Connection(**mysql_auth)
with conn:
    group = Group(conn, 'СГН3-71')
    group.save()
    groups = group.objects.all()
    for i, g in enumerate(groups, 1):
        print('Group #{}: {}'.format(i, g))

    print('> get :: Group #1: {}'.format(group.objects.get(id=1)))

    student = Student(conn, 'Михаил', 'Волынов', 1)
    student.save()
    students = student.objects.all()
    for i, s in enumerate(students, 1):
        print('Student #{}: {}'.format(i, s))

    print('> get :: Student #1: {}'.format(student.objects.get(id=1)))
    # student.objects.drop()

