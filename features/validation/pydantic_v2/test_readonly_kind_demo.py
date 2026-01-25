from typing import Annotated

from pydantic import BaseModel, ValidationError, Field
import pytest

# 方案 1: 使用 Field(frozen=True) 使特定字段只读
class AnimalFieldFrozen(BaseModel):
    kind: Annotated[str, Field(frozen=True)]

# 方案 2: 使用 model_config 使整个模型只读
class AnimalModelFrozen(BaseModel):
    model_config = {"frozen": True}
    kind: str

def test_field_frozen():
    animal = AnimalFieldFrozen(kind="cat")
    assert animal.kind == "cat"
    with pytest.raises(ValidationError) as excinfo:
        animal.kind = "dog"
    assert "Field is frozen" in str(excinfo.value)
    print("Field(frozen=True) works: kind is readonly")

def test_model_frozen():
    animal = AnimalModelFrozen(kind="cat")
    assert animal.kind == "cat"
    with pytest.raises(ValidationError) as excinfo:
        animal.kind = "dog"
    assert "Instance is frozen" in str(excinfo.value)
    print("model_config frozen=True works: kind is readonly")

if __name__ == "__main__":
    test_field_frozen()
    test_model_frozen()
