from flask import Flask,render_template,request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/hello')
def hello():
    return "HEyeaaaa"
@app.route('/greet/<name>')
def greet(name):
    return f"HEyayaya {name}"
@app.route('/handle_url_params')
def handle_params():
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greeting=request.args['greeting']
        name=request.args['name']
        return f"{greeting} {name}"
    else:
        return "Some parameters are missing"
if __name__=="__main__":
    app.run(debug=True)
