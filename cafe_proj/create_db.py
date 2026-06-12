import sqlite3

conn = sqlite3.connect("cafe.db")
cursor = conn.cursor()

print("PRODUCTS TABLE")
cursor.execute("SELECT * FROM products")
products = cursor.fetchall()

for row in products:
    print(row)

print("\nCART TABLE")
cursor.execute("SELECT * FROM cart")
cart = cursor.fetchall()

for row in cart:
    print(row)

conn.close()