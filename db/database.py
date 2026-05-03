from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "postgresql://postgres:%40soufiane0908%40@localhost:5432/mybrand_db"

engine = create_engine(DATABASE_URL, echo=True)

def creat_db():
    SQLModel.metadata.create_all(engine)
    

def get_session():
    with Session(engine) as session:
        yield session