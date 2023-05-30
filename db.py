import sqlalchemy
from sqlalchemy.orm import declarative_base

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import Session

metadata = MetaData()
Basis = declarative_base()


class Candidate(Basis):
    __tablename__ = 'cfndidate'
    profile_id = sq.Column(sq.Integer, primary_key=True)
    worksheet_id = sq.Column(sq.Integer, primary_key=True)

# добавление записи в бд
engine = create_engine(db_url_object)
Basis.metadata.create_all(engine)
with Session(engine) as session:
    to_bd = Candidat(profile_id=1, worksheet_id=1)
    session.add(to_bd)
    session.commit()

# извлечение записей из БД
engine = create_engine(db_url_object)
with Session(engine) as session:
    from_bd = session.query(Candidat).filter(Candidat.profile_id == 1).all()
    for item in from_bd:
        print(item.worksheet_id)
        
# функция сохранения данных о пользователе ВКонтакте в базу данных
# возвращае True, если данные сохранены в базе данных, иначе False
    def new_vkuser(self, user_id: VKUser) -> bool:
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
