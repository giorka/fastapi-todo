from dataclasses import dataclass

from domain.entities.base import IEntity


@dataclass
class GetEntityBuilder:
    entity: type[IEntity]
    data_src: dict

    def build(self) -> 'entity':
        return self.entity(**self.data_src)

    def __call__(self, *args, **kwargs) -> 'entity':
        return self.build()
