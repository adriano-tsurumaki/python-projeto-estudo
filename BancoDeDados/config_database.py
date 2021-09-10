from datetime import datetime
from peewee import (SqliteDatabase, Model, AutoField, TextField, ForeignKeyField, DateTimeField,
                    IntegerField, BooleanField)

DATABASE = SqliteDatabase(r'D:\Banco do Brasil\Python\Controle\Projeto\BancoDeDados\concurso.db')


class BaseModel(Model):
    class Meta:
        database = DATABASE


class Disciplina(BaseModel):
    id = AutoField()
    nome = TextField(unique=True)


class Assunto(BaseModel):
    id = AutoField()
    id_disciplina = ForeignKeyField(Disciplina, backref='Assuntos')
    nome = TextField(unique=True)


class Questao(BaseModel):
    id = AutoField()
    id_assunto = ForeignKeyField(Assunto, backref='Questoes')
    numero_questao = IntegerField()


class Nota(BaseModel):
    id = AutoField()
    id_questao = ForeignKeyField(Questao, backref='Notas')
    acerto = BooleanField()
    data = DateTimeField(default=datetime.now)


def start_config_db():
    tabelas = [
        Disciplina,
        Assunto,
        Questao,
        Nota
    ]
    DATABASE.connect()
    DATABASE.create_tables(tabelas)
    DATABASE.close()


if __name__ == '__main__':
    start_config_db()
