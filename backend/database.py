import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",       
                user="root",            
                password="sua_senha",   
                database="patrimonios_ideau"
            )
            if self.connection.is_connected():
                print("✅ Conexão com MySQL estabelecida com sucesso!")
        except Error as e:
            print(f"❌ Erro ao conectar no MySQL: {e}")

    def executar_query(self, query, params=None):
        """Executa INSERT, UPDATE ou DELETE"""
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        self.connection.commit()
        return cursor.lastrowid

    def buscar_query(self, query, params=None):
        """Executa SELECT e retorna os resultados"""
        cursor = self.connection.cursor(dictionary=True)
        cursor.execute(query, params)
        return cursor.fetchall()
