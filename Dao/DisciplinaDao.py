from BancoDeDados.config_database import Disciplina


class DisciplinaDao:
    @staticmethod
    def listar():
        return Disciplina.select()

    @staticmethod
    def retornar_por_id(id_disciplina):
        return Disciplina.get(Disciplina.id == id_disciplina)

    @staticmethod
    def retornar_por_nome(nome):
        return Disciplina.get(Disciplina.nome == nome)

    @staticmethod
    def inserir_um(nome):
        try:
            Disciplina.create(nome=nome)
            input('Disciplina registrado com sucesso.')
            return True
        except (ValueError, Exception):
            input('Já existe uma disciplina com esse nome.')
            return False
