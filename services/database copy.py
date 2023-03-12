import sys
import os
# Adiciona o diretório atual ao sys.path
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path)

import database_config as config
import mysql.connector
from mysql.connector import Error

cnx = mysql.connector.connect(**config.DB_CONFIG)

# cnx = mysql.connector.connect(user=f"{config.DB_CONFIG['user']}", 
#                               password=f"{config.DB_CONFIG['password']}",
#                               host=f"{config.DB_CONFIG['host']}",
#                               database=f"{config.DB_CONFIG['database']}")
cursor = cnx.cursor()

def get_cursor():
    return cursor

def close_connection():
    cursor.close()
    cnx.close()


# query = "SELECT * FROM funcionario"
# cursor.execute(query)

# for (id, nome, idade, cargo) in cursor:
#   print(id, nome, idade, cargo)

#fechar =  cursor.close()