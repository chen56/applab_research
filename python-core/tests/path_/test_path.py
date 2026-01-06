from pathlib import PosixPath


def test_path():
    from pathlib import Path
    # assert Path(Path.home(), "b").__str__() == "a/b"
    print ("----",Path(Path.home(), "b"))
    assert str(Path("a", "b")) == "a/b"
    assert Path("a", "b").joinpath("c").__str__() == "a/b/c"
    CONFIG_DIR = Path.home().joinpath(".applab")
    print(f"{CONFIG_DIR=}")
    ACCOUNTS_FILE = CONFIG_DIR.joinpath(".accounts.json")
    print(f"{ACCOUNTS_FILE=}")
    print(f"{PosixPath("a", "b").joinpath("c")}")

