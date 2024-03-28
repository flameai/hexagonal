from __future__ import annotations
from abc import ABC, abstractmethod
from enum import Enum

from common.hexagonal.exceptions import (
    NotExistingRelationalDatabaseSettings,
    NotExistingNoSQLDatabaseSettings,
    NotExistingInMemoryDatabaseSettings,
)


class ComponentCategoryEnum(Enum):
    RelationalDB = "RelationalDB"  #  Postgres, MySQL
    NoSQLDB = "NoSQLDB"  #  Mongo, Cassandra
    QueueBroker = "QueueBroker"  #  RabbitMQ, Kaffka
    InMemoryDB = "InMemoryDB"  #  Redis, Memcached


class CategoryСomponentRegistry:
    """Registry for components"""

    EXCEPTION_MAPPING = {
        ComponentCategoryEnum.RelationalDB: NotExistingRelationalDatabaseSettings,
        ComponentCategoryEnum.NoSQLDB: NotExistingNoSQLDatabaseSettings,
        ComponentCategoryEnum.InMemoryDB: NotExistingInMemoryDatabaseSettings,
    }

    components_by_category: dict = {key: None for key in ComponentCategoryEnum}

    @classmethod
    def get_exception_for_component_category(
        cls, component_category: ComponentCategoryEnum
    ):
        return (
            cls.EXCEPTION_MAPPING[component_category]
            if component_category in cls.EXCEPTION_MAPPING
            else Exception(
                f"Cant get component {component_category.value} from application."
            )
        )

    @classmethod
    def get_component_by_category_or_exception(
        cls, component_category: ComponentCategoryEnum
    ) -> CategoryComponent:
        """
        Returns component. For example DB Session, Redis pool, Rabbit Queue etc
        """

        # By the way Morse operator
        if (component := cls.components_by_category[component_category]) is None:
            exception = cls.get_exception_for_component_category(component_category)
            raise exception

        return component

    @classmethod
    def register_component(cls, component: CategoryComponent):
        if cls.components_by_category[component.category] is None:
            cls.components_by_category[component.category] = component


class CategoryComponent:
    category: ComponentCategoryEnum

    def __new__(cls, *args, **kwargs):
        if cls is CategoryComponent:
            raise Exception('Cannot be instantiatied')

        return object.__new__(*args, **kwargs)

    def __init__(self) -> None:
        self.register()

    def register(self) -> None:
        CategoryComponentRegistry.register_component(self)
