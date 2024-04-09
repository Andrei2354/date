import pytest
from areas import Areas

@pytest.fixture
def areas1():
    return Areas(4, 8)

def test_areaRectangulo(areas1):
    assert areas1.areaRectangulo() == 32


def test_areaTriangulo(areas1):
    assert areas1.areaTriangulo() == 16