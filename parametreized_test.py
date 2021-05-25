import pytest

@pytest.mark.parametrize("num,output",[(2,20),(3,33),(4,40),(5,55)])

def test_multiplication(num,output):
    assert 10*num == output
