from sqlalchemy import create_engine, BIGINT, insert, select
from sqlalchemy.orm import declarative_base, Mapped, Session, mapped_column

engine = create_engine("postgresql+psycopg2://postgres:1@localhost:5432/fitnice_bot")

Base = declarative_base()
session = Session(bind=engine)


class User(Base):
    __tablename__ = 'bot_users'
    id: Mapped[int] = mapped_column(__type_pos=BIGINT, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(__type_pos=BIGINT, unique=True)
    first_name: Mapped[str] = mapped_column(nullable=True)
    last_name: Mapped[str] = mapped_column(nullable=True)
    username: Mapped[str] = mapped_column(unique=True, nullable=True)


Base.metadata.create_all(engine)

session.close()
