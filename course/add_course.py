
from tableC import cursor, course_add, commit
from ranglar import yashil

@commit
def c_add():
    title = input("Turi:  ")
    description = input("Ta'rif: ")
    mentor = input("O'qituvchi: ")
    during = int(input("Kurs davomiyligi (oy): "))
    price = int(input("Kurs narxi (har oy uchun): "))
    completed = input("Kurs boshlanganmi? : ")
    olish = (title, description, mentor, during, price, completed)
    cursor.execute(course_add, olish)
    yashil("Muvvofaqqiyatli qo'shildi")
