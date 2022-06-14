from dataclasses import dataclass


class TaskStatus:
    INCOMPLETE = 0
    COMPLETE = 1


@dataclass
class Task:
    id: int
    name: str = "NoName"
    status: int = TaskStatus.INCOMPLETE


class TaskStore:
    def __init__(self):
        self.clear()

    def clear(self):
        self.store = {}
        self.latest_id = 0

    def get_all(self) -> list:
        return list(self.store.values())

    def get(self, id: int) -> Task:
        return self.store.get(id, None)

    def add(self, task: Task) -> bool:
        if task.id in self.store:
            return False
        self.store[task.id] = task
        return True

    def create(self, name: str, status: int = TaskStatus.INCOMPLETE) -> Task:
        self.latest_id += 1
        new_task = Task(id=self.latest_id, name=name, status=status)
        if not self.add(new_task):
            return None
        return new_task

    def update(self, id, name, status) -> Task:
        if id not in self.store:
            return None
        task = self.store[id]
        task.name = name
        task.status = status
        return task

    def delete(self, id) -> bool:
        if id not in self.store:
            return False
        del self.store[id]
        return True


g_store = TaskStore()


def get_store() -> TaskStore:
    return g_store
