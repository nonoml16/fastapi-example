from sqlalchemy import *
from sqlalchemy.orm import *

SQL_DATABASE_URL='sqlite:///./sql_app.db'

engine = create_engine(SQL_DATABASE_URL, conntect_args={'check_same_thread': False})

Session=sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_session()-> Session:
    session = Session()
    try:
        yield session
    finally:
        session.close()

