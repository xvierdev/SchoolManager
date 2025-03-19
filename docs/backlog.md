# Backlog do Projeto: Sistema de Gerenciamento Escolar Web Local para Professores

**Visão Geral:**

Um sistema web local desenvolvido em Flask com banco de dados SQLite, rodando em um servidor Linux, para auxiliar professores na organização de turmas, alunos, horários, chamadas e geração de planilhas de frequência.

**Requisitos:**

## A Fazer:

| ID | Descrição | Prioridade | Esforço (Pontos) | Critérios de Aceitação | Categoria | Responsável |
|---|---|---|---|---|---|---|
| 1 | Configuração do ambiente de desenvolvimento (Flask, SQLite, Linux). | Alta | 3 | Ambiente de desenvolvimento configurado e pronto para uso. | Infraestrutura | [Nome] |
| 2 | Criação do banco de dados SQLite com tabelas para turmas, alunos, horários e chamadas. | Alta | 5 | Banco de dados criado com tabelas e relacionamentos adequados. | Banco de Dados | [Nome] |
| 3 | Implementação da funcionalidade de cadastro de turmas (nome do curso, professor, horário, duração total, duração da aula, lista de alunos). | Alta | 8 | Turmas podem ser cadastradas com todos os dados especificados. | Funcionalidade | [Nome] |
| 4 | Implementação da funcionalidade de cadastro de alunos (nome, telefone, data de início, vínculo com turma). | Alta | 5 | Alunos podem ser cadastrados com todos os dados especificados. | Funcionalidade | [Nome] |
| 5 | Implementação da funcionalidade de criação automática de horários (com base em dados da turma). | Alta | 8 | Horários semanais são gerados automaticamente e exibidos em formato de grade. | Funcionalidade | [Nome] |
| 6 | Implementação do sistema de chamada online (registro de presença/ausência, histórico, edição). | Alta | 10 | Chamadas podem ser registradas, visualizadas e editadas. | Funcionalidade | [Nome] |
| 7 | Implementação da funcionalidade de geração de planilhas de frequência (CSV ou Excel). | Alta | 8 | Planilhas são geradas com dados corretos e podem ser baixadas. | Funcionalidade | [Nome] |
| 8 | Desenvolvimento da interface web Flask (rotas, templates, design responsivo). | Alta | 10 | Interface web intuitiva, responsiva e fácil de usar. | Interface | [Nome] |
| 9 | Implementação da funcionalidade de backup e restauração do banco de dados. | Média | 5 | O professor pode salvar o banco de dados e restaurar. | Melhoria | [Nome] |
| 10 | Testes unitários e de integração das funcionalidades. | Alta | 5 | Todas as funcionalidades são testadas e funcionam corretamente. | Testes | [Nome] |
| 11 | Documentação do sistema (instalação, uso, etc.). | Média | 3 | Documentação completa e clara do sistema. | Documentação | [Nome] |

## Concluídos:

*Nenhum item concluído até o momento.*

## Melhorias Adicionais:

* Adicionar funcionalidade de pesquisa de alunos e turmas.
* Implementar um sistema de notificações para lembrar o professor das chamadas.
* Criar um dashboard com estatísticas sobre as turmas e alunos.

## Detalhamento e Priorização:

* **Prioridades:**
    * **Alta:** Tarefas essenciais para o funcionamento básico do sistema.
    * **Média:** Melhorias e funcionalidades adicionais.
* **Esforço:** Estimativa de pontos para cada tarefa, representando a complexidade e o tempo necessário.
* **Critérios de Aceitação:** Condições para que uma tarefa seja considerada concluída.
* **Observações:**
    * Preencher a coluna "Responsável" com os nomes dos membros da equipe.
    * O backlog está sujeito a alterações e atualizações conforme o projeto avança.