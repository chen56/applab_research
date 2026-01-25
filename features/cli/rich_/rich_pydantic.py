#%% [markdown]
# ### 验证 CloudAccount 序列化
# 这里我们在交互式窗口测试字段是否丢失

#%%
import rich
from pydantic import TypeAdapter, BaseModel, ConfigDict
from typing import Union

# 1. 定义模型 (模拟你的 apphub 结构)
class CloudAccount(BaseModel):
    name: str
    vendor: str

class TencentCloudAccount(CloudAccount):
    app_id: str
    uin: str

#%%
# 2. 构造数据
a = TencentCloudAccount(name="test", vendor="tencent", app_id="123", uin="1001")

# 3. 不同的适配方案对比
# 方案 A: 严格基类 (会丢失字段)
adapter_strict = TypeAdapter(list[CloudAccount])

# 方案 B: 多态 Union (保留字段)
adapter_poly = TypeAdapter(list[Union[TencentCloudAccount, CloudAccount]])

#%%
# 4. 运行并查看结果

rich.print("[bold green]Strict Adapter Result (Fields Lost):[/bold green]")
rich.print(adapter_strict.dump_python([a]))

rich.print("\n[bold blue]Polymorphic Adapter Result (All OK):[/bold blue]")
rich.print(adapter_poly.dump_python([a]))

console=rich.console.Console(force_jupyter=True)
console.print("\n[bold blue]Polymorphic Adapter Result (All OK):[/bold blue]")


# 测试 Pydantic TypeAdapter 的性能
from pydantic import TypeAdapter
adapter = TypeAdapter(list[int])
