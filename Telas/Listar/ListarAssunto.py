from ..TelaBase import TelaBase


class ListarAssunto(TelaBase):
    def mostrar(self):
        from Dao.AssuntoDao import AssuntoDao
        from Dao.DisciplinaDao import DisciplinaDao

        self.cls()
        self.verde().bold().print('Listagem de assunto')

        print('Índice\tDisciplina')

        for disciplina in DisciplinaDao.listar():
            print(str(disciplina.id) + '\t' + disciplina.nome)

        print('\nPara voltar digite -1\n')
        indice = input('Selecione a disciplina desejada por índice: ')

        if indice == '-1':
            return not self.manter_na_tela

        if not indice.isnumeric():
            input('Deve ser um número.')
            return self.manter_na_tela

        try:
            nome_disciplina = DisciplinaDao.retornar_por_id(indice).nome
        except (ValueError, Exception):
            self.cls()
            input('Disciplina não foi encontrado. Tente novamente.')
            return self.manter_na_tela

        lista_de_assuntos = AssuntoDao.listar(indice)

        if len(lista_de_assuntos) == 0:
            self.cls()
            input('Não há nenhum assunto criado na disciplina ' + nome_disciplina)
        else:
            self.cls()
            print('Indices\tAssuntos')
            for assunto in lista_de_assuntos:
                print(str(assunto.id) + '\t' + assunto.nome)
            input('')

        return self.manter_na_tela
