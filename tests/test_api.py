import unittest

from app import app
from app.store import TaskStatus, g_store

client = app.test_client()


def test_hello():
    resp = client.get("/")
    data = resp.text
    assert data == "<p>Hello, World!</p>"


class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = app
        # self.app_context = self.app.app_context()
        # self.app_context.push()
        self.client = self.app.test_client()
        g_store.clear()

    # def tearDown(self):
    #     self.app_context.pop()

    def test_CRUD(self):
        # create a task
        resp = self.client.post("/tasks", json={"name": "buy dinner"})
        data = resp.get_json()
        result = data["result"]
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(result["id"], 1)
        self.assertEqual(result["name"], "buy dinner")

        # list tasks
        resp = self.client.get("/tasks")
        data = resp.get_json()
        result = data["result"]
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(result), 1)

        # update task
        resp = self.client.put(
            f"/tasks/{1}",
            json={"name": "buy breakfast", "status": TaskStatus.COMPLETE},
        )
        data = resp.get_json()
        result = data["result"]
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(result["id"], 1)
        self.assertEqual(result["name"], "buy breakfast")
        self.assertEqual(result["status"], TaskStatus.COMPLETE)

        # delete task
        resp = self.client.delete(f"/tasks/{1}")
        data = resp.get_json()
        result = data["result"]
        self.assertEqual(resp.status_code, 200)

        # list tasks
        resp = self.client.get("/tasks")
        data = resp.get_json()
        result = data["result"]
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(result), 0)

    def test_error(self):
        # create a task
        resp = self.client.post("/tasks", json={"name": "buy dinner"})
        data = resp.get_json()
        result = data["result"]
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(result["id"], 1)
        self.assertEqual(result["name"], "buy dinner")

        # get a none existing task
        resp = self.client.get(f"/tasks/{2}")
        data = resp.get_json()
        result = data["result"]
        self.assertEqual(resp.status_code, 404)

        # update a none existing task
        resp = self.client.put(
            f"/tasks/{2}",
            json={"name": "buy breakfast", "status": TaskStatus.COMPLETE},
        )
        data = resp.get_json()
        result = data["result"]
        self.assertEqual(resp.status_code, 404)

        # delete a none existing task
        resp = self.client.delete(f"/tasks/{2}")
        data = resp.get_json()
        result = data["result"]
        self.assertEqual(resp.status_code, 404)
