
# pytest -v

def inc(x):
    return x + 1

def test_basico():
    assert inc(3) == 4
