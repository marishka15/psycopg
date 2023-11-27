import psycopg2

def create_db(conn):
    with conn.cursor() as cur:
        cur.execute("""
        DROP TABLE phone;
        DROP TABLE data;
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS data(
        id SERIAL PRIMARY KEY,
        name VARCHAR(40),
        lastname VARCHAR(60),
        email VARCHAR(40)
        );
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS phone(
        phone_id SERIAL PRIMARY KEY,
        phone VARCHAR(40),
        id INTEGER NOT NULL REFERENCES data(id)
        );
        """)
        conn.commit()

def add_client(conn, firstname, lastname, email, phone=None):
    with conn.cursor() as cur:
        cur.execute("""INSERT INTO data (name, lastname, email) VALUES(%s, %s, %s);"""
        , (firstname, lastname, email))


        cur.execute("""
        SELECT * FROM data;
              """)
        return cur.fetchall()

def add_phone(conn, id, phone):
    with conn.cursor() as cur:
        cur.execute("""INSERT INTO phone (id, phone) VALUES (%s, %s);
        """, (id, phone))


        cur.execute("""
        SELECT * FROM phone;
                """)
        return cur.fetchall()

def change_client(conn, id, name=None, lastname=None, email=None, phone=None):
    with conn.cursor() as cur:
        cur.execute("""UPDATE data SET email=%s WHERE id=%s;
        """, (email, id))

        cur.execute("""
        SELECT * FROM data;
                """)
        return cur.fetchall()[1]


def delete_phone(conn, id, phone):
    with conn.cursor() as cur:
        cur.execute("""DELETE FROM phone
        WHERE id=%s AND phone=%s;
        """, (id, phone))

        cur.execute("""
        SELECT * FROM phone;
                """)
        return cur.fetchall()

def delete_client(conn, id):
    with conn.cursor() as cur:
        cur.execute("""DELETE FROM data WHERE id=%s;
        """, (id,))

        cur.execute("""
        SELECT * FROM data;
                """)
        return cur.fetchall()

def find_client(conn, name=None, lastname=None, email=None, phone=None):
    with conn.cursor() as cur:
        cur.execute("""SELECT * FROM data d
        JOIN phone p ON d.id = p.id
        WHERE phone=%s;
        """, (phone,))
        return cur.fetchall()[0]

if __name__ == "__main__":
    with psycopg2.connect(database="postgresql_python", user="postgres", password="DilanOBrayen69") as conn:
        create_db(conn)
        add_client(conn, 'Иван', 'Петров', '5757@mail.ru')
        print(add_client(conn,'Семён', 'Соколов', 'sokol33@gmail.com'))
        add_phone(conn, 1, '+79998086576')
        print(add_phone(conn, 2, '+78657293478'))
        print(change_client(conn, 1, email='petrovi@mail.ru'))
        print(delete_phone(conn, 1, phone='+79998086576'))
        print(delete_client(conn, 1))
        print(find_client(conn, phone='+78657293478'))

    conn.close()
