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
if __name__ == "__main__":
    app.run(debug=True)

@app.route('/add',methods=['POST'])
def add_expenses():
    spendings=request.form['spendings']
    spent_on=request.form['spent_on']
    query="insert into dailytracker(spendings, spent_on) values(%s %s)"
    cursor.execute(query,(spendings,spent_on))
    db.commit()
    return redirect('/')