
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

dbuser = "user"
dbpsd = "psd"
dbserver = "localhost"
dbport = 3306
dbname = "fastapi_demo"

# 设置数据库配置 数据库 + 数据库驱动 ://
SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{dbuser}:{dbpsd}@{dbserver}:{dbport}/{dbname}"

# 启动数据库链接
dbengine = create_engine(SQLALCHEMY_DATABASE_URL)

# 启动会话管理器（绑定对象到数据库链接）
sessions = sessionmaker(bind = dbengine)

# 设置整个数据库的基底对象，无需更多设置
class Base(DeclarativeBase):
    pass

def get_session():
    session = sessions()
    try:
        yield session
    finally:
        session.close()

        