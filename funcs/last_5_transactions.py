import json

def get_operations_list():
    """
    Считывает данные с файла operations.json и возвращает список последних исполненных операций
    """
    with open("/home/vladimir/PycharmProjects/Course_work_3/src/operations.json") as file:
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
        return last_executed_operations
