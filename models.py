import os
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

# Definir o caminho do banco de dados para ser criado na mesma pasta que o script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "projeto1.db")

# Criar a URL de conexão usando o caminho absoluto
CONN = f"sqlite:///{db_path}"

engine = create_engine(CONN, echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# Definir a classe Produto
class Produto(Base):
    __tablename__ = "PRODUTO"
    id = Column(Integer, primary_key=True)
    titulo = Column(String(50))
    preco = Column(Float())

# Criar as tabelas no banco de dados
Base.metadata.create_all(engine)
