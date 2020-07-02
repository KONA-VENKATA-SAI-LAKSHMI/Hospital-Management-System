from flask import Flask
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

if __name__ == '__main__':
    app.run(debug=True)

#Importing routes.py
from hms import Routes