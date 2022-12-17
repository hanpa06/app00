import pytest
import sys, pathlib

sys.path.append(str(pathlib.Path(__file__).parent.parent/'src'))

from app00.mod00 import add, sub


@pytest.mark.parametrize("a, b, exp", [
    (3,5,8), (1,2,3), (5,6,11)
])
def test_add(a, b, exp):
    assert add(a,b) == exp

@pytest.mark.parametrize("a, b, exp", [
    (3,5,-2), (1,2,-1), (5,6,-1)
])
def test_sub(a, b, exp):
    assert sub(a,b) == exp