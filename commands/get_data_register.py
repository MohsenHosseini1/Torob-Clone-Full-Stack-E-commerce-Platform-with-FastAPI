from getpass import getpass
def info():
    username = input("username: ")
    name = input("name: ")
    passwd = getpass("password: ")
    return username, passwd, name