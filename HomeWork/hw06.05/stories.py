from flask import Flask, render_template, g, request, flash
import sqlite3

with sqlite3.connect('life_stories.db') as con:
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS history_peoples(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    story TEXT
    )
    """)
# menu = [
#     ('Главная',  '/'),
#     ('Добавьте свою историю', '/make_history'),
# ]
# with sqlite3.connect('menu_point.db') as con:
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS menu(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT,
#     url TEXT
#     )
#     """)
#     for m in menu:
#         cur.execute('INSERT INTO menu VALUES(NULL,?,?)', m)

app = Flask('__name__')
app.config['SECRET_KEY'] = '56343821a12b4f8f275a563a880104bf86053beb'


def get_post(db, story_id):
    try:
        curs = db.cursor()
        curs.execute(f"SELECT name,story FROM history_peoples WHERE id={story_id}")
        res = curs.fetchone()
        print(res)
        if res:
            return res
    except sqlite3.Error as e:
        print('Ошибка получения из БД' + str(e))
    return False, False


def get_posts_anonce(db):
    try:
        curs = db.cursor()
        curs.execute("SELECT id,name,story FROM history_peoples ORDER BY id DESC")
        res = curs.fetchall()
        if res:
            return res
    except sqlite3.Error as e:
        print('Ошибка получения статей из БД' + str(e))


def add_post(db, title, text):
    try:

        curs = db.cursor()
        curs.execute("INSERT INTO history_peoples VALUES(NULL,?,?)", (title, text))
        db.commit()

    except sqlite3.Error as e:
        print('Ошибка добавления статьи в БД' + str(e))
        return False
    return True


def connect_db():
    con = sqlite3.connect('life_stories.db')
    con.row_factory = sqlite3.Row
    return con


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


def get_menu():
    con = sqlite3.connect('menu_point.db')
    cur = con.cursor()
    cur.execute('SELECT name,url FROM menu')
    menu = cur.fetchall()
    print(menu)
    return menu


@app.route('/')
def head():
    db = get_db()
    return render_template('attraction.html', title='Главная', menu=get_menu(), stories=get_posts_anonce(db))


@app.route('/make_history', methods=['POST', 'GET'])
def make_history():
    db = get_db()
    if request.method == 'POST':
        if len(request.form['name']) > 4 and len(request.form['story']) > 10:
            res = add_post(db, request.form['name'], request.form['story'])
            if not res:
                flash('Ошибка добавления истории!!!', category='error')
            else:
                flash('История добавлена успешно!!!', category='success')
        else:
            flash('Ошибка добавления истории!!!', category='error')
    return render_template('make_history.html', title="Запишите свою историю", menu=get_menu())


@app.route('/story/<int:id_story>')
def show_story(id_story):
    db = get_db()
    print(id_story)
    name, story = get_post(db, id_story)

    return render_template('story.html', title="История", menu=get_menu(), name=name, story=story)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html', title='Страница не найдена', menu=get_menu())


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


if __name__ == '__main__':
    app.run(debug=True)
