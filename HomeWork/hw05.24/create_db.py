from db import create_db, Session
from product import Product
from buyer import Buyer
from faker import Faker

faker = Faker('ru_RU')
create_db()


def create(session):
    name_prod=[]
    product = [
        (47290, 'Хлеб ржано-пшеничный', '42,4'),
        (47292, 'Хлеб белый', '43,9'),
        (47295, 'Яйцо куриное дес.', '55,3'),
        (47298, 'Молоко 2,5% 1л.', '46,8'),
        (47299, 'Творог 5% 1кг.', '249,8'),
        (48390, 'Сметана 15% 1л.', '143,6'),
        (48393, 'Масло сливочное 1кг.', '364,9'),
        (48394, 'Масло подсолнечное 1л.', '78,3'),
        (48397, 'Сахар-песок 1кг.', '37,4'),
        (48399, 'Мука пшеничная 1кг.', '30,5'),
        (40790, 'Гречневая крупа 1кг.', '48,2'),
        (40793, 'Рис шлифованный 1кг.', '49,7'),
        (40795, 'Свинина 1кг.', '248,7'),
        (40797, 'Говядина 1кг.', '327,3'),
        (40800, 'Мясо кур 1кг.', '114,1')
    ]
    for pr in product:
        name_prod.append(pr[1])
        products = Product(pr[0], pr[1], pr[2])
        session.add(products)
    session.commit()
    for _ in range(10):
        name_buyers = faker.name()
        name_products = faker.random.choice(name_prod)
        quantity = faker.random.randint(5, 20)
        buy = Buyer(name_buyers, name_products, quantity)
        session.add(buy)
    session.commit()


create(Session())
