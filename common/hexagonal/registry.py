from __future__ import annotations
from enum import Enum
from typing import Type

from common.hexagonal.exceptions import (
    NotExistingRelationalDatabaseSettings,
    NotExistingNoSQLDatabaseSettings,
    NotExistingInMemoryDatabaseSettings,
)


class AdapterCategoryEnum(Enum):
    RelationalDB = "RelationalDB"  #  Postgres, MySQL
    NoSQLDB = "NoSQLDB"  #  Mongo, Cassandra
    QueueBroker = "QueueBroker"  #  RabbitMQ, Kaffka
    InMemoryDB = "InMemoryDB"  #  Redis, Memcached


class CategoryAdapterRegistry:
    """Registry for adapters"""

    EXCEPTION_MAPPING = {
        AdapterCategoryEnum.RelationalDB: NotExistingRelationalDatabaseSettings,
        AdapterCategoryEnum.NoSQLDB: NotExistingNoSQLDatabaseSettings,
        AdapterCategoryEnum.InMemoryDB: NotExistingInMemoryDatabaseSettings,
    }

    adapters_by_category: dict = {key: None for key in AdapterCategoryEnum}

    @classmethod
    def get_exception_for_adapter_category(cls, adapter_category: AdapterCategoryEnum):
        return (
            cls.EXCEPTION_MAPPING[adapter_category]
            if adapter_category in cls.EXCEPTION_MAPPING
            else Exception(
                f"Cant get adapter {adapter_category.value} from application."
            )
        )

    @classmethod
    def get_adapter_by_category_or_exception(
        cls, adapter_category: AdapterCategoryEnum
    ) -> CategoryAdapter:
        """
        Returns adapter. For example DB Session, Redis pool, Rabbit Queue etc
        """

        # By the way Morse operator
        if (adapter := cls.adapters_by_category[adapter_category]) is None:
            exception = cls.get_exception_for_adapter_category(adapter_category)
            raise exception

        return adapter

    @classmethod
    def register_adapter(cls, adapter: Type[CategoryAdapter]):
        if cls.adapters_by_category[adapter.category] is None:
            cls.adapters_by_category[adapter.category] = adapter()


class CategoryAdapter:
    category: AdapterCategoryEnum

    def __new__(cls, *args, **kwargs):
        if cls is CategoryAdapter:
            raise Exception("Cannot be instantiated")

        return object.__new__(*args, **kwargs)

    @classmethod
    def register(cls) -> None:
        CategoryAdapterRegistry.register_adapter(cls)
