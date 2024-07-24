from common.task import Task

class InMemoryDatabase:
    def __init__(self):
        self._storage: dict[str, Task] = dict()

    def store(self, task: Task):
        self._storage[task.name] = task

    def load(self, name: str):
        return self._storage[name]

    def delete(self, name: str):
        self._storage.pop(name)

    def load_all(self):
        return self._storage.values()