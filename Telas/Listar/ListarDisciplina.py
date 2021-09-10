from ..TelaBase import TelaBase


class ListarDisciplina(TelaBase):
    def mostrar(self):
        from Dao.DisciplinaDao import DisciplinaDao

        self.cls()
        self.azul().bold().print('Listagem de disciplina')
        lista_de_disciplinas = DisciplinaDao.listar()
        if len(lista_de_disciplinas) == 0:
            print('Não há nenhuma disciplina criada.')
        else:
            print('Índice\tDisciplina')
            for disciplina in lista_de_disciplinas:
                print(str(disciplina.id) + '\t' + disciplina.nome)

        input('Pressione qualquer botão para sair')
        return not self.manter_na_tela

