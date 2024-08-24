from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import yaml
import psycopg2
from typing import List, Optional

class Q:
    def __init__(self):
        with open("config_yaml/pg.yaml") as f:
            self.config = yaml.safe_load(f)
        self.connect()
    
    def connect(self):
        self.con = psycopg2.connect(
            host=self.config['host'], 
            database=self.config['database'], 
            port=self.config['port'], 
            user=self.config['username'], 
            password=self.config['password']
        )
        self.cur = self.con.cursor()
    
    def add(self, username, product_name, product_description, product_price, product_category, image):
        self.cur.execute(
            "INSERT INTO products(owner, productname, product_description, product_price, category, image) VALUES (%s, %s, %s, %s, %s, %s) RETURNING productid",
            (username, product_name, product_description, product_price, product_category, image)
        )
        product_id = self.cur.fetchone()[0]
        self.con.commit()
        category_list = product_category.split()
        for category in category_list:
            self.cur.execute(f"UPDATE categories SET {category} = TRUE WHERE product_id = %s", (product_id,))
        self.con.commit()
        return product_id
    
    def view1(self):
        self.cur.execute("SELECT productid, productname, product_price FROM products;")
        return self.cur.fetchall()

    def choose(self, n):
        self.cur.execute("SELECT * FROM products WHERE productid = %s;", (n,))
        return self.cur.fetchone()
    
    def search(self, nameproduct):
        self.cur.execute("SELECT * FROM products WHERE productname LIKE %s;", (f'%{nameproduct}%',))
        return self.cur.fetchall()
    
    def info(self, username):
        self.cur.execute("SELECT username, name FROM users WHERE username = %s;", (username,))
        return self.cur.fetchone()
    
    def myproduct(self, username):
        self.cur.execute("SELECT * FROM products WHERE owner = %s;", (username,))
        return self.cur.fetchall()

class Product(BaseModel):
    product_name: str
    product_description: str
    product_price: float
    product_category: str
    image: str

app = FastAPI()

def get_db():
    db = Q()
    try:
        yield db
    finally:
        db.cur.close()
        db.con.close()

@app.post("/add")
def add_product(product: Product, username: str = "mohsen", db: Q = Depends(get_db)):
    product_id = db.add(username, product.product_name, product.product_description, product.product_price, product.product_category, product.image)
    return {"product_id": product_id}

@app.get("/view1")
def view_all_products(db: Q = Depends(get_db)):
    products = db.view1()
    return {"products": products}

@app.get("/choose/{product_id}")
def choose_product(product_id: int, db: Q = Depends(get_db)):
    product = db.choose(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"product": product}

@app.get("/search")
def search_product(nameproduct: str, db: Q = Depends(get_db)):
    products = db.search(nameproduct)
    return {"products": products}

@app.get("/info")
def user_info(username: str = "mohsen", db: Q = Depends(get_db)):
    user = db.info(username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"user": user}

@app.get("/myproduct")
def user_products(username: str = "mohsen", db: Q = Depends(get_db)):
    products = db.myproduct(username)
    return {"products": products}

#  dev fastapi --reload
