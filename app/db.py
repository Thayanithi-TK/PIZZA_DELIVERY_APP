from sqlalchemy.ext.asyncio import create_async_engine ,AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

DATABSE_URL = 'postgresql://root:root@local:5432/Bizza_Delivey_App'

engine = create_async_engine(DATABSE_URL, echo=True ,future=True)


AsyncSessionlocal=sessionmaker(
    bind=engine,
    class_=AsyncSession
    expire_on_commit=False
)

Base =declarative_base()

async def get_db():
    async with AsyncSessionlocal() as session:
        yield session