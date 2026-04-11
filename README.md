# Caregiver Task Manager

## Descrição do Projeto

O **Caregiver Task Manager** é uma aplicação em linha de comando (CLI) desenvolvida para auxiliar cuidadores na organização de tarefas diárias essenciais, como administração de medicamentos, alimentação e cuidados gerais.

O sistema foi criado com foco em simplicidade, praticidade e redução da sobrecarga mental enfrentada por cuidadores.


## Problema

Cuidadores frequentemente lidam com múltiplas responsabilidades simultâneas, o que pode levar a:

* esquecimento de tarefas importantes
* dificuldade de organização da rotina
* sobrecarga mental
* falhas no acompanhamento de atividades críticas


## Solução

A aplicação permite registrar e acompanhar tarefas de forma simples, garantindo maior controle sobre a rotina.


## Público-alvo

* cuidadores informais (familiares)
* profissionais da área de saúde
* pessoas responsáveis por idosos ou pacientes


## Funcionalidades

* Adicionar tarefas
* Listar tarefas
* Marcar tarefa como concluída
* Persistência de dados em arquivo JSON


## Tecnologias utilizadas

* Python
* JSON (armazenamento de dados)
* pytest (testes automatizados)


## Instalação

Clone o repositório:

```bash
git clone https://github.com/giovannadsr/caregiver-task-manager.git
cd caregiver-task-manager
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Como executar

### Adicionar tarefa

```bash
python src/main.py adicionar "Dar remédio" 08:00
```

### Listar tarefas

```bash
python src/main.py listar
```

### Concluir tarefa

```bash
python src/main.py concluir 1
```

## Testes

```bash
pytest
```


## Estrutura do Projeto

```
caregiver-task-manager/
├── src/
│   ├── main.py
│   ├── manager.py
│   └── task.py
├── tests/
│   └── test_tasks.py
├── .github/workflows/
│   └── ci.yml
├── README.md
├── requirements.txt
├── VERSION
```


## Versionamento

Versão atual: **1.0.0**

Este projeto segue o padrão de versionamento semântico:

* MAJOR: mudanças grandes
* MINOR: novas funcionalidades
* PATCH: correções


## Autora

Giovanna Rodrigues


## Repositório

https://github.com/giovannadsr/caregiver-task-manager

