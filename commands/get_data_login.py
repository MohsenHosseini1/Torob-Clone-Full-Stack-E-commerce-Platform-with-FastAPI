from getpass import getpass
def login():
    username = input("username: ")
    passwd = getpass("password: ")
    return username, passwd