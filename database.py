from connect import *
import logging
logging.basicConfig(
    level=logging.DEBUG,
    filename="database.log",
    filemode="w"
)


def insert(table, data):
    try:
        keys = list(data.keys())
        keys_with_accent = ["`" + key + "`" for key in keys]
        values = list(data.values())

        key_string = ",".join(keys_with_accent)
        length = len(keys)
        sub = ",".join(["%s"] * length)

        sql = f"INSERT INTO `{table}` ({key_string}) VALUES ({sub})"

        with connection.cursor() as cursor:
            cursor.execute(sql, values)

        connection.commit()

        return cursor.lastrowid
    except pymysql.DataError as e:
        logging.critical(e.args[1])
        logging.critical(data)


def init(table):
    with connection.cursor() as cursor:
        cursor.execute(f"TRUNCATE TABLE {table}")


def select(table):
    try:
        sql = f"SELECT * FROM {table}"

        with connection.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()
    except pymysql.DataError as e:
        logging.critical(e.args[1])
