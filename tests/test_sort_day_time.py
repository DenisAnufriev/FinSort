import pytest
from datetime import datetime
from src.func import sort_day_time


def test_sorting_order():
    operations = [
        {'date': '2023-06-01T12:30:00'},
        {'date': '2023-05-01T08:45:00'},
        {'date': '2023-06-01T15:00:00'}
    ]

    expected = [
        {'date': '01.06.2023 15:00:00'},
        {'date': '01.06.2023 12:30:00'},
        {'date': '01.05.2023 08:45:00'}
    ]

    result = sort_day_time(operations)
    assert result == expected


def test_already_sorted():
    operations = [
        {'date': '2023-06-01T15:00:00'},
        {'date': '2023-06-01T12:30:00'},
        {'date': '2023-05-01T08:45:00'}
    ]

    expected = [
        {'date': '01.06.2023 15:00:00'},
        {'date': '01.06.2023 12:30:00'},
        {'date': '01.05.2023 08:45:00'}
    ]

    result = sort_day_time(operations)
    assert result == expected