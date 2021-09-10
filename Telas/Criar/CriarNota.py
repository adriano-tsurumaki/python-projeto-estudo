from ..TelaBase import TelaBase


class CriarNota(TelaBase):
    def __init__(self, nome_disciplina, indice_assunto, nome_assunto):
        from Dao.QuestaoDao import QuestaoDao
        self.nome_disciplina = nome_disciplina
        self.indice_assunto = indice_assunto
        self.nome_assunto = nome_assunto
        self.quantidade = QuestaoDao.retornar_quantidade(self.indice_assunto)

    def mostrar_unidade(self):
        self.cls()
        self.amarelo().bold().print('Criar nota por unidade')
        print('Disciplina: ' + self.nome_disciplina)
        print('Assunto: ' + self.nome_assunto)
        print('Quantidade de questões: ' + str(self.quantidade))
        input('')

    def mostrar_grupo(self):
        self.cls()
        self.amarelo().bold().print('Criar nota por grupo')
        print('\nDisciplina: ' + self.nome_disciplina)
        print('Assunto: ' + self.nome_assunto)
        print('Quantidade de questões: ' + str(self.quantidade))
        print('\nDigite -1 para sair\n')

        inicio = input('Digite a primeira questão: ')

        if inicio == '-1':
            return not self.manter_na_tela

        if not inicio.isnumeric():
            input('Deve ser um número')
            return self.manter_na_tela

        inicio = int(inicio)

        if inicio == '-1':
            return not self.manter_na_tela

        fim = input('Digite a última questão: ')
        if not fim.isnumeric():
            input('Deve ser um número')
            return self.manter_na_tela

        fim = int(fim)

        if fim > self.quantidade:
            input('O valor deve ser menor ou igual a quantidade de questões.')
            return self.manter_na_tela

        tipo_acerto = input('Classificar a faixa como acertos ou erros? [A/E]\n')

        if tipo_acerto.lower() not in ['a', 'e']:
            input('Comando inválido.')
            return self.manter_na_tela

        acertos = input('Quais questões você ' + ('acertou' if tipo_acerto.lower() == 'a' else 'errou') + '?\n')
        acertos = acertos.strip().split(',')

        self.cls()
        self.amarelo().bold().print('Criar nota por grupo')
        print('\nDisciplina: ' + self.nome_disciplina)
        print('Assunto: ' + self.nome_assunto)
        print('Quantidade de questões: ' + str(self.quantidade))
        print('\nInserir notas nas questões entre ' + str(inicio) + ' e ' + str(fim))

        if not self.confirmar("Confirmar? [Y/N]\n"):
            return self.manter_na_tela

        try:
            acertos = list(map(lambda x: int(x.strip()), acertos))
            for acerto in acertos:
                if acerto not in range(inicio, fim+1):
                    input('As questões acertadas devem estar entre ' + str(inicio) + ' e ' + str(fim))
                    return self.manter_na_tela
        except (ValueError, Exception):
            input('Deve ser um número')
            return self.manter_na_tela

        from Dao.NotaDao import NotaDao

        NotaDao.inserir_range(self.indice_assunto,
                              (True if tipo_acerto.lower() == 'a' else False),
                              acertos, inicio, fim)
