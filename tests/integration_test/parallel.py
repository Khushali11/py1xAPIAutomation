# parallel excution
def test_tc1():
    assert 4 == 3


def test_tc2():
    assert True


def test_tc3():
    assert False


def test_tc4():
    return 4 != 6



#pip install pytest-xdist
#pytest -n auto tests/integration_test/parallel.py
#pytest -n 2 auto tests/integration_test/parallel.py

