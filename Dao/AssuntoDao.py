from BancoDeDados.config_database import Disciplina, Assunto


class AssuntoDao:
    @staticmethod
    def listar(id_disciplina):
        return Assunto.select().where(id_disciplina == Assunto.id_disciplina)

    @staticmethod
    def retornar_por_id(indice_disciplina, indice_assunto):
        return Assunto\
            .select()\
            .where(
                Assunto.id_disciplina == indice_disciplina,
                Assunto.id == indice_assunto
            )\
            .get()

    @staticmethod
    def inserir_um(id_disciplina, nome):
        try:
            Assunto.create(id_disciplina=id_disciplina, nome=nome)
            input('Assunto registrado com sucesso.')
            return True
        except (ValueError, Exception):
            input('Já existe um assunto com esse nome.')
            return False
