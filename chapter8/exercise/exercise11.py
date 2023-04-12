def send_messages(msgs: list[str], send_list: list[str]):
    while msgs:
        msg = msgs.pop()
        print(msg)
        send_list.append(msg)


msgs = ['esr', 'test', 'abc']
send_list = []
send_messages(msgs[:], send_list)
print(msgs)
print(send_list)
