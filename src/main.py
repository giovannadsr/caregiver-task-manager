import sys
from src.manager import TaskManager
from src.weather import obter_clima

manager = TaskManager()

if len(sys.argv) < 2:
    print("Use: adicionar | listar | concluir")
    sys.exit()

comando = sys.argv[1]

if comando == "adicionar":
    descricao = sys.argv[2]
    horario = sys.argv[3]
    manager.adicionar_tarefa(descricao, horario)

elif comando == "listar":
    manager.listar_tarefas()

elif comando == "concluir":
    task_id = int(sys.argv[2])
    manager.concluir_tarefa(task_id)

elif comando == "clima":
    print(obter_clima())

else:
    print("Comando inválido")

