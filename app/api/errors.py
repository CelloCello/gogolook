import logging
import traceback

from app import app
from app.utilities import json_response
from app.exceptions import BaseError

logger = logging.getLogger()


@app.errorhandler(Exception)
def handle_unexpected_error(error):
    print("eeeee111111", error)
    except_msg = traceback.format_exc()
    logger.error(except_msg)
    result = {
        "type": "UnexpectedException",
        "exception": repr(error),
        "traceback": except_msg,
    }
    return json_response(result, 500)


@app.errorhandler(BaseError)
def handle_base_error(error):
    print("eeeee222222")
    result = {"exception": repr(error), "traceback": traceback.format_exc()}
    return json_response(result, error.status_code)
