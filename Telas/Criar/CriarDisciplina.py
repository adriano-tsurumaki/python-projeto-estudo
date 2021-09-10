from ..TelaBase import TelaBase


class CriarDisciplina(TelaBase):
    def mostrar(self):
        from Dao.DisciplinaDao import DisciplinaDao
        from ..Listar.ListarDisciplina import ListarDisciplina

        self.cls()
        self.azul().bold().print('Criar disciplina')
        print('\nPara voltar digite -1')
        print('Para listar digite 0\n')
        nome = input('Disciplina: ')

        if nome == '-1':
            return not self.manter_na_tela

        if nome.isnumeric() and nome == '0':
            self.janela(ListarDisciplina().mostrar)
            return self.manter_na_tela

        if len(nome) == 0:
            input('Não é aceitado vazio.')
            return self.manter_na_tela

        confirmar = input(nome + ' será criado.\nConfirmar? [Y/N]\n')

        if confirmar.lower() != 'y':
            return self.manter_na_tela

        DisciplinaDao.inserir_um(nome)
        return self.manter_na_tela
