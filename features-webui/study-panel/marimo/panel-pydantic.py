import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(r"""
    # panel pydantic

    ## class state pydantic
    """)
    return


@app.cell
def _():
    # import
    import marimo as mo

    return (mo,)


@app.cell
def _():
    return


@app.cell
def _(mo):
    check=mo.ui.checkbox(False,label="hello")
    check
    return (check,)


@app.cell
def _(check):
    check.value
    return


if __name__ == "__main__":
    app.run()
