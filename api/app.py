from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy 
from flask_cors import CORS
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.config.from_pyfile('config.py')
app.debug = True

CORS(app)


from views import *


if __name__ ==  "__main__":
    app.run(debug=True)