from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

@app.route("/")
def home():

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="imsocool24@13",
        database="cafe_db"
    )

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products")

    products = cursor.fetchall()

    conn.close()

    return str(products)

@app.route("/order", methods=["POST"])
def order():

    product_id = request.form["product_id"]

    conn = sqlite3.connect("cafe.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO cart(product_id) VALUES(?)",
        (product_id,)
    )

    conn.commit()
    conn.close()

    return redirect("/")


@app.route("/cart")
def cart():

    conn = sqlite3.connect("cafe.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT products.name,
           products.price
    FROM cart
    JOIN products
    ON cart.product_id = products.id
    """)

    items = cursor.fetchall()

    cursor.execute("""
    SELECT SUM(products.price)
    FROM cart
    JOIN products
    ON cart.product_id = products.id
    """)

    total = cursor.fetchone()[0]

    conn.close()

    if total is None:
        total = 0

    return render_template(
        "cart.html",
        items=items,
        total=total
    )


if __name__ == "__main__":
    app.run(debug=True)