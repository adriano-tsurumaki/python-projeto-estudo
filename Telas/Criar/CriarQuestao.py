from ..TelaBase import TelaBase


class CriarQuestao(TelaBase):
    indice_disciplina = ''
    nome_disciplina = ''
    indice_assunto = ''
    nome_assunto = ''

    def validar_selecao(self):
        if self.nome_disciplina == '' or self.nome_disciplina is None:
            input('\nDisciplina não selecionado')
            return not self.manter_na_tela

        if self.nome_assunto == '' or self.nome_assunto is None:
            input('\nAssunto não selecionado')
            return not self.manter_na_tela

        return self.manter_na_tela

    def parte_disciplina(self):
        from Dao.DisciplinaDao import DisciplinaDao

        self.cls()
        self.amarelo().bold().print('Selecione uma disciplina')

        lista_de_disciplinas = DisciplinaDao.listar()

        for disciplina in lista_de_disciplinas:
            print(str(disciplina.id) + '\t' + disciplina.nome)

        print('\nDigite -1 para sair\n')

        self.indice_disciplina = input('Seleciona uma disciplina pelo índice: ')

        if self.indice_disciplina == '-1':
            return not self.manter_na_tela

        if not self.indice_disciplina.isnumeric():
            input('Deve ser um número.')
            return self.manter_na_tela

        try:
            self.nome_disciplina = DisciplinaDao.retornar_por_id(self.indice_disciplina).nome
            return not self.manter_na_tela
        except (ValueError, Exception):
            self.cls()
            input('Disciplina não foi encontrado. Tente novamente.')
            return self.manter_na_tela

    def parte_assunto(self):
        from Dao.AssuntoDao import AssuntoDao

        self.cls()
        self.amarelo().bold().print('Selecione um assunto')

        if self.nome_disciplina == '' or self.nome_disciplina is None:
            input('\nDisciplina não selecionado')
            return not self.manter_na_tela

        lista_de_assuntos = AssuntoDao.listar(self.indice_disciplina)

        for assunto in lista_de_assuntos:
            print(str(assunto.id) + '\t' + assunto.nome)

        print('\nDigite -1 para sair\n')

        self.indice_assunto = input('Seleciona um assunto pelo índice: ')

        if self.indice_assunto == '-1':
            self.indice_assunto = None
            return not self.manter_na_tela

        if not self.indice_assunto.isnumeric():
            input('Deve ser um número.')
            return self.manter_na_tela

        try:
            self.nome_assunto = AssuntoDao.retornar_por_id(self.indice_disciplina, self.indice_assunto).nome
            return not self.manter_na_tela
        except (ValueError, Exception):
            self.cls()
            input('Assunto não foi encontrado. Tente novamente.')
            return self.manter_na_tela

    def parte_questao(self):
        if not self.validar_selecao():
            return not self.manter_na_tela

        from Dao.QuestaoDao import QuestaoDao

        quantidade_confirmar = QuestaoDao.retornar_quantidade(self.indice_assunto)
        if quantidade_confirmar > 0:
            texto_plural = 'Existem ' + str(QuestaoDao.retornar_quantidade(self.indice_assunto)) \
                           + ' questões registradas nesse assunto'
            texto_sing = 'Existe' + str(QuestaoDao.retornar_quantidade(self.indice_assunto)) \
                         + ' questão registrado nesse assunto'

            texto = (texto_plural if QuestaoDao.retornar_quantidade(self.indice_assunto) > 1 else texto_sing) \
                + ', deseja adicionar mais?[Y/N]\n'

            if not self.confirmar(texto):
                return not self.manter_na_tela

        self.cls()
        self.amarelo().bold().print('Inserir questões')

        print('\nDigite -1 para sair')
        quantidade = input('\nQuantas questões existem neste assunto?\n')

        if not quantidade.isnumeric():
            input('Deve ser um número.')
            return self.manter_na_tela

        confirmar = input('Confirmar a operação? [Y/N]')

        if confirmar.lower() != 'y':
            return self.manter_na_tela

        QuestaoDao.inserir(int(quantidade), self.indice_assunto)

    def parte_nota(self):
        from Utils.ValidarInput import ValidarInput

        self.cls()
        self.amarelo().bold().print('Inserir notas')

        if not self.validar_selecao():
            return not self.manter_na_tela

        print('\nDisciplina: ' + (self.nome_disciplina if self.nome_disciplina else 'Nenhum selecionado'))
        print('Índice: ' + str(self.indice_disciplina))
        print('\nAssunto: ' + (self.nome_assunto if self.nome_assunto else 'Nenhum selecionado'))
        print('Índice: ' + str(self.indice_assunto) + '\n')

        print('[0] - Voltar')
        print('[1] - Inserir em grupo\n')
        print('[2] - Inserir por unidade')

        escolha = input('Digite aqui: ')

        [mensagem, validado] = ValidarInput.validar_input_numerico(escolha, 0, 3)
        if not validado:
            input(mensagem)
            return self.manter_na_tela

        escolha = int(escolha)

        if escolha == 0:
            return not self.manter_na_tela

        from .CriarNota import CriarNota

        criar_nota = CriarNota(self.nome_disciplina, self.indice_assunto, self.nome_assunto)

        opcoes = {
            1: lambda: criar_nota.mostrar_grupo(),
            2: lambda: criar_nota.mostrar_unidade()
        }

        self.transitar_janela(opcoes, escolha)
        return self.manter_na_tela

    def mostrar(self):
        from Utils.ValidarInput import ValidarInput

        self.cls()
        self.amarelo().bold().print('Inserir questões')

        print('\nDisciplina: ' + (self.nome_disciplina if self.nome_disciplina else 'Nenhum selecionado'))
        print('Índice: ' + str(self.indice_disciplina))
        print('\nAssunto: ' + (self.nome_assunto if self.nome_assunto else 'Nenhum selecionado'))
        print('Índice: ' + str(self.indice_assunto) + '\n')

        print('[0] - Voltar')
        print('[1] - Disciplina')
        print('[2] - Assunto')
        print('[3] - Questao')
        print('[4] - Nota')

        escolha = input('Digite aqui: ')

        [mensagem, validado] = ValidarInput.validar_input_numerico(escolha, 0, 4)
        if not validado:
            input(mensagem)
            return self.manter_na_tela

        escolha = int(escolha)

        if escolha == 0:
            return not self.manter_na_tela

        opcoes = {
            1: lambda: self.parte_disciplina(),
            2: lambda: self.parte_assunto(),
            3: lambda: self.parte_questao(),
            4: lambda: self.parte_nota()
        }

        self.transitar_janela(opcoes, escolha)
        return self.manter_na_tela
