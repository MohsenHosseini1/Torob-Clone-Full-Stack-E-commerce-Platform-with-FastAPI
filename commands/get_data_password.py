from getpass import getpass
def change_pass():
    p = getpass("Current password : ")
    return p
def change_pass2():
    p1 = getpass("New password : ")
    p2 = getpass("Repeat New password : ")
    return p1, p2