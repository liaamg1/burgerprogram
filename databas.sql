# Databasen som används i projektet
# Vi kommer behöva koppla denna databas till vårt projekt till main filen
# Vi kan också använda oss av json filer för att spara data istället för en SQL databas
import mysql.connector

db_connection = mysql.connector.connect(
    host="localhost", # databasen ligger på localhost
    user="root" # användarnamn
    password="root" # lösenord
    database="burgardatabase" # databasens namn
)

cursor = db_connection.cursor()

cursor.execute(
    
)# SQL kommando för att skapa en tabell
