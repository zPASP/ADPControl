import database_config as config
import mysql.connector

cnx = mysql.connector.connect(**config.DB_CONFIG)

# cnx = mysql.connector.connect(user=f"{config.DB_CONFIG['user']}", 
#                               password=f"{config.DB_CONFIG['password']}",
#                               host=f"{config.DB_CONFIG['host']}",
#                               database=f"{config.DB_CONFIG['database']}")


cursor = cnx.cursor()

# query = "SELECT * FROM funcionario"
# cursor.execute(query)

# for (id, nome, idade, cargo) in cursor:
#   print(id, nome, idade, cargo)

fechar =  cursor.close()