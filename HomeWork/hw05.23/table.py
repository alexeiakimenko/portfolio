import sqlite3

products1 = [
    (48390, 'Сметана 15% 1л.', '143,6'),
    (48393, 'Масло сливочное 1кг.', '364,9'),
    (48394, 'Масло подсолнечное 1л.', '78,3'),
    (48397, 'Сахар-песок 1кг.', '37,4'),
    (48399, 'Мука пшеничная 1кг.', '30,5')
]
products2 = [
    (40790, 'Гречневая крупа 1кг.', '48,2'),
    (40793, 'Рис шлифованный 1кг.', '49,7'),
    (40795, 'Свинина 1кг.', '248,7'),
    (40797, 'Говядина 1кг.', '327,3'),
    (40800, 'Мясо кур 1кг.', '114,1')
]

with sqlite3.connect('food.db') as con:
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code INTEGER,
    name TEXT,
    price TEXT
    )
    """)
    cur.execute("INSERT INTO products VALUES(1,47290,'Хлеб ржано-пшеничный','42,4')")
    cur.execute("INSERT INTO products VALUES(2,47292,'Хлеб белый','43,9')")
    cur.execute("INSERT INTO products VALUES(3,47295,'Яйцо куриное дес.','55,3')")
    cur.execute("INSERT INTO products VALUES(4,47298,'Молоко 2,5% 1л.','46,8')")
    cur.execute("INSERT INTO products VALUES(5,47299,'Творог 5% 1кг.','249,8')")
    for prod in products1:
        cur.execute("INSERT INTO products VALUES(NULL,?,?,?)", prod)
    cur.executemany("INSERT INTO products VALUES(NULL,?,?,?)", products2)
