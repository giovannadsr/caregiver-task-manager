class Task:
    def __init__(self, id, descricao, horario, concluida=False):
        self.id = id
        self.descricao = descricao
        self.horario = horario
        self.concluida = concluida

    def marcar_concluida(self):
        self.concluida = True

    def __str__(self):
        status = "✔" if self.concluida else "✘"
        return f"[{self.id}] {self.descricao} - {self.horario} ({status})"