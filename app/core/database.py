from sqlmodel import SQLModel, create_engine, Session

sqlite_filename = 'RPA_Tools.db'

sqlite_url = f"sqlite:///{sqlite_filename}"

engine = create_engine(sqlite_url, echo=True)

def init_db():
    from models import Bot, HistoryExecution
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session