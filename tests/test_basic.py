
def test_addition():
    assert 1 + 1 == 2


def test_temperature_range():
    temperature = 0.3
    assert 0.0 <= temperature <= 1.0


def test_retrieval_k():
    k = 5
    assert k > 0
