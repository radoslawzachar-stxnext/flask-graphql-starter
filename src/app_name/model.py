from sqlalchemy import *
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, relationship, scoped_session, sessionmaker

from app_name.consts import CONNECTION_STRING

engine = create_engine(CONNECTION_STRING, convert_unicode=True)
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)

Base = declarative_base()
# We will need this for querying
Base.query = db_session.query_property()


class Category(Base):
    __tablename__ = "category"
    id = Column(UUID, primary_key=True)
    name = Column(String)


class Product(Base):
    __tablename__ = "product"
    id = Column(UUID, primary_key=True)
    name = Column(String)
    weight = Column(Integer)
    unit = Column(Float)
    unit_of_measure = Column(String)
    date_added = Column(DateTime)
    category = Column(ForeignKey(Category.id))
