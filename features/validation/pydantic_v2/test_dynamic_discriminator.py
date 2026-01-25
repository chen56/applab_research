from pydantic import BaseModel, Field, TypeAdapter, Discriminator
from typing import Annotated, Dict, Type, Union, Literal, List
import pytest

# 1. 定义基类
class Animal(BaseModel):
    kind: Annotated[str, Field(frozen=True)]

# 2. 定义子类型
class Cat(Animal):
    kind: Literal["cat"]
    meow: str

class Dog(Animal):
    kind: Literal["dog"]
    bark: str

# 3. 动态注册机制
# 假设我们有一个类型集合，可以动态增加
# registered_types: List[Type[Animal]] = [Cat, Dog]
registered_types: List[type[Animal]] = []
registered_types.append(Cat)
registered_types.append(Dog)

def get_dynamic_animal_adapter():
    # 核心：使用 Union[*types] 动态构建 Union 类型
    # 使用 Annotated 和 Discriminator 显式指定鉴别器字段，提高性能并避免歧义
    DynamicUnion = Annotated[Union[tuple(registered_types)], Discriminator("kind")]
    return TypeAdapter(DynamicUnion)

def test_dynamic_parsing():
    adapter = get_dynamic_animal_adapter()

    # 测试解析 Cat
    cat_data = {"kind": "cat", "meow": "miu"}
    cat_obj = adapter.validate_python(cat_data)
    assert isinstance(cat_obj, Cat)
    assert cat_obj.meow == "miu"

    # 测试解析 Dog
    dog_data = {"kind": "dog", "bark": "woof"}
    dog_obj = adapter.validate_python(dog_data)
    assert isinstance(dog_obj, Dog)
    assert dog_obj.bark == "woof"

    # 4. 动态增加新类型
    class Bird(Animal):
        kind: Literal["bird"] = "bird"
        tweet: str
    
    registered_types.append(Bird)
    
    # 重新获取 adapter (因为 Union 已经变了)
    new_adapter = get_dynamic_animal_adapter()
    bird_data = {"kind": "bird", "tweet": "chirp"}
    bird_obj = new_adapter.validate_python(bird_data)
    assert isinstance(bird_obj, Bird)
    assert bird_obj.tweet == "chirp"

if __name__ == "__main__":
    # 手动运行演示
    adapter = get_dynamic_animal_adapter()
    
    data = [
        {"kind": "cat", "meow": "miu"},
        {"kind": "dog", "bark": "woof"}
    ]
    
    # 解析列表
    ListAdapter = TypeAdapter(List[Annotated[Union[tuple(registered_types)], Discriminator("kind")]])
    animals = ListAdapter.validate_python(data)
    print(f"Parsed animals: {animals}")
    
    # 动态添加并再次尝试
    class Bird(Animal):
        kind: Literal["bird"] = "bird"
        tweet: str
    registered_types.append(Bird)
    
    # 更新 ListAdapter
    DynamicUnion = Annotated[Union[tuple(registered_types)], Discriminator("kind")]
    NewListAdapter = TypeAdapter(List[DynamicUnion])
    
    data.append({"kind": "bird", "tweet": "chirp"})
    animals = NewListAdapter.validate_python(data)
    print(f"Parsed animals with bird: {animals}")
