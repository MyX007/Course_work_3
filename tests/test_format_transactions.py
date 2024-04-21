from funcs.format_transactions import format_transactions
from funcs.last_5_transactions import get_operations_list
def test_lenght_transactions_list():
    assert len(format_transactions()) == 5



