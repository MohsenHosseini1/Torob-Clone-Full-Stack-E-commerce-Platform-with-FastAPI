from data_base_query.query import q
from .hash import hash_passwd
from commands.get_data_password import change_pass2
import hashlib
class do:
    def __init__(self,username):
        self.username = username
        self.obj = q()
        self.obj.connect()
    def register(self, password, name):
        password = hash_passwd(password) #hash kardan
        self.obj.reg(self.username, password, name)
        print("register successfully🎉")
    def login(self, p):
        p = hash_passwd(p)
        status = False
        if self.obj.loggin(self.username, p):
            print("logged in successfully🔑")
            status = True
        else:
            print("wrong username or password🔒")
        return status
    def add_product(self, product_name, product_description, product_price,product_category,image):
        self.obj.add(self.username, product_name, product_description, product_price,product_category,image)
        print(" successfully🎉")
    def view(self):
        self.obj.view1()
    def choosee(self, n):
        self.obj.choose(n)
    def likee(self,n):
        self.obj.like(n)
    def savedd(self,n):
        self.obj.save(n,self.username)
    def searchh(self,nameproduct):
        self.obj.search(nameproduct) 
    def infoo(self):
        self.obj.info(self.username)   
    def change_pass(self, p,p1,p2):
        password = hash_passwd(p)
        if self.obj.loggin(self.username, password):    
            print("ok")        
            if p1 == p2:
                password = hash_passwd(p1)
                self.obj.update_pass(self.username, password)
            else:
                print("passwords are not match")
        else:
            print("current password is wrong")
    def categoryy(self,x):
        self.obj.category(x) 
    def myproductt(self):
        self.obj.myproduct(self.username) 
