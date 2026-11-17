
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from database.database import Base

class UserList(Base):
    # 数据表名
    __tablename__ = "userList"

    # 设置数据表的列，存储用户名、id、email
    # 中间是类型声明，需要使用 Mapped[]传入
    # 后面一项是这一列的声明（primary_key 主键、String(1)字符串长度-放在第一位、unque 不允许重复）
    name:  Mapped[str] = mapped_column(String(50))
    id:    Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)

