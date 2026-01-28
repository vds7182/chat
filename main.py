from fastapi import FastAPI
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession
from config import Config
async_engine: AsyncEngine = create_async_engine(Config.DATABASE_URL, echo=True)

SessionLocal = sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def get_session() -> AsyncSession:
    async with SessionLocal() as session:
        yield session

# --- DB init ---
async def init_db():
    async with async_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
def life_span():
    print("Lifespan!!!!!")
    init_db()
    yield
    print("LIFeSPANEND!!!!!!!!!!!!!!!")
app = FastAPI(life_span=life_span,name="Chat")

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
