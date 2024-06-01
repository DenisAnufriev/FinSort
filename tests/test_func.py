import pytest
from src.func import get_operations
def test_get_operations():
    assert {} not in get_operations()

test_get_operations()