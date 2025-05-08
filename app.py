from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Setup SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///firstapp.db'
db = SQLAlchemy(app)

# Model
class Students(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(50))
    lname = db.Column(db.String(50))
    age = db.Column(db.Integer)
    city = db.Column(db.String(50))

    def __repr__(self):
        return f'{self.sno} - {self.fname}'

# Routes
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        age = request.form['age']
        city = request.form['city']
        new_student = Students(fname=fname, lname=lname, age=age, city=city)
        db.session.add(new_student)
        db.session.commit()
    all_students = Students.query.all()
    return render_template('index.html', data=all_students)

@app.route('/home')
def home():
    return 'Welcome to the Home Page!'

if __name__ == '__main__':
    app.run(debug=True)
