
import sqlite3

connection = sqlite3.connect("KURSLAR")
cursor = connection.cursor()


cursor.execute("""create table if not exists course(
    id integer primary key,
    title varchar (10),
    description varchar,
    mentor varchar ,
    during integer,
    price integer,
    completed varchar
    );
""")



course_add = """
        insert into course (title, description, mentor, during, price, completed) values (?, ?, ?, ?, ?, ?);
    """


kurslar = cursor.execute(""" select * from course""").fetchall()





def commit(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        connection.commit()
        return result
    return wrapper