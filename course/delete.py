
from hammasi import show_all
from tableC import cursor, commit
from ranglar import sariq, qizil

@commit
def trash():
    show_all()
    id = int(input("ID =====> "))
    yana = cursor.execute(f"""select * from course where id={id}""").fetchone()
    if not yana:
        qizil("Xato ma'lumot kiritildi")

    else:
        cursor.execute(f"""
        delete from course where id={id}
        """)
        sariq("O'chirildi: ")