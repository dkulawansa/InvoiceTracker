from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = '5eff0e854b7a55a95084e52fa4a1ae43'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:tiger@localhost/testdb'
db= SQLAlchemy(app)
bootstrap = Bootstrap(app)


from invoice import routes