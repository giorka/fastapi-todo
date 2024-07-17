from __future__ import annotations

from abc import ABC
from dataclasses import dataclass

from sqlalchemy.ext.asyncio import AsyncSession


@dataclass
class IRepository(ABC):
    session: AsyncSession
