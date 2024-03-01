from pymysql import Connection


def init_db(db: Connection) -> None:
    with open('database/schema_users.sql', encoding='utf-8') as f_users:
        sql_users = f_users.read()
    with open('database/schema_payments.sql', encoding='utf-8') as f_pensions:
        sql_pensions = f_pensions.read()
    with db.cursor() as cursor:
        cursor.execute(sql_users)
        cursor.execute(sql_pensions)


def select_all_users_payments(db: Connection) -> tuple[str, str, float]:
    sql = ("SELECT users.id, users.fio, payments.type, payments.amount FROM users INNER JOIN payments ON "
           "users.id=payments.user_id;")
    with db.cursor() as cursor:
        cursor.execute(sql)
    result = cursor.fetchall()

    return result


def select_all_users(db: Connection) -> tuple[str, str]:
    sql = ("SELECT users.id, users.fio FROM users")
    with db.cursor() as cursor:
        cursor.execute(sql)
    result = cursor.fetchall()

    return result
