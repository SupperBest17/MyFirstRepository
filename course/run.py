from menu import menyu
from hammasi import show_all
from update import update
from add_course import c_add
from delete import trash
from ranglar import qizil


def runrunrun():
    while True:
        s = menyu()
        if s == "1" :
            show_all()
        elif s == "2" :
            c_add()
        elif s == "3" :
            update()
        elif s == "4" :
            trash()
        elif s == "5":
            break
        else:
            qizil("Xato ma'lumot kiritildi")

runrunrun()
