from fastapi import FastAPI

# 这里指定 FastAPI 对象
# 运行时给 uvicorn 以 app 指定
app = FastAPI()

# 这一行注册路由
@app.get("/hello") # GET 方法 接口 http://ip:端口/hello
def hello(): # 接口都被调用时的运行函数，括号填入传入参数
    return {"message":"Hallo World!"}

# 接口接收数据对象审查类（作为父类传入子类）
from pydantic import BaseModel

# 定义接收用户对象
class User(BaseModel):
    # 设置初始值
    name: str = "I"
    age: int = 18
    email: str = "example@example.com"

# POST 方法接收
@app.post("/say")
def say(userinput: User):
    return {"message":f"You R {userinput.name} aged {userinput.age}"}

@app.post("/register")
def register(userinput: User):
    a=1
    # 待
