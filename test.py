from wcferry import Wcf, WxMsg

wcf = Wcf()

data = wcf.get_friends()

print(data)


def find_wxid_by_remark(data, target_remark):
    for item in data:
        if item['name'] == target_remark:
            return item['wxid']
    return None


target_remark = "A8"
result = find_wxid_by_remark(data, target_remark)
print(result)
# # wxid_ff3jpzvpmasy22   孙蓓蓓
# wxid_9ciybqebvucb22 A4
# wxid_cmdsn13aobh822 A8

# inspirit = ["知识改变命运，学习成就未来。",
#             "每天进步一点点，积累成就大梦想。",
#             "学习是种投资，未来会加倍回报你。",
#             "不怕慢，只怕站。坚持就是胜利。",
#             "书本是智慧的钥匙，开启无限可能。",
#             "学习如逆水行舟，不进则退。",
#             "努力不一定成功，但放弃一定失败。",
#             "学无止境，勇攀高峰。",
#             "今日的努力，明日的实力。",
#             "学习让你与众不同，知识使你独一无二。",
#             "梦想在课堂上起航，每一刻都是新的起点。",
#             "学习不仅是积累知识，更是点燃激情的火花。",
#             "每一堂课都是通往智慧殿堂的阶梯，勇敢迈步吧！",
#             "书本是打开世界的钥匙，每一页都藏着无限可能。",
#             "不要害怕挑战，因为每一次努力都在塑造更好的你。",
#             "教室里的每一分钟，都是为未来铺路的宝贵时光。",
#             "知识就像星辰，点亮你前行的路，照亮你的梦。",
#             "今天的努力，是为了明天站在更高的山峰俯瞰世界。",
#             "保持好奇，保持热情，课堂是你探索未知的乐园。",
#             "记住，最远的距离不是从这到那，而是从说到做。"
#             ]
#
# print(len(inspirit))
# print(inspirit[19])
