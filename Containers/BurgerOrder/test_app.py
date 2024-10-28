import app

def test_add():
    assert app.add(7, 3) == 10
    assert app.add(7) == 9
