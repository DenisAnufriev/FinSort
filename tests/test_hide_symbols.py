import pytest
from src.func import hide_symbols

def test_hide_symbols_card_numbers():
    operations = [
        {'from': 'Visa Gold 1234567812345678', 'to': 'Master 8765432187654321'}
    ]
    expected = [
        {'from': 'Visa Gold 1234 56** **** 5678', 'to': 'Master 8765 43** **** 4321'}
    ]
    result = hide_symbols(operations)
    assert result == expected

def test_hide_symbols_account_numbers():
    operations = [
        {'from': 'Account 12345678901234567890', 'to': 'Account 09876543210987654321'}
    ]
    expected = [
        {'from': 'Account **7890', 'to': 'Account **4321'}
    ]
    result = hide_symbols(operations)
    assert result == expected