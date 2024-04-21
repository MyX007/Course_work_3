from funcs.format_transactions import format_transactions

def test_lenght_transactions_list():
    """
    Проверяет чтобы длина списка транзакций была равна 5
    """
    assert len(format_transactions()) == 5



