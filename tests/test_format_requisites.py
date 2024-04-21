from funcs.format_requisites import format_requisites
from funcs.last_5_transactions import get_operations_list

def test_lenght_requisites_list():
    assert len(format_requisites()) == 5

def test_id():
    for i in get_operations_list():
        assert i['id'] in format_requisites()