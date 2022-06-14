import unittest

from app.store import TaskStatus, TaskStore, Task


class StoreTestCase(unittest.TestCase):
    def setUp(self):
        self.store = TaskStore()

    def test_CRUD(self):
        # create two tasks
        new_task = self.store.create("buy dinner")
        self.assertEqual(new_task.id, 1)
        self.assertEqual(new_task.name, "buy dinner")
        self.assertEqual(new_task.status, TaskStatus.INCOMPLETE)

        new_task = self.store.create("buy dinner")
        self.assertEqual(new_task.id, 2)
        self.assertEqual(new_task.name, "buy dinner")
        self.assertEqual(new_task.status, TaskStatus.INCOMPLETE)

        # list tasks
        tasks = self.store.get_all()
        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[1].id, 2)

        # update task
        updated_task = self.store.update(
            1, "buy breakfast", TaskStatus.COMPLETE
        )
        self.assertEqual(updated_task.id, 1)
        self.assertEqual(updated_task.name, "buy breakfast")
        self.assertEqual(updated_task.status, TaskStatus.COMPLETE)

        # delete task
        result = self.store.delete(1)
        self.assertTrue(result)

        # list tasks
        tasks = self.store.get_all()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].id, 2)

    def test_error(self):
        # create a task
        new_task = self.store.create("buy dinner")
        self.assertEqual(new_task.id, 1)
        self.assertEqual(new_task.name, "buy dinner")
        self.assertEqual(new_task.status, TaskStatus.INCOMPLETE)

        # add an task with existing id
        new_task = Task(1, "buy dinner")
        result = self.store.add(new_task)
        self.assertFalse(result)

        # update a none existing task
        updated_task = self.store.update(3, "No", TaskStatus.INCOMPLETE)
        self.assertIsNone(updated_task)

        # delete a none existing task
        result = self.store.delete(3)
        self.assertFalse(result)
