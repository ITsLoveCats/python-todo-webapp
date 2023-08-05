from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

# create the extension
db = SQLAlchemy()
# initialize the app with the extension
db.init_app(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(100))
    complete = db.Column(db.Boolean)


@app.route('/')
def index():

    todo_list = Todo.query.all()
    print("------")
    print(todo_list)
    return render_template('base.html', todo_list=todo_list)
    # return render_template('base.html')


if __name__ == "__main__":
    # with app.app_context():
    #     db.create_all()

    app.run(debug=True)
