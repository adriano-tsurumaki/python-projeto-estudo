from ..TelaBase import TelaBase


class CriarAssunto(TelaBase):
    nome_disciplina = ''
    indice_disciplina = ''

    def mostrar(self):
        from Dao.DisciplinaDao import DisciplinaDao
        from .CriarDisciplina import CriarDisciplina

        self.cls()
        self.verde().bold().print('Criar assunto')

        lista_de_disciplinas = DisciplinaDao.listar()
        if len(lista_de_disciplinas) == 0:
            print('Não há nenhuma disciplina criada.')
            escolha = input('Deseja criar uma disciplina agora? [Y/N]\n')
            if escolha.lower() == 'y':
                self.janela(CriarDisciplina().mostrar)
                return self.manter_na_tela
            elif escolha.lower() == 'n':
                return not self.manter_na_tela
            else:
                input('Comando inválido. ')
                return self.manter_na_tela
        else:
            print('Índice\tDisciplina')
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
        except (ValueError, Exception):
            self.cls()
            input('Disciplina não foi encontrado. Tente novamente.')
            return self.manter_na_tela

        self.janela(self.mostrar_assunto)
        return self.manter_na_tela

    def mostrar_assunto(self):
        from Dao.AssuntoDao import AssuntoDao
        from ..Listar.ListarAssunto import ListarAssunto

        self.cls()
        self.verde().bold().print('Nome do assunto')
        print('\nDisciplina: ' + self.nome_disciplina)
        print('\nPara voltar digite -1')
        print('Para listar digite 0\n')

        nome = input('Digite o nome do assunto: ')

        if nome == '-1':
            return not self.manter_na_tela

        if nome == '0':
            self.janela(ListarAssunto().mostrar)

        if len(nome) == 0:
            input('Não é aceitado vazio.')
            return self.manter_na_tela

        confirmar = input(nome + ' será criado.\nConfirmar? [Y/N]\n')

        if confirmar.lower() != 'y':
            return self.manter_na_tela

        AssuntoDao.inserir_um(self.indice_disciplina, nome)
        return self.manter_na_tela
