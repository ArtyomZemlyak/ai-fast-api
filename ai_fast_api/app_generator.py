#!/usr/bin/env python

import logging
from typing import Callable
import sys

from fastapi import FastAPI, Request

# TODO: from fastapi_utils.tasks import repeat_every


def copy_doc(copy_func: Callable) -> Callable:
    """Use Example: copy_doc(self.copy_func)(self.func) or used as deco"""

    def wrapper(func: Callable) -> Callable:
        func.__doc__ = copy_func.__doc__
        return func

    return wrapper


async def _template(func, request):
    """
    Used to receive messages on the set port (in main.py).

    Args
    ----------
        `request` : Message from POST. Task, that needed be executed.

    Return
    ----------
        `dict` : result of executing task.
    """
    try:
        task_msg = await request.json()
    except Exception as e:
        logging.error("Cant read json data!", exc_info=True)
        return {"error": "Cant read json data!"}

    try:
        result_msg = {"error": "Error occured while execute task!"}
        logging.info("Task started...")

        result_msg = await func(task_msg)

        logging.info("Task done.")
    except Exception as e:
        logging.error("Error occured while doing task! Task aborted!", exc_info=True)
        return {"error": "Error occured while doing task! Task aborted!"}

    return result_msg


def async_func(func):
    @copy_doc(func)
    async def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


def app_func(app, func, func_name):
    @app.post(f"/{func_name}/")
    @copy_doc(func)
    async def wrapper(request: Request):
        result_msg = await _template(func, request)
        return result_msg

    return wrapper


THIS_MODULE = sys.modules[__name__]


def generate_api(api_class):
    app = FastAPI()

    api_methods = [i for i in api_class.__dir__() if i[0] != "_"]

    for func_name in api_methods:
        func = api_class.__getattribute__(func_name)
        ay_func = async_func(func)
        api_func = app_func(app, ay_func, func_name)
        setattr(THIS_MODULE, func_name, api_func)

    return app
