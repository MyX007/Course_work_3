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
            sender.append(i['from'].split(" "))
            recipient.append(i['to'].split(" "))
            for s in sender:
                if s[0] == "Счет":
                    s[1] = f"**{s[1][-4:]}"
                    requisite.append(' '.join(s))

                else:
                    s[1] = f"{s[1][:4]} {s[1][5:7]}** **** {s[1][-4:]}"
                    sender = ' '.join(s)
                    requisite.append(' '.join(s))

        else:
            recipient.append(i['to'].split(" "))

        for r in recipient:
            if r[0] == "Счет":
                r[1] = f"**{r[1][-4:]}"
                requisite.append(' '.join(r))

            else:
               r[1] = f"{r[1][:4]} {r[1][5:7]}** **** {r[1][-4:]}"
               requisite.append(' '.join(r))
        requisites[i['id']] = ' -> '.join(requisite)

    return requisites
