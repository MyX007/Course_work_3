from funcs import last_5_transactions

def test_lenght_transactions():
    """
    Проверяет функкцию, чтобы длина списка была равна 5
    """
    assert len(last_5_transactions.get_operations_list()) == 5

def  test_executed_status():
    """
    Проверяет наличие статуса "EXECUTED" у всех операций из списка
    """
    for i in last_5_transactions.get_operations_list():
        assert i["state"] == "EXECUTED"