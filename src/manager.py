# src/manager.py

import json
import os
from task import Task

ARQUIVO = "tasks.json"

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1
        self.carregar()

    def carregar(self):
        if not os.path.exists(ARQUIVO):
            return

        with open(ARQUIVO, "r") as f:
            dados = json.load(f)
            for item in dados:
                tarefa = Task(**item)
                self.tasks.append(tarefa)

            if self.tasks:
                self.next_id = max(t.id for t in self.tasks) + 1

    def salvar(self):
        with open(ARQUIVO, "w") as f:
            json.dump([t.__dict__ for t in self.tasks], f, indent=4)

    def adicionar_tarefa(self, descricao, horario):
        tarefa = Task(self.next_id, descricao, horario)
        self.tasks.append(tarefa)
        self.next_id += 1
        self.salvar()
        print("Tarefa adicionada!")

    def listar_tarefas(self):
        if not self.tasks:
            print("Nenhuma tarefa cadastrada.")
            return

        for task in self.tasks:
            print(task)

    def concluir_tarefa(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.marcar_concluida()
                self.salvar()
                print("Tarefa concluída!")
                return
        
        print("Tarefa não encontrada.")