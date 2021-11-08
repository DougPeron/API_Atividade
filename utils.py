from models import Pessoas, db_session

#insere dados tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Peron',idade=30)
    print(pessoa)
    pessoa.save()

#consulta dados da tabela pessoa
def consulta_pessoas():
    pessoa = Pessoas.query.all()
    pessoa = Pessoas.query.filter_by(nome='Douglas').first()
    print(pessoa.idade)

#altera dados da tabela pessoa
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome= 'Douglas').first()
    pessoa.idade = 21
    pessoa.save()

#exclui dados da tabela pessoa
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Douglas').first()
    pessoa.delete()

if __name__ == '__main__':
    consulta_pessoas()
    altera_pessoa()
    insere_pessoas()