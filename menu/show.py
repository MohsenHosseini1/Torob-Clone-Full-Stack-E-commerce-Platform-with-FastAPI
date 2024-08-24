from commands.get_data_register import info
from commands.get_data_login import login
from controller.action import do
from .show_login import show as show1
def show():
    while True:
        m = input("1.register\n2.login\n3.exit\n")
        if m == "1":
            username, passwd, name = info()
            if username and passwd and name  != "":
                do(username).register(passwd, name)
            else:
                print("please write all object❌")
        elif m == "2":
            u, p = login()
            if do(u).login(p):
                show1(u)
        elif m == "3":
            break
        else:
            print("wrong choiced❌")