from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)


def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="imsocool24@13",
        database="cafe"
    )


@app.route("/")
def home():

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    conn.close()

    return render_template(
        "index.html",
        products=products
    )


@app.route("/order", methods=["POST"])
def order():

    product_id = request.form["product_id"]

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO cart(product_id) VALUES(%s)",
        (product_id,)
    )

    conn.commit()
    conn.close()

    return redirect("/")


@app.route("/cart")
def cart():

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT cart.id,
            products.name,
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

    if total is None:
        total = 0

    conn.close()

    return render_template(
        "cart.html",
        items=items,
        total=total
    )
@app.route("/remove", methods=["POST"])
def remove():
    conn=get_db_connection()
    cursor=conn.cursor()
    cart_id=request.form.get("cart_id")
    cursor.execute("""delete from cart where id= %s""",(cart_id,))
    conn.commit()
    conn.close()
    return redirect("/cart")


if __name__ == "__main__":
    app.run(debug=True)