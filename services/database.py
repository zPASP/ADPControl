import sys
import os
# Adiciona o diretório atual ao sys.path
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path)

import database_config as config
import mysql.connector

class Database:
    def __init__(self):
        self.host = f"{config.DB_CONFIG['host']}"
        self.user = f"{config.DB_CONFIG['user']}"
        self.password = f"{config.DB_CONFIG['password']}"
        self.database = f"{config.DB_CONFIG['database']}"
        self.connection = None

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )

    def disconnect(self):
        if self.connection:
            self.connection.close()

    def execute_query(self, query, params=None):
        print('-EXECUTE QUERY-')
        self.connect()
        cursor = self.connection.cursor(dictionary=True)
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)

        self.connection.commit()

        #result = cursor.fetchall()
        result = last_id = cursor.lastrowid
        # print("last_id:", last_id)

        cursor.close()
        self.disconnect()
        return result, last_id
    
    def view_table(self, query, params=None):
        print('-VIEW TABLE QUERY-')
        self.connect()
        cursor = self.connection.cursor(dictionary=True)
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)

        # self.connection.commit()

        result = cursor.fetchall()
        last_id = cursor.lastrowid
        # print("last_id:", last_id)

        cursor.close()
        self.disconnect()
        return result, last_id
    
    def execute_query_one(self, query, params=None):
        print('-EXECUTE QUERY ONE-')
        self.connect()
        cursor = self.connection.cursor(dictionary=True)
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        
        result = cursor.fetchone()

        cursor.close()
        self.disconnect()
        return result 















# def connect(self):
#         self.connection = mysql.connector.connect(
#             **config.DB_CONFIG
#         )

# def disconnect(self):
#         if self.connection:
#             self.connection.close()




# cnx = mysql.connector.connect()

# # cnx = mysql.connector.connect(user=f"{config.DB_CONFIG['user']}", 
# #                               password=f"{config.DB_CONFIG['password']}",
# #                               host=f"{config.DB_CONFIG['host']}",
# #                               database=f"{config.DB_CONFIG['database']}")


# cursor = cnx.cursor()

# # query = "SELECT * FROM funcionario"
# # cursor.execute(query)

# # for (id, nome, idade, cargo) in cursor:
# #   print(id, nome, idade, cargo)

# #fechar =  cursor.close()