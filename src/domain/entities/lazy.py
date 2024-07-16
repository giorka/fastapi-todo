from typing import Generator

from domain.entities.base import BaseEntity


class LazyEntity(BaseEntity):
    def __init__(self, data_source: dict) -> None:
        self.data_source = data_source
        self.__dict__ = data_source

    # def __getitem__(self, key: str) -> any:
    #     if key not in self.cache:
    #         self.cache[key] = self.data_source[key]
    #
    #     return self.cache[key]

    # def __iter__(self) -> Generator[None, None, any]:
    #     for key in self.data_source:
    #         yield getattr(self, key)
