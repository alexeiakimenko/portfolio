from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///courses.db'
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'llvclsdcfkflhtrktksljklwej4ljojeldsjlkvslzjvjlejptouwej'


class Course(db.Model):
    __tablename__ = 'for_students'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(), nullable=False)
    price = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'{self.title} - {self.price}'


@app.route('/', methods=['POST', 'GET'])
def index():
    courses = db.session.query(Course).all()
    return render_template('attraction.html', title='Каталог', courses=courses)


@app.route('/description/<alias>', methods=['POST', 'GET'])
def description(alias):
    print(alias)
    course = db.session.query(Course).filter(Course.title == alias).all()
    for c in course:
        title = c.title
        price = c.price
        desc = c.description

    return render_template('description.html', title=title, price=price, desc=desc)


@app.route('/change', methods=['POST', 'GET'])
def change():
    if request.method == 'POST':
        new_course = request.form['title']
        new_price = request.form['price']
        new_description = request.form['description']
        data = Course(title=new_course, price=new_price, description=new_description)
        print(data)
        try:
            db.session.add(data)
            db.session.commit()
        except Exception as e:
            return f'Не удалось добавить данные. {e} '
    return render_template('change.html', title='Внесение')


@app.route('/info', methods=['POST', 'GET'])
def info():
    return render_template('info.html', title='О нас')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
