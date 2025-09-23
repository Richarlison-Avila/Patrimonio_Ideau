class DepreciacaoLancamento:
    def __init__(self, id=None, patrimonio_id=None, competencia=None,
                 valor=None, acumulado=None, criado_em=None):
        self.id = id
        self.patrimonio_id = patrimonio_id
        self.competencia = competencia
        self.valor = valor
        self.acumulado = acumulado
        self.criado_em = criado_em