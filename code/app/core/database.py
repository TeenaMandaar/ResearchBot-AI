from sqlmodel import SQLModel, create_engine, Session

# Step 1: Create the connection to the file
# check_same_thread=False is needed specifically for SQLite in web apps
engine = create_engine("sqlite:///./ResearchBot.db", connect_args={"check_same_thread": False})

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    # This is a "Dependency" function.
    # It opens a connection, lets the app use it, and then closes it automatically.
    with Session(engine) as session:
        yield session