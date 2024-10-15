import mysql.connector

def get_burgers():
    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="burgardatabase"
    )
    
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM burgers")
    burgers = cursor.fetchall()
    cursor.close()
    db_connection.close()
    
    return burgers
