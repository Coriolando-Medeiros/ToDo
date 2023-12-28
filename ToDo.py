import sqlite3

def conecta_bd():
    conexao = sqlite3.connect('ToDo.sqlite3')
    cursor = conexao.cursor()
    return conexao, cursor

def criar_tabelas():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS categorias (
            id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT (100)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS atividades (
            id_atividade INTEGER PRIMARY KEY,
            nome TEXT (100),
            descricao TEXT,
            data TEXT,
            id_categoria INTEGER,
            executada INTEGER DEFAULT 0,
            FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria) ON DELETE CASCADE
        )
    ''')


def criar_categoria(nome):
    sql = '''INSERT INTO categorias(nome) VALUES (?)'''
    cursor.execute(sql, (nome,))
    conexao.commit()

def atualizar_categoria(id_categoria, nome):
    sql = '''UPDATE categorias SET nome = ? WHERE id_categoria = ?'''
    cursor.execute(sql, (nome, id_categoria))
    conexao.commit()

def excluir_categoria(id_categoria):
    sql = '''DELETE FROM categorias WHERE id_categoria = ?'''
    cursor.execute(sql, (id_categoria,))
    conexao.commit()

def criar_atividade(nome, descricao, data, id_categoria):
    sql = '''INSERT INTO atividades (nome, descricao, data, id_categoria) VALUES (?, ?, ?, ?)'''
    cursor.execute(sql, (nome, descricao, data, id_categoria))
    conexao.commit()

def atualizar_atividade(id_atividade, nome, descricao, data, id_categoria):
    sql = '''UPDATE atividades SET nome = ?, descricao = ?, data = ?, id_categoria = ? WHERE id_atividade = ?'''
    cursor.execute(sql, (nome, descricao, data, id_categoria, id_atividade))
    conexao.commit()

def excluir_atividade(id_atividade):
    sql = '''DELETE FROM atividades WHERE id_atividade = ?'''
    cursor.execute(sql, (id_atividade,))
    conexao.commit()

def consultar_atividades():
    sql = '''SELECT * FROM atividades'''
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        if row[5] == 1:
            status = 'Tarefa Executada'
        else:
            status = 'A Fazer'
        print(f'ID: {row[0]} - Nome: {row[1]} - Descrição: {row[2]} - Data: {row[3]} - Categoria ID: {row[4]} - Status: {status}')
    conexao.commit()
def listar_atividades(data):
    sql = '''SELECT * FROM atividades WHERE data = ?'''
    cursor.execute(sql, (data,))
    rows = cursor.fetchall()
    for row in rows:
        if row[5] == 1:
            status = 'Tarefa Executada'
        else:
            status = 'A Fazer'
        print(f'ID: {row[0]} - Nome: {row[1]} - Descrição: {row[2]} - Data: {row[3]} - Categoria ID: {row[4]} - Status: {status}')
    conexao.commit()

def listar_categorias():
    sql = '''SELECT * FROM categorias'''
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print(f'ID Categoria: {row[0]} - Nome: {row[1]}')
    conexao.commit()
    
def marcar_atividade_executada(id_atividade, data):
    sql = '''UPDATE atividades SET executada = 1 WHERE id_atividade = ?'''
    cursor.execute(sql, (id_atividade,))
    conexao.commit()
    listar_atividades(data)


if __name__ == "__main__":
    conexao, cursor = conecta_bd()
    criar_tabelas()

    while True:
        print('\n ------------------------ToDo List -------------------------')
        print('| 1 - Criar categoria                                       |')
        print('| 2 - Listar categorias                                     |')
        print('| 3 - Atualizar categoria                                   |')
        print('| 4 - Excluir categoria                                     |')
        print('| 5 - Criar atividade                                       |')
        print('| 6 - Atualizar atividade                                   |')
        print('| 7 - Excluir atividade                                     |')
        print('| 8 - Listar atividades                                     |')
        print('| 9 - Marcar atividade como executada                       |')
        print('| 0 - Sair                                                  |')
        print(' -----------------------------------------------------------')

        opcao = input('Opção: ')

        if opcao == '1':
            nome = input('Informe o nome da categoria: ')
            criar_categoria(nome)
            

        elif opcao == '2':
            print('-----------------------------------------------------------------------------------------------------------------------------')
            listar_categorias()
            print('-----------------------------------------------------------------------------------------------------------------------------')
            aguarda = input('Digite qualquer tecla: ') #Entrada usada para uma experiência melhor de visualização dos dados

        elif opcao == '3':
            print('-----------------------------------------------------------------------------------------------------------------------------')
            listar_categorias()
            print('-----------------------------------------------------------------------------------------------------------------------------')
            id_categoria = int(input('Digite o ID da categoria a ser atualizada: '))
            nome = input('Novo nome: ')
            atualizar_categoria(id_categoria, nome)

        elif opcao == '4':
            print('-----------------------------------------------------------------------------------------------------------------------------')
            listar_categorias()
            print('-----------------------------------------------------------------------------------------------------------------------------')
            id_categoria = int(input('Digite o ID da categoria para excluir: '))
            excluir_categoria(id_categoria)

        elif opcao == '5':
            nome = input('Nome da atividade: ')
            descricao = input('Descrição da atividade: ')
            data = input('Data da atividade: ')
            print('-----------------------------------------------------------------------------------------------------------------------------')
            listar_categorias()
            print('-----------------------------------------------------------------------------------------------------------------------------')
            id_categoria = int(input('ID da Categoria da atividade: '))
            criar_atividade(nome, descricao, data, id_categoria)

        elif opcao == '6':
            consultar_atividades()
            id_atividade = int(input('ID da atividade a ser alterada: '))
            nome = input('Nome da nova atividade: ')
            descricao = input('Nova descrição: ')
            data = input('Nova data: ')
            id_categoria = int(input('Novo ID da Categoria da atividade '))
            atualizar_atividade(id_atividade, nome, descricao, data, id_categoria)

        elif opcao == '7':
            print('-----------------------------------------------------------------------------------------------------------------------------')
            listar_atividades(data)
            print('-----------------------------------------------------------------------------------------------------------------------------')
            id_atividade = int(input('ID da atividade a ser removida: '))
            excluir_atividade(id_atividade)

        elif opcao == '8':
            data = input('Digite a data a consultar: ')
            print('-----------------------------------------------------------------------------------------------------------------------------')
            listar_atividades(data)
            print('-----------------------------------------------------------------------------------------------------------------------------')
            aguarda = input('Digite qualquer tecla: ') #Entrada usada para uma experiência melhor de visualização dos dados
        
        elif opcao == '9':
            data = input('Data da atividade: ')
            print('-----------------------------------------------------------------------------------------------------------------------------')
            listar_atividades(data)
            print('-----------------------------------------------------------------------------------------------------------------------------')
            id_atividade = int(input('ID da atividade a ser marcada como executada: '))
            marcar_atividade_executada(id_atividade, data)

        elif opcao == '0':
            conexao.close()
            break

        else:
            print('Opção inválida!')
