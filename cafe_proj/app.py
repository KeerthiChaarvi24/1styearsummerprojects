from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/order', methods=['POST'])
def order():
    prices={
        "Coffee":250,
        "Cookie":99,
        "Cake":150
    }
    item = request.form['item']
    price=prices[item]
    return f"You selected {item} cost {price}"

if __name__ == '__main__':
    app.run(debug=True)