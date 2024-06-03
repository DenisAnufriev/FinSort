import pytest
from src.func import sorted_executed

def test_sorted_executed():
    operations = [
        {'id': 1, 'state': 'EXECUTED', 'amount': 100},
        {'id': 2, 'state': 'PENDING', 'amount': 200},
        {'id': 3, 'state': 'EXECUTED', 'amount': 150},
        {'id': 4, 'state': 'FAILED', 'amount': 50},
        {'id': 5, 'state': 'EXECUTED', 'amount': 300}
    ]

    expected_output = [
        {'id': 1, 'state': 'EXECUTED', 'amount': 100},
        {'id': 3, 'state': 'EXECUTED', 'amount': 150},
        {'id': 5, 'state': 'EXECUTED', 'amount': 300}
    ]

    assert sorted_executed(operations) == expected_output