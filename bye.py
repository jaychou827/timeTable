import Utils
from wcferry import Wcf, WxMsg

wcf = Wcf()

users = {}

datas = Utils.read_csv_to_dict("users.csv")

for data in datas:
    users[data[7]] = data[6]

for receiver in users.keys():
    welcome_msg = Utils.get_good_bye_msg(users[receiver])

    wcf.send_text(msg=welcome_msg, receiver=receiver)
