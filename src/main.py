from func import hide_symbols


def main():
    """
    main operations 12
    """
    operation = hide_symbols()
    # print(operation[0:])
    for i in operation[:5]:
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
