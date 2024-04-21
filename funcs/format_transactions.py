from funcs.last_5_transactions import get_operations_list
from funcs.format_requisites import format_requisites
import datetime


def format_transactions():
    """
    Преобразует последние 5 успешнных операций в формат:
    <дата перевода> <описание перевода>
    <откуда> -> <куда>
    <сумма перевода> <валюта>
    """
    transactions = []
    for i in get_operations_list():
        date = datetime.datetime.strptime(i['date'][:10], "%Y-%m-%d")

        if i["description"] == "Открытие вклада":
            transactions.append(f"{date.strftime("%d.%m.%Y")} {i['description']}\n{format_requisites()[i['id']]}\n{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}\n")
        else:
            transactions.append(f"{date.strftime("%d.%m.%Y")} {i['description']}\n{format_requisites()[i['id']]}\n{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}\n")
    return transactions


