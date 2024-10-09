import sqlalchemy as sa
from config import Config

engine = sa.create_engine(Config.SQLALCHEMY_DATABASE_URI)
