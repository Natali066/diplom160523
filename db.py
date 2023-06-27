import sqlalchemy
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import Session

metadata = MetaData()
Basis = declarative_base()

import sqlalchemy as sq
from sqlalchemy.orm import declarative_base
from sqlalchemy import creativ_engine Metadata
from sqlalchemy.orm import Session

from config import dbl_url_object

metadata = MetaData()
Base = declarativ_base()


class Viewed(Base):
    __tablename__ = 'viewed'
    profile_id = sq.Column (sq.Integer, primary_key = True)
    worksheet_id = sq.Column(sq.Integer, primary_key=True)

def add_user(engine, profile_id, worksheet_id):
    with Session(engine) as session:
        to_bd = Viewed(profile_id=profile_id, worksheet_id=worksheet_id)
        session.add(to_bd)
        session.commit()

def chek_user(engine, profile_id, worksheet_id):
    with Session(engine) as session:
        from_bd = session.query(Viewed).filter(
            Viewed.profile_id == profile_id,
            Viewed.worksheet_id == worksheet_id
        ). first()
        return True if from_bd else False

if __name__ == '__main__':
    engine = create_engine(db_url_object)
    Base.metadata.create_all(engine)
    res = chek_user(engine, 2113, 1245121)
    print(res)


def new_user(self, user_id: Viewed) -> bool:
    sql = f"""
            SELECT * FROM users_id WHERE vk_id={user_id.vk_id};
            """
        result = self.connection.execute(sql).fetchone()
        # если запрос выполнился успешно
        if result is None:
            # нет такого пользователя в базе данных
            sql = f"""
                INSERT INTO vk_users (vk_id, name_user, lastname_user, bdate, sex, city, vkdomain, last_visit, settings) 
                VALUES ({user_id.vk_id},'{user_id.name_user}','{user_id.lastname_user}','{user_id.bdate}',{user_id.sex},{user_id.city},'{user_id.vkdomain}','{user_id.last_visit}', ,{user_id.settings});
                """
        else:
            # пользователь уже существует в базе данных
            sql = f"""
                UPDATE vk_users SET last_visit = '{user_id.last_visit}' WHERE vk_id = {user_id.vk_id};
                """
        result = self.connection.execute(sql)
        # если запрос выполнился с ошибкой
        if result is None:
            return False
        # успешный результат
        return True
 


# coding=utf-8
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
