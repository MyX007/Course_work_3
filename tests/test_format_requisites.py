from funcs.format_requisites import format_requisites
from funcs.last_5_transactions import get_operations_list

def test_lenght_requisites_list():
    """
    Проверяет чтобы длиная списка реквизитов была равна 5
    """
    assert len(format_requisites()) == 5

def test_id():
    """
    Проверяет чтобы все ключи 'id' были взяты из
    списка последних 5 успешных операций
    """
    for i in get_operations_list():
        assert i['id'] in format_requisites()