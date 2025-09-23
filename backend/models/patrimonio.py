class Patrimonio:
    def __init__(self, id=None, codigo_tombamento=None, descricao=None,
                 categoria_id=None, numero_serie=None, data_aquisicao=None,
                 valor_aquisicao=None, nota_fiscal_item_id=None,
                 centro_custo_id=None, setor_atual_id=None, local_atual_id=None,
                 status=None, observacoes=None):
        self.id = id
        self.codigo_tombamento = codigo_tombamento
        self.descricao = descricao
        self.categoria_id = categoria_id
        self.numero_serie = numero_serie
        self.data_aquisicao = data_aquisicao
        self.valor_aquisicao = valor_aquisicao
        self.nota_fiscal_item_id = nota_fiscal_item_id
        self.centro_custo_id = centro_custo_id
        self.setor_atual_id = setor_atual_id
        self.local_atual_id = local_atual_id
        self.status = status
        self.observacoes = observacoes
