import json

def get_operations_list():
    """
    Считывает данные с файла operations.json и возвращает список последних исполненных операций
    """
    with open("../src/operations.json", encoding="utf-8") as file:
        operations_list = json.load(file)
        last_executed_operations = []
        sorted_ops_list = sorted(operations_list, key=lambda x: x.get('date', ''), reverse=True)
        while len(last_executed_operations) != 5:
            for i in sorted_ops_list:

                if i['state'] == 'EXECUTED':
                    last_executed_operations.append(i)
                else:
                    pass
                if len(last_executed_operations) == 5:
                    break
        return last_executed_operations
