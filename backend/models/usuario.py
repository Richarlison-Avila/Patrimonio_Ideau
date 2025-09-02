from backend.database import Database

class Usuario:
    def __init__(self, id_usuario=None, nome=None, email=None, senha=None, tipo="comum"):
        self.id_usuario = id_usuario
        self.nome = nome
        self.email = email
        self.senha = senha
        self.tipo = tipo  # "master" ou "comum"

    def salvar(self):
        db = Database()
        if self.id_usuario is None:
            # Inserir novo usuário
            query = """
            INSERT INTO usuarios (nome, email, senha, tipo_usuario)
            VALUES (%s, %s, %s, %s)
            """
            params = (self.nome, self.email, self.senha, self.tipo)
            self.id_usuario = db.executar_query(query, params)
        else:
            # Atualizar usuário existente
            query = """
            UPDATE usuarios SET nome=%s, email=%s, senha=%s, tipo_usuario=%s
            WHERE id_usuario=%s
            """
            params = (self.nome, self.email, self.senha, self.tipo, self.id_usuario)
            db.executar_query(query, params)

    @staticmethod
    def buscar_todos():
        db = Database()
        query = "SELECT * FROM usuarios"
        return db.buscar_query(query)

    @staticmethod
    def buscar_por_email(email):
        db = Database()
        query = "SELECT * FROM usuarios WHERE email=%s"
        result = db.buscar_query(query, (email,))
        return result[0] if result else None
