import os
from src.manager import TaskManager

ARQUIVO_TESTE = "test_tasks.json"


def setup_function():
    # Limpa o arquivo antes de cada teste
    if os.path.exists(ARQUIVO_TESTE):
        os.remove(ARQUIVO_TESTE)


def test_adicionar_tarefa():
    manager = TaskManager(ARQUIVO_TESTE)
    manager.adicionar_tarefa("Dar remédio", "08:00")

    assert len(manager.tasks) == 1
    assert manager.tasks[0].descricao == "Dar remédio"
    assert manager.tasks[0].concluida is False


def test_concluir_tarefa():
    manager = TaskManager(ARQUIVO_TESTE)
    manager.adicionar_tarefa("Dar remédio", "08:00")

    manager.concluir_tarefa(1)

    assert manager.tasks[0].concluida is True


def test_tarefa_inexistente():
    manager = TaskManager(ARQUIVO_TESTE)

    manager.concluir_tarefa(99)

    assert len(manager.tasks) == 0