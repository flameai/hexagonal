"""
Здесь буду храниться настройки приложения 
в гексагональных рамках в целом
"""

from __future__ import annotations
from typing import Type

class App:

    @classmethod
    def register_adapter(cls, adapter: Type[CategoryAdapter]) -> None:
        adapter.register()

    @classmethod
    def register_port()
