import mysql.connector
import psycopg2
from psycopg2 import sql
import json

# MySQL connection
mysql_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'alsharif_2022',
    'database': 'smart_poultry'
}

# PostgreSQL connection
postgres_config = {
    'host': 'localhost',
    'database': 'kuku_smart',
    'user': 'postgres',
    'password': 'postgres'
}

def get_mysql_data(table_name):
    """Fetch data from MySQL table."""
    try:
        conn = mysql.connector.connect(**mysql_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute(f"SELECT * FROM {table_name}")
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()

def insert_postgres_data(table_name, data):
    """Insert data into PostgreSQL table."""
    try:
        conn = psycopg2.connect(**postgres_config)
        cursor = conn.cursor()
        
        # Get column names from first row
        columns = data[0].keys()
        
        # Create SQL query
        query = sql.SQL("INSERT INTO {} ({}) VALUES ({})").format(
            sql.Identifier(table_name),
            sql.SQL(', ').join(map(sql.Identifier, columns)),
            sql.SQL(', ').join(sql.Placeholder() * len(columns))
        )
        
        # Execute for each row
        for row in data:
            cursor.execute(query, row)
        
        conn.commit()
    finally:
        cursor.close()
        conn.close()

def migrate_table(table_name):
    """Migrate a single table from MySQL to PostgreSQL."""
    print(f"\nMigrating table: {table_name}")
    data = get_mysql_data(table_name)
    if data:
        insert_postgres_data(table_name, data)
        print(f"Successfully migrated {len(data)} records")
    else:
        print("No data to migrate")

def main():
    # List of tables to migrate
    tables = [
        'activity_type_tb',
        'activity_schedule_tb',
        'batches_tb',
        'batch_activity_tb',
        'batch_feeding_tb',
        'breeds_tb',
        'breed_activities_tb',
        'breed_conditions',
        'breed_feeding_tb',
        'condition_types_tb',
        'food_types_tb',
        'farms_tb',
        'farmers_tb'
    ]
    
    for table in tables:
        migrate_table(table)

if __name__ == '__main__':
    main()
