import func


def main():
    # Загрузка операций из файла
    operations_dict = func.get_operations("../operations.json")
    # Сортировка операций по дате и времени
    sorted_operations = func.sort_day_time(operations_dict)
    # Сортировка по выполненым(EXECUTED) операциям
    sorted_executed = func.sorted_executed(sorted_operations)
    # Маскировка номеров карт и счетов
    hide_symbols = func.hide_symbols(sorted_executed, "*", 4)

    # Вывод первых 5 операций
    for i in hide_symbols[:5]:
        if 'from' in i:
            print(f"""{i['date'][:10]} {i['description']}
{i['from']} -> {i['to']}
{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}
""")
        else:
            print(f"""{i['date'][:10]} {i['description']}
{i['description']} -> {i['to']}
{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}
""")

if __name__ == "__main__":
    main()
