import json

def get_operations_list():
    """
    Считывает данные с файла operations.json и возвращает список последних исполненных операций
    """
    with open("../src/operations.json", encoding="utf-8") as file:
        operations_list = json.load(file)
        last_executed_operations = []
        while len(last_executed_operations) != 5:
            for i in operations_list[::-1]:
                if i['state'] == 'EXECUTED':
                    last_executed_operations.append(i)
                else:
                    pass
                if len(last_executed_operations) == 5:
                    break
        return sorted(last_executed_operations, key=lambda x: x['date'], reverse=True)
