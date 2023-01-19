from config import DataBase

try:
    session = DataBase().connect()
except Exception as err:
    while err:
        if type(err) == BaseException:
            session = DataBase().connect()
