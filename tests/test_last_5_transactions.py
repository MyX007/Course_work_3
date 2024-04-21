from funcs import last_5_transactions

def test_lenght_transactions():
    assert len(last_5_transactions.get_operations_list()) == 5

def  test_executed_status():
    for i in last_5_transactions.get_operations_list():
        assert i["state"] == "EXECUTED"