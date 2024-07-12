from abc import ABC, abstractmethod


class BaseRepository(ABC):
    @abstractmethod
    def add(self):
        ...

    @abstractmethod
    def get(self, specification: ...):
        ...

    @abstractmethod
    def filter(self, specification: ...):
        ...

    @abstractmethod
    def all(self):
        ...
