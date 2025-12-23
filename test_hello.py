from hello import add, minus


def test_add():
    assert add(1,  2) == 3


def test_minus():
    assert minus(1, 2) == -1
