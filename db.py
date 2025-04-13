import mysql.connector

def connect_db():
    # Connect to MySQL
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="celeron",
        database="kfood_pos"
    )


def get_table_names():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES")
    tables = [row[0] for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return tables


def get_primary_key(table_name):
    conn = connect_db()
    cursor = conn.cursor()
    query = f"""
        SELECT COLUMN_NAME
        FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
        WHERE TABLE_SCHEMA = DATABASE()
          AND TABLE_NAME = '{table_name}'
          AND CONSTRAINT_NAME = 'PRIMARY'
    """
    cursor.execute(query)
    primary_key = cursor.fetchone()[0] if cursor.fetchone() else None
    cursor.close()
    conn.close()
    return primary_key


def get_columns(table_name):
    conn = connect_db()
    cursor = conn.cursor()
    query = f"DESCRIBE {table_name}"
    cursor.execute(query)
    columns = cursor.fetchall()
    col_names = [col[0] for col in columns]
    cursor.close()
    conn.close()
    return col_names


def get_foreign_keys(table_name):
    conn = connect_db()
    cursor = conn.cursor()
    query = f"""
        SELECT COLUMN_NAME, REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME
        FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
        WHERE TABLE_SCHEMA = DATABASE()
          AND TABLE_NAME = '{table_name}'
          AND REFERENCED_TABLE_NAME IS NOT NULL
    """
    cursor.execute(query)
    foreign_keys = cursor.fetchall()
    cursor.close()
    conn.close()
    return foreign_keys


def get_columns_for_table(table_name, schema):
    conn = connect_db()
    cursor = conn.cursor()
    query = """
        SELECT COLUMN_NAME
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_SCHEMA = %s
          AND TABLE_NAME = %s
          AND EXTRA NOT LIKE '%%auto_increment%%'  -- Exclude auto-increment primary keys
    """
    cursor.execute(query, (schema, table_name))
    result = [row[0] for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return result