from pydantic import BaseModel

class User(BaseModel):
    # 纯类常量，不参与模型字段校验
    DEFAULT_ROLE: str = "user"
    MAX_AGE: int = 120

    # 模型的普通字段
    name: str
    age: int

# 访问类常量
print(User.DEFAULT_ROLE)  # 输出: user
print(User.MAX_AGE)       # 输出: 120

# 实例也可以访问
user = User(name="Alice", age=25)
print(user.DEFAULT_ROLE)  # 输出: user