class Fornecedor:
    def __init__(self, id=None, razao_social=None, cnpj=None, ie=None,
                 contato=None, telefone=None, email=None):
        self.id = id
        self.razao_social = razao_social
        self.cnpj = cnpj
        self.ie = ie
        self.contato = contato
        self.telefone = telefone
        self.email = email
