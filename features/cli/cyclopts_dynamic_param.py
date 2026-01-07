from dataclasses import make_dataclass
from cyclopts import App

DynamicOpts = make_dataclass(
    "DynamicOpts",
    [
        ("region", str, None),
        ("gpu", int, 0),
    ],
)

app = App()

@app.default()
def deploy(opts: DynamicOpts):
    print(opts)
app()
# app.group_parameters.