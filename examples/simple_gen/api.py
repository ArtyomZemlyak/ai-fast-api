"""
File contains description of class DocAPI.
"""

import io
import json
import os
import logging
import pathlib
from time import time
from typing import Any, List, Union
from base64 import b64encode, b64decode

import datetime
import logging
import re
from uuid import uuid4

logging.basicConfig(format="%(asctime)s %(levelname)s:%(message)s", level=logging.INFO)

from ai_common_utils.config import load_config

# from adapters.file_storage import FileStorageAdapter


class DocAPI:
    """
    A class of Doc API. Share API for different apps. Work with documents sended from them.

    Args
    ----------
            `config` : Path to config.json file or dict with config for DocAPI.
    """

    def __init__(self, config: Union[str, dict] = None) -> None:
        # self._CONFIG = load_config(config, level=3)
        logging.info("DocAPI initialization...")

        # self.file_storage = FileStorageAdapter(self._CONFIG)
        # self.file_storage.connect()
        # self.file_storage.create_section(self._CONFIG["file_storage"]["section_name"])

        # self.arrow = ArrowClient(
        #     self._CONFIG
        # )  # TODO: Add configuration and loading if needed

        logging.info("DocAPI initialized.")

    # ---INNER-METHODS------------------
    def _create_tables(self, tables: List[dict] = None):
        """
        Create specific tables for VarvaraAPI.

        Args
        ----------
                `tables` : List of tables to create for working with VarvaraAPI.
        """
        if type(tables) == list and len(tables) != 0:
            for table in tables:
                self.postgres.create_table(f"API_{table['name']}", table["columns"])

    def _done(self, status: int = 1, data: Any = None, descr: str = None):
        if descr:
            logging.info(descr)
        return {
            "status": status,
            "data": data,
            "description": descr,
        }

    def _error(
        self, status: int = 0, code: int = 404, error: str = None, descr: str = None
    ):
        if descr:
            logging.error(descr)
        return {
            "status": status,
            "code": code,
            "error": error,
            "description": descr,
        }

    def method(self, *args, **kwargs):
        return "its `method`"
