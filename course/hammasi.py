from tableC import commit, cursor


@commit
def show_all():
    for course in cursor.execute(""" select * from course""").fetchall():
        print(course)