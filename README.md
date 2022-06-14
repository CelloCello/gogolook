# gogolook

Coding Exercise from Gogolook

- Python 3.7.10
- Flask 2.0.3
- pytest 7.1.2

[Spec](coding_exercise.md)

## Notes

- In the spec, the endpoints of API have `/tasks` and `/task`. I unified them into `/tasks` to become more RESTful.

- Because of using an in-memory mechanism to handle data storage and there is no any lock when doing storage operation, it can only run in a single thread in one process to protect data.

- It should use WSGI HTTP Server like gunicorn, uWSGI in the container to get higher performance. But because of the previous point, WSGI HTTP Server become meaningless. So I set `FLASK_ENV=development` and execute `flask run` directly.


## Run in Container

### Build image

    $ sh docker/build.sh

You will get an image named `gogolook:latest`

### Run container

    $ docker run -d -p 5000:5000 --name=gogolook gogolook:latest

After running container, you can access `localhost:5000` by browser to see the Hello World page and `localhost:5000/tasks` to get task list.

Then, you can use `curl` or `Postman` to test the APIs.


## Run for Development

Install requirements in your virtual environment first.

    $ pip install -r requirements.txt

Run app by Flask CLI

    $ flask run

## Unit Test

Install requirements for testing first.

    $ pip install -r requirements-test.txt

Run pytest

    $ pytest
