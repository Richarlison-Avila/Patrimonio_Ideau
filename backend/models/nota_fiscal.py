class NotaFiscal:
    def __init__(self, id=None, numero=None, serie=None, chave_acesso=None,
                 data_emissao=None, fornecedor_id=None, valor_total=None):
        self.id = id
        self.numero = numero
        self.serie = serie
        self.chave_acesso = chave_acesso
        self.data_emissao = data_emissao
        self.fornecedor_id = fornecedor_id
        self.valor_total = valor_total
