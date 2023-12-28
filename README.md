# Aplicação de Lista de Tarefas (ToDo List)

## Visão Geral

Esta aplicação em Python é um simples gerenciador de lista de tarefas (ToDo list) que utiliza o SQLite como banco de dados de backend. A aplicação permite que os usuários realizem operações básicas de CRUD (Create, Read, Update, Delete) tanto em categorias quanto em atividades.

## Recursos

- **Criar Categoria:** Os usuários podem criar novas categorias para organizar suas atividades.
- **Listar Categorias:** Visualizar uma lista de todas as categorias existentes.
- **Atualizar Categoria:** Modificar o nome de uma categoria existente.
- **Excluir Categoria:** Remover uma categoria juntamente com suas atividades associadas.
- **Criar Atividade:** Adicionar novas atividades com nome, descrição, data de vencimento e associação a uma categoria específica.
- **Atualizar Atividade:** Modificar os detalhes de uma atividade existente.
- **Excluir Atividade:** Remover uma atividade da lista.
- **Listar Atividades:** Visualizar uma lista de atividades juntamente com seus detalhes e status.
- **Marcar Atividade como Executada:** Marcar uma atividade como executada, alterando seu status para "Tarefa Executada".

## Uso

1. **Criar Categoria**
   - Escolha a opção 1 e insira o nome da categoria quando solicitado.

2. **Listar Categorias**
   - Escolha a opção 2 para visualizar uma lista de categorias existentes.

3. **Atualizar Categoria**
   - Escolha a opção 3, selecione a categoria a ser atualizada pelo seu ID e insira o novo nome.

4. **Excluir Categoria**
   - Escolha a opção 4, selecione a categoria a ser excluída pelo seu ID.

5. **Criar Atividade**
   - Escolha a opção 5 e insira os detalhes da nova atividade, incluindo nome, descrição, data de vencimento e o ID da categoria associada.

6. **Atualizar Atividade**
   - Escolha a opção 6, selecione a atividade a ser atualizada pelo seu ID e insira os novos detalhes.

7. **Excluir Atividade**
   - Escolha a opção 7, selecione a atividade a ser excluída pelo seu ID.

8. **Listar Atividades**
   - Escolha a opção 8 para visualizar uma lista de atividades. Forneça a data de vencimento para filtrar a lista.

9. **Marcar Atividade como Executada**
   - Escolha a opção 9, insira a data de vencimento para visualizar uma lista de atividades e, em seguida, selecione a atividade a ser marcada como executada.

10. **Sair**
    - Escolha a opção 0 para sair da aplicação.

## Observação

Esta aplicação é um gerenciador de lista de tarefas baseado em console e fornece uma interface simples para gerenciar categorias e atividades. O código utiliza o SQLite para armazenamento de dados, garantindo que sua lista de tarefas seja persistente entre as sessões.

##**Telas**
**Menu inicial**

![image](https://github.com/Coriolando-Medeiros/ToDo/assets/107105546/5ea85ac8-022e-4913-92f5-800365752dff)

**Lista de categorias adicionadas**

![image](https://github.com/Coriolando-Medeiros/ToDo/assets/107105546/11598e14-60de-4ea7-8b2d-69acd142ffdd)

