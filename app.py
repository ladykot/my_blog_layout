from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')
# db = SQLAlchemy(app)

# migrate = Migrate(webapp, db)  # связываем  текущее приложение с базой
# manager = Manager(webapp)
# manager.add_command("db", MigrateCommand)         