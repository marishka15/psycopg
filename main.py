import psycopg2

def create_db(conn):
    with conn.cursor() as cur:
        cur.execute("""
        DROP TABLE data;""")

        cur.execute("""
        CREATE TABLE IF NOT EXISTS data(
        id SERIAL PRIMARY KEY,
        name VARCHAR(40),
        lastname VARCHAR(60),
        email VARCHAR(40),
        phone VARCHAR(20)
        );
        """)
        conn.commit()

def add_client(conn, firstname, lastname, email, phones=None):
    with conn.cursor() as cur:
        cur.execute("""INSERT INTO data (name, lastname, email) VALUES(%s, %s, %s);"""
        , (firstname, lastname, email))
        cur.execute("""
        SELECT * FROM data;
                """)
        print(cur.fetchall())

def add_phone(conn, id, phone):
    with conn.cursor() as cur:
        cur.execute("""UPDATE data SET phone=%s WHERE id=%s;
        """, (id, phone))
        cur.execute("""
        SELECT * FROM data;
                """)
        print(cur.fetchall())
def change_client(conn, id, name=None, lastname=None, email=None, phone=None):
    with conn.cursor() as cur:
        cur.execute("""UPDATE data SET name=%s, lastname=%s, email=%s, phone=%s WHERE id=%s;
        """, (id, name, lastname, email, phone))
        cur.execute("""
        SELECT * FROM data;
                """)
        print(cur.fetchall())
def delete_phone(conn, id, phone):
    pass

def delete_client(conn, id):
    with conn.cursor() as cur:
        cur.execute("""DELETE FROM data WHERE id=%s;
        """, (id,))
        cur.execute("""
        SELECT * FROM data;
                """)
        print(cur.fetchall())
#def find_client(conn, name=None, lastname=None, email=None, phone=None):
#    with conn.cursor() as cur:
#        cur.execute("""SELECT id FROM data WHERE name=%s AND lastname=%s AND email=%s AND phone=%s;
#        """, (name, lastname, email, phone))
#        cur.execute("""
#        SELECT * FROM data;
#                """)
#        print(cur.fetchall())

with psycopg2.connect(database="postgresql_python", user="postgres", password="DilanOBrayen69") as conn:
    add_client(conn, 'Пётр', 'Иванов', '464646@mail.ru')
    #########################################
    add_phone(conn,'+79029383789', 1)
    #################################
    change_client(conn,'Пётр', 'Иванов', 'petriv@mail.ru', '+79826754365', 1)
    ################################
    delete_phone(conn, 1, '+79826754365')
    ########################################
    delete_client(conn, 4)
    ######################################
    #find_client(conn, 'Пётр', 'Иванов', 'petriv@mail.ru', '+79826754365')

conn.close()