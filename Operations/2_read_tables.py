import psycopg2  #? A python driver for postgreSQL
from dotenv import load_dotenv  #? A function to load .env files
import os  #? To interact with the OS and its functionalities


env_path = 'D:/Coding-Applications/VS Code/VSC Code files/AWS-postgreSQL/.env'  #? specify the 'absolute-path' where the .env files are located
load_dotenv(dotenv_path=env_path)  #? Load environment variables from .env file (the env variables will be made available in this file)

hostname = os.getenv('HOSTNAME1')  #? pls use 'HOSTNAME1', bcoz HOSTNAME env variable will hold your device-name, change the same in .env file
port = os.getenv('PORT')
username = os.getenv('USERNAME1')  #? pls use 'USERNAME1', bcoz USERNAME env variable will hold your user-name, change the same in .env file
password = os.getenv('PASSWORD')
database = os.getenv('DATABASE')

try:
    connection = psycopg2.connect(
        host=hostname,
        port=port,
        user=username,
        password=password,
        dbname=database
    )
    print('Successfully connected to the database')
except Exception as e:
    print('Can\'t connect to the database')
    print(e)


#? perform read operations on the database
def list_tables(connection):
    cursor = connection.cursor()
    read_query = f""" SELECT table_name FROM information_schema.tables
                    WHERE table_schema = 'public' """
    cursor.execute(read_query)
    tables = cursor.fetchall()

    print("Tables in the database: ")

    for table in tables:
        print(table)

#? Call function here
list_tables(connection)

#! Please close the connection:
connection.close()