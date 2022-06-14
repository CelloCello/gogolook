from flask import jsonify

from app.exceptions import ParamError


def json_response(result=None, status_code=200):
    if result is None:
        result = {}
    data = {"result": result}
    return jsonify(data), status_code


def check_params(check_list, params):
    """check (key, type) from params"""
    for check in check_list:
        key = check[0]
        param_type = check[1]
        if not params.get(key):
            raise ParamError(f"Please input [{key}]")
        if type(params[key]) != param_type:
            raise ParamError(
                f"{key} type error ({str(type(params[key]))} not {param_type})"
            )
