import mysql.connector

def conectar():
    conexao = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='Brauninha29',
        database='pizzas'
    )
    return conexao

def inserirPizzas():
    conexao = conectar()
    meucursor = conexao.cursor()
    nome = input('Qual o nome da pizza? ')
    id = int(input('Qual o id do sabor? '))
    descricao = input('Quais são os ingredientes? ')
    sql = 'INSERT INTO pizzas (nome, id_sabor, descricao) VALUES (%s, %s, %s)'
    val = (nome, id, descricao,)
    meucursor.execute(sql, val)
    conexao.commit()
    print(meucursor.rowcount, 'dado foi inserido.')
    meucursor.close()
    conexao.close()

def inserirSabores():
    conexao = conectar()
    meucursor = conexao.cursor()
    nome = input('Qual o nome do sabor da pizza? ')
    preco = int(input('Qual o preço? '))
    tamanho = input('Qual o id do tamanho da pizza? ')
    sql = 'INSERT INTO sabores (nome, preco, id_tamanho) VALUES (%s, %s, %s)'
    val = (nome, preco, tamanho)
    meucursor.execute(sql, val)
    conexao.commit()
    print(meucursor.rowcount, 'dado foi inserido.')
    meucursor.close()
    conexao.close()

def inserirTamanhos():
    conexao = conectar()
    meucursor = conexao.cursor()
    nome = input('Qual o tamanho da Pizza? ')
    sql = 'INSERT INTO tamanhos (nome) VALUES (%s)'
    val = (nome,)
    meucursor.execute(sql, val)
    conexao.commit()
    print(meucursor.rowcount, 'dado foi inserido.')
    meucursor.close()
    conexao.close()

def listarPizzas():
    conexao = conectar()
    print('Lista de Pizzas')
    meucursor = conexao.cursor()
    sql = 'SELECT p.id, p.nome as pizza, p.id_sabor, s.nome AS sabor, p.descricao FROM pizzas p JOIN sabores s ON p.id_sabor = s.id'
    meucursor.execute(sql)
    pizzas = meucursor.fetchall()
    print(f'{"id":12}{"nome":10}{"id_sabor":14}{"sabor":20}{"descrição":0}')
    for id, nome, id_sabor, nome, descricao in pizzas:
        print(id,'\t', nome,'\t', id_sabor,'\t', nome, '\t', descricao)
    meucursor.close()
    conexao.close()

def listarSabores():
    conexao = conectar()
    print('Lista de Sabores')
    meucursor = conexao.cursor()
    meucursor.execute('SELECT s.id, s.nome AS sabor, s.preco, t.nome AS tamanho FROM sabores s JOIN tamanhos t ON s.id_tamanho = t.id')
    sabores = meucursor.fetchall()
    print(f'{"id":12}{"nome":12}{"preço":9}{"tamanho":0}')
    for id, nome, preco, tamanho in sabores:
        print(id,'\t', nome,'\t', preco,'\t', tamanho)
    meucursor.close()
    conexao.close()

def listarTamanhos():
    conexao = conectar()
    print('Lista de Tamanhos')
    meucursor = conexao.cursor()
    meucursor.execute('SELECT * FROM tamanhos')
    tamanhos = meucursor.fetchall()
    print(f'{"id":10}{"Nome":0}')
    for id, nome in tamanhos:
        print(id,'\t',nome)
    meucursor.close()
    conexao.close()

def alterar():
    conexao = conectar()
    listarPizzas()
    meucursor = conexao.cursor()
    id = int(input('Qual id você quer alterar? '))
    nome = input('Qual o novo nome da pizza? ')
    sql = 'UPDATE pizzas SET nome = %s where id = %s'
    val = (nome, id)
    meucursor.execute(sql, val)
    conexao.commit()
    print(meucursor.rowcount, 'dado foi alterado.')
    meucursor.close()
    conexao.close()

def deletar():
    conexao = conectar()
    listarPizzas()
    meucursor = conexao.cursor()
    deletar = int(input('Qual id você quer apagar? '))
    sql = 'DELETE FROM pizzas WHERE id = %s'
    val = (deletar,)
    meucursor.execute(sql, val)
    conexao.commit()
    print(meucursor.rowcount, 'dado foi deletado.')
    meucursor.close()
    conexao.close()

def pesquisar():
    conexao = conectar()
    meucursor = conexao.cursor()
    pesquisar = input('Qual o nome de pizza você deseja pesquisar? ')
    sql = 'SELECT * FROM pizzas WHERE nome = %s'
    val = (pesquisar,)
    meucursor.execute(sql, val)
    pizzas = meucursor.fetchall()
    print(f'{"id":14}{"nome":16}{"id_sabor":20}{"descrição":0}')
    for id, nome, id_sabor, descricao in pizzas:
        print(id,'\t', nome,'\t', id_sabor,'\t', descricao)
    meucursor.close()
    conexao.close()

while True:
    print(' ')
    print('1.Inserir Pizzas')
    print('2.Inserir Sabores')
    print('3.Inserir Tamanhos')
    print('4.Listar Pizzas')
    print('5.Listar Sabores')
    print('6.Listar Tamanhos')
    print('7.Alterar')
    print('8.Deletar')
    print('9.Pesquisar')
    print('10.Sair')
    print(' ')
    opcao = int(input('Qual das opções você deseja? '))
    if opcao == 1:
        inserirPizzas()
    elif opcao == 2:
        inserirSabores()
    elif opcao == 3:
        inserirTamanhos()
    elif opcao == 4:
        listarPizzas()
    elif opcao == 5:
        listarSabores()
    elif opcao == 6:
        listarTamanhos()
    elif opcao == 7:
        alterar()
    elif opcao == 8:
        deletar()
    elif opcao == 9:
        pesquisar()
    elif opcao == 10: 
        print('Sair')
        break 
    else:
        print('Opção inválida')
    