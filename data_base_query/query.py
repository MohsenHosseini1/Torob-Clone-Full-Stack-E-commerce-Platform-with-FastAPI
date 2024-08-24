import yaml
import psycopg2

class q: #q manzor query 
    def __init__(self):
         with open("config_yaml\\pg.yaml") as f:
              self.config = yaml.safe_load(f)
    def connect(self): #ijad connection ba database
        self.con = psycopg2.connect(host=self.config['host'], database=self.config['database'], port=self.config['port'], user=self.config['username'], password=self.config['password'])
        self.cur = self.con.cursor()
    def reg(self, username, password, name):
        self.cur.execute(f"insert into users(username, passwd, name) values('{username}', '{password}', '{name}')")
        self.con.commit()
    def loggin(self, u, p):
        self.cur.execute(f"select username, passwd from users where username = '{u}'and passwd = '{p}'")
        return bool(self.cur.fetchone())
    def add(self,username, product_name, product_description, product_price,product_category,image):
        self.cur.execute(f"insert into products(owner, productname, product_description, product_price,category,image) values('{username}', '{product_name}', '{product_description}', '{product_price}','{product_category}','{image}')")
        self.con.commit()
        self.cur.execute(f"SELECT productid FROM products where owner = '{username}' and productname = '{product_name}';")
        g = self.cur.fetchall()
        s = g[0][0]
        self.cur.execute(f"insert into categories(product_id) values({s})")
        self.con.commit()
        category = product_category.split()
        for i in category:
            self.cur.execute(f"update categories set {i} = TRUE  where product_id = '{s}'")
            self.con.commit()
    def view1(self):
        self.cur.execute("SELECT productid, productname, product_price FROM products;")
        print(self.cur.fetchall())
    def choose(self , n ):
        self.cur.execute(f"SELECT * FROM products where productid = {n};")
        print(self.cur.fetchall())
    def like(self, n):
        self.cur.execute(f"update products set product_like = product_like + 1 where productid = '{n}'")
        self.con.commit()
        print("liked❤")
    def save(self, n,username):
        self.cur.execute(f"SELECT saveditem FROM users where username = '{username}';")
        savenow = self.cur.fetchall()
        b = str(savenow) + n
        print(b)
        
        ''''self.cur.execute(f"update users set saveditem = saveditem + '{d}' where username = '{username}'")
        self.con.commit()'''
        print("save")
    def search(self , nameproduct ):
        self.cur.execute(f"SELECT * FROM products WHERE productname LIKE '%{nameproduct}%';")
        print(self.cur.fetchall())
    def info(self,username):
        self.cur.execute(f"SELECT username,name FROM users where username = '{username}';")
        print(self.cur.fetchall())
    def update_pass(self, u, p):
        self.cur.execute(f"update users set passwd = '{p}' where username = '{u}' ")
        self.con.commit()
    def category(self,x):
        self.cur.execute(f"SELECT product_id FROM categories where {x} = TRUE;")
        v = self.cur.fetchall()
        for b in v:
            j = b[0]
            self.cur.execute(f"SELECT productid, productname, product_price FROM products where productid = '{j}';")
            print(self.cur.fetchall())
    def myproduct(self,username):
        self.cur.execute(f"SELECT * FROM products where owner = '{username}';")
        print(self.cur.fetchall())
