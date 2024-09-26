""" Module to handle all handlers in the infrastructure layer """

import importlib
import os
from types import ModuleType
from typing import Iterator


class Handlers:
    """Module to handle all handlers in the infrastructure layer"""

    path = ("src", "infrastructure", "handlers")
    ignored = ("__init__.py", "__pycache__")

    @classmethod
    def __all_module_names(cls) -> list:
        """Return a list of all handlers in the infrastructure layer"""
        return list(
            filter(
                lambda module: module not in cls.ignored, os.listdir("/".join(cls.path))
            )
        )

    @classmethod
    def __module_namespace(cls, handler_name: str) -> str:
        """Return the namespace of the handler"""
        return f"{'.'.join(cls.path)}.{handler_name}"

    @classmethod
    def iterator(cls) -> Iterator[ModuleType]:
        """Iterate over all handlers in the infrastructure layer"""

        for module in cls.__all_module_names():
            handler = importlib.import_module(cls.__module_namespace(module[:-3]))
            yield handler

    @classmethod
    def modules(cls) -> map:
        """Return a map of all handlers in the infrastructure layer"""
        return map(
            lambda module: cls.__module_namespace(module[:-3]), cls.__all_module_names()
        )
