import psycopg2

def build_connection(database, user):
    return psycopg2.connect(database = database, user = user)

def get_cursor(conn):
    return conn.cursor()

def add_records(cursor,table,columns,values):
    #var = f'INSERT INTO {table} ({",".join(columns)}) VALUES {tuple(values)}'
    #breakpoint()
    cursor.execute(f'INSERT INTO {table} ({",".join(columns)}) VALUES {tuple(values)}')

def drop_records(cursor,table):
    cursor.execute(f'TRUNCATE {table}')

def close_conn(conn):
    conn.close()

