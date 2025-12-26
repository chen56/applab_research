import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo


    mo.md("ssssss")
    return (mo,)


@app.cell
def _():
    import os
    import datetime
    print(datetime.datetime.now())
    os.getcwd()
    return


@app.cell
def _(mo):
    slider = mo.ui.slider(1, 22)
    slider
    return (slider,)


@app.cell
def _(slider):
    slider.value
    return


if __name__ == "__main__":
    app.run()
