# FinSort
Этот проект предоставляет функции для фильтрации и сортировки финансовых операций на основе их состояния и даты.

Проект включает следующие функции:
1. **get_operations**: Читает JSON-файл и возвращает список операций, исключая пустые словари.
2. **sort_day_time**: Сортирует список операций по дате и времени в порядке убывания.
3. **hide_symbols**: Маскирует номера счетов в списке операций.
4. **sorted_executed**: Фильтрует список операций, чтобы включить только те, у которых состояние "EXECUTED".
