from funcs.last_5_transactions import get_operations_list

def format_requisites():
    """
    Скрывает полные реквизиты отправителя/получателя и возвращает словарь с ключами, которые равны id операции
    и значениями с реквизитами этих операций
    """
    requisites = {}
    for i in get_operations_list():
        recipient = []
        requisite = []
        if 'from' in i:
            sender = []
            sender.append(i['from'])
            recipient.append(i['to'])
            for s in sender:
                if 'Счет' in s:
                    s = f"Счет **{s[-4:]}"
                    requisite.append(s)

                else:
                    s = f"{s[:-12]} {s[-12:-10]}** **** {s[-4:]}"
                    sender = s
                    requisite.append(s)

        else:
            recipient.append(i['to'])

        for r in recipient:
            if 'Счет' in r:
                r = f"Счет **{r[-4:]}"
                requisite.append(r)

            else:
               r = f"{r[:-12]} {r[-12:-10]}** **** {r[-4:]}"
               requisite.append(r)
        requisites[i['id']] = ' -> '.join(requisite)

    return requisites
