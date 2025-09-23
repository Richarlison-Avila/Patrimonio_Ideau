class Movimentacao:
    def __init__(self, id=None, patrimonio_id=None, de_setor_id=None,
                 de_local_id=None, para_setor_id=None, para_local_id=None,
                 motivo=None, usuario_id=None, criado_em=None):
        self.id = id
        self.patrimonio_id = patrimonio_id
        self.de_setor_id = de_setor_id
        self.de_local_id = de_local_id
        self.para_setor_id = para_setor_id
        self.para_local_id = para_local_id
        self.motivo = motivo
        self.usuario_id = usuario_id
        self.criado_em = criado_em
