import json
from datetime import datetime


def get_operations():
    with open("../operations.json", 'r') as file:
        data = json.load(file)
    operations_list = data
    operations_list.remove({})
    return operations_list


def sort_by_day():
    operations = get_operations()
    # print(operations[0]['date'])
    for operation in operations:
        operation['date'] = datetime.fromisoformat(operation['date']).strftime("%d.%m.%Y %H:%M:%S")

    operations = sorted(
        operations,
        key=lambda day_time: datetime.strptime(day_time['date'], "%d.%m.%Y %H:%M:%S"), reverse=True
    )
    return operations


last_operations = sort_by_day()


def last_five_executed():
    last_five = 0
    last_five_operations = []
    for i in last_operations:
        if last_five == 5:
            return last_five_operations
        if i['state'] == 'EXECUTED':
            # print(i)
            last_five_operations.append(i)
            last_five += 1


# last_five_executed()

def hide_symbols():
    last_operations = last_five_executed()
    hide = "*"
    step = 4
    for operation in last_operations:
        if 'from' in operation:
            card = operation['from']
            from_check = card.split()
            # print(s2[:-1], len(s2[-1]), s2[-1])
            if len(from_check[-1]) == 16:
                card_numb = from_check[-1][:6] + (hide * 6) + from_check[-1][-4:]
                hide_card = ' '.join(card_numb[i:i + step] for i in range(0, len(card_numb), step))
                from_check[-1] = hide_card
                operation['from'] = ' '.join(from_check)
                # print(s2[0:-1])
                # print(s2)
                # print(hide_card)
                # print(operation['from'])
            if len(from_check[-1]) == 20:
                hide_account = (hide*2) + from_check[-1][-4:]
                from_check[-1] = hide_account
                operation['from'] = ' '.join(from_check)
                # print(operation['from'])
        if 'to' in operation:
            account = operation['to']
            from_check = account.split()
            # print(s2[:-1], len(s2[-1]), s2[-1])
            if len(from_check[-1]) == 16:
                card_numb = from_check[-1][:6] + (hide * 6) + from_check[-1][-4:]
                hide_card = ' '.join(card_numb[i:i + step] for i in range(0, len(card_numb), step))
                from_check[-1] = hide_card
                operation['to'] = ' '.join(from_check)
                # print(s2[0:-1])
                # print(s2)
                # print(hide_card)
                # print(operation['from'])
            if len(from_check[-1]) == 20:
                hide_account = (hide * 2) + from_check[-1][-4:]
                from_check[-1] = hide_account
                operation['to'] = ' '.join(from_check)
                # print(operation['from'])

    return last_operations

# last_five_transaction = hide_symbols()
#
# for i in last_five_transaction:
#     print(i)
