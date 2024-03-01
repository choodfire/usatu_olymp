from pymysql import Connection


def init_db(db: Connection) -> None:
    with open('database/schema.sql', encoding='utf-8') as f:
        command = f.read()
        with db.cursor() as cursor:
            cursor.execute(command)
