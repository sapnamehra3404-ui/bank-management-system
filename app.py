 HEAD
from flask import Flask, render_template, request
from bank import Bank

from flask import Flask, render_template
114b23f77cb906b9c75572438d9445dd2df48a9a

app = Flask(__name__)

@app.route('/')
def home():
HEAD
    return render_template("index.html")

@app.route('/create', methods=['GET','POST'])
def create():
    if request.method == 'POST':
        obj = Bank()
        result = obj.CreateAccount(
            request.form['name'],
            request.form['age'],
            request.form['phone'],
            request.form['email'],
            request.form['pin']
        )
        return result
    return render_template("create.html")


from flask import request, render_template

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':

        account = request.form.get('account')
        pin = request.form.get('pin')

        # Empty field check
        if not account or not pin:
            return render_template("login.html", error="All fields are required!")

        obj = Bank()
        result = obj.Login(account, pin)

        # Agar login fail hua
        if result == "Account not found":
            return render_template("login.html", error="Account not found!")

        if result == "Invalid PIN":
            return render_template("login.html", error="Wrong PIN!")

        # Agar login success
        return render_template("login.html", success="Login Successful!")

    return render_template("login.html")

@app.route('/deposit', methods=['GET','POST'])
def deposit():
    if request.method == 'POST':
        obj = Bank()
        result = obj.Deposit(
            request.form['account'],
            request.form['amount']
        )
        return result
    return render_template("deposit.html")

@app.route('/balance', methods=['GET','POST'])
def balance():
    if request.method == 'POST':
        obj = Bank()
        result = obj.CheckBalance(
            request.form['account']
        )
        return result
    return render_template("balance.html")

@app.route('/withdraw', methods=['GET','POST'])
def withdraw():
    if request.method == 'POST':
        obj = Bank()
        result = obj.Withdraw(
            request.form['account'],
            request.form['amount']
        )
        return result
    return render_template("withdraw.html")   

if __name__ == "__main__":
    app.run(debug=True)


    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/deposit')
def deposit():
    return render_template('deposit.html')

if __name__ == '__main__':
    app.run(debug=True)
114b23f77cb906b9c75572438d9445dd2df48a9a
