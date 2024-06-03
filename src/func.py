import json
from datetime import datetime


def get_operations(operations):
    """
    Читает JSON-файл, извлекает список операций и удаляет из него пустые словари.
    :operations: Путь к файлу с операциями в формате JSON
    :return: Список операций без пустых словарей
    """
    with open(operations, 'r', encoding='utf-8') as file:
        data = json.load(file)
    operations_list = [operation for operation in data if operation]
    return operations_list


def sort_day_time(operations):
    """
    Изменяет формат времени и сортирует список по дате/времени.

    :return: Отсортированный список операций
    """
    for operation in operations:
        operation['date'] = datetime.fromisoformat(operation['date']).strftime("%d.%m.%Y %H:%M:%S")

    operations.sort(
        key=lambda operation: datetime.strptime(operation['date'], "%d.%m.%Y %H:%M:%S"), reverse=True
    )
    return operations

def sorted_executed(operations):
    executed = []
    for i in operations:
        if i['state'] == 'EXECUTED':
            executed.append(i)
    return executed

def hide_symbols(last_operations, hide="*", step=4):
    """
    Маскируем номера счетов
    """
    for operation in last_operations:
        if 'from' in operation:
            card = operation['from']
            from_check = card.split()
            if len(from_check[-1]) == 16:
                card_numb = from_check[-1][:6] + (hide * 6) + from_check[-1][-4:]
                hide_card = ' '.join(card_numb[i:i + step] for i in range(0, len(card_numb), step))
                from_check[-1] = hide_card
                operation['from'] = ' '.join(from_check)
            if len(from_check[-1]) == 20:
                hide_account = (hide*2) + from_check[-1][-4:]
                from_check[-1] = hide_account
                operation['from'] = ' '.join(from_check)
        if 'to' in operation:
            account = operation['to']
            from_check = account.split()
            if len(from_check[-1]) == 16:
                card_numb = from_check[-1][:6] + (hide * 6) + from_check[-1][-4:]
                hide_card = ' '.join(card_numb[i:i + step] for i in range(0, len(card_numb), step))
                from_check[-1] = hide_card
                operation['to'] = ' '.join(from_check)
            if len(from_check[-1]) == 20:
                hide_account = (hide * 2) + from_check[-1][-4:]
                from_check[-1] = hide_account
                operation['to'] = ' '.join(from_check)

    return last_operations

