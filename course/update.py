from ranglar import yashil, qizil
from hammasi import show_all
from tableC import cursor, commit



@commit
def update():
    show_all()
    id = int(input("ID ======> "))
    bitta = cursor.execute(f""" select * from course where id={id} """)

    if not bitta:
        qizil("Noto'g'ri ma'lumot kiritildi: ")
    else:
        title = input("Turi:  ")
        description = input("Ta'rif: ")
        mentor = input("O'qituvchi: ")
        during = int(input("Kurs davomiyligi (oy): "))
        price = int(input("Kurs narxi (har oy uchun): "))
        completed = input("Kurs boshlanganmi? : ")
        cursor.execute(f"""
        update course set title="{title}" , description="{description}", mentor="{mentor}", during="{during}", price="{price}", completed="{completed}"
        """)
        yashil("muvvofaqqiyatli saqlandi")