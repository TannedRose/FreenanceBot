from sqlalchemy import BigInteger, ForeignKey, String, Column, Integer, INT, VARCHAR
from sqlalchemy.orm import DeclarativeBase, Mapped, MappedColumn, Relationship, mapped_column, relationship
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs


engine = create_async_engine(url='sqlite+aiosqlite:///name.sqlite3')

async_session = async_sessionmaker(engine)


class Base(DeclarativeBase):
    pass


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
