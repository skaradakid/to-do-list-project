from flask import Flask
from db import users

app = Flask(__name__)

@app.route("/")
def greet():
    name = input("enter your fullname> ")
    password = input('enter your password')
    if (name, password) in users:
        return "account already exist"
    else:
        users.append((name, password))

if __name__ == "__main__":
    app.run(debug=True)