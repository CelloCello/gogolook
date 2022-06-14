import logging
from dataclasses import asdict

from flask import request
# from flask import Blueprint

from app import app
from app.utilities import json_response, check_params
from app.store import get_store, TaskStatus

logger = logging.getLogger()
store = get_store()
ROUTE_PREFIX = "tasks"


@app.route(f"/{ROUTE_PREFIX}", methods=["GET"])
def get_tasks():
    logger.info("Get tasks")
    tasks = store.get_all()
    tasks = [asdict(t) for t in tasks]
    return json_response(tasks)


@app.route(f"/{ROUTE_PREFIX}/<int:id>", methods=["GET"])
def get_task(id):
    logger.info(f"Get a task: {id}")
    task = store.get(id)
    if not task:
        logger.warning(f"Task not found: {id}")
        return json_response(None, 404)
    return json_response(asdict(task))


@app.route(f"/{ROUTE_PREFIX}", methods=["POST"])
def create_task():
    logger.info("Create a task")
    req_json = request.get_json()
    check_params([("name", str)], req_json)

    task_name = req_json.get("name", "")

    task = store.create(name=task_name)
    if not task:
        logger.warning(f"Task create failed: {task_name}")
        return json_response(None, 404)
    logger.info(f"Task was created: {task.id}")
    return json_response(asdict(task), 201)


@app.route(f"/{ROUTE_PREFIX}/<int:id>", methods=["PUT"])
def update_task(id):
    logger.info(f"Update a task: {id}")
    req_json = request.get_json()
    check_params([("name", str), ("status", int)], req_json)

    new_name = req_json.get("name", "NoName")
    new_status = req_json.get("status", TaskStatus.INCOMPLETE)

    task = store.update(id, new_name, new_status)
    if not task:
        logger.warning(f"Task not found: {id}")
        return json_response(None, 404)
    logger.info(f"Task was updated: {id}, {new_name}, {new_status}")
    return json_response(asdict(task))


@app.route(f"/{ROUTE_PREFIX}/<int:id>", methods=["DELETE"])
def delete_task(id):
    logger.info(f"Delete a task: {id}")
    if not store.delete(id):
        logger.warning(f"Task not found: {id}")
        return json_response(None, 404)
    logger.info(f"Task was deleted: {id}")
    return json_response()
