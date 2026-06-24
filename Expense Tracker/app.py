from flask import Flask, render_template, request, redirect
import mysql.connector as mysql

app = Flask(__name__)


db= mysql.connect(
    host="localhost",
    user="root",
    password="imsocool24@13",
    database="ExpenseTracker")
cursor=db.cursor()
    

@app.route('/')
#This code defines the default home page for a Python Flask web application. When someone visits the root URL of your website (e.g., http://localhost:5000/), it triggers the home() function, which loads and displays your index.html
def home():
    return render_template('index.html')

@app.route('/login',methods=['POST'])
def login():
    email=request.form['email']
    phone=request.form['phone']
    cursor.execute("select * from customers where email=%s or phone=%s",(email,phone))
    customer=cursor.fetchone()
    if customer:
        customer_id=customer[0]
    else:
        cursor.execute("insert into customers(name, email, phone) values (%s, %s, %s)"(name, email, phone))
        db.commit()
        customer_id=cursor.lastrowid
    return redirect(f'/customer/{customer_id}')

@app.route('/customer/<int:customer_id')
def customer_dashboard(customer_id):
    cursor.execute("select * from customers where id = %s",(customer_id,))
    customer=cursor.fetchone()
    cursor.execute("select( * from orders where customer_id= %s",(customer_id))
    orders=cursor.fetchall()
    return render-template('customer.html', customer=customer,orders=orders)

@app.route('/add',methods=['POST'])
def add_expenses():
    spendings=request.form['spendings']
    spent_on=request.form['spent_on']
    query="insert into dailytracker(spendings, spent_on) values(%s ,%s)"
    cursor.execute(query,(spendings,spent_on))
    db.commit()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)