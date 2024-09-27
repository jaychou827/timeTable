import schedule
import time
from datetime import datetime, timedelta
import Utils
from wcferry import Wcf, WxMsg
import random
from threading import Thread
from queue import Empty
import threading

wcf = Wcf()
users = {}

datas = Utils.read_csv_to_dict("users.csv")

for data in datas:
    users[data[7]] = data[6]

for receiver in users.keys():
    welcome_msg = Utils.get_welcome_msg(users[receiver])

    wcf.send_text(msg=welcome_msg, receiver=receiver)


def auto():
    inspirit = ["知识改变命运，学习成就未来。",
                "每天进步一点点，积累成就大梦想。",
                "学习是种投资，未来会加倍回报你。",
                "不怕慢，只怕站。坚持就是胜利。",
                "书本是智慧的钥匙，开启无限可能。",
                "学习如逆水行舟，不进则退。",
                "努力不一定成功，但放弃一定失败。",
                "学无止境，勇攀高峰。",
                "今日的努力，明日的实力。",
                "学习让你与众不同，知识使你独一无二。",
                "梦想在课堂上起航，每一刻都是新的起点。",
                "学习不仅是积累知识，更是点燃激情的火花。",
                "每一堂课都是通往智慧殿堂的阶梯，勇敢迈步吧！",
                "书本是打开世界的钥匙，每一页都藏着无限可能。",
                "不要害怕挑战，因为每一次努力都在塑造更好的你。",
                "教室里的每一分钟，都是为未来铺路的宝贵时光。",
                "知识就像星辰，点亮你前行的路，照亮你的梦。",
                "今天的努力，是为了明天站在更高的山峰俯瞰世界。",
                "保持好奇，保持热情，课堂是你探索未知的乐园。",
                "记住，最远的距离不是从这到那，而是从说到做。"
                ]

    def job(start_time1, course_name1, room1, end_date1, end_time1, name1, receiver1):
        msg = f"""    👑{name1}请上课👑
        🌟课程：💎{course_name1}💎
        🌸教室：💎{room1}💎
        🎀上课：💎{start_time1}💎
        🌷下课：💎{end_time1}💎
        ✨记得带上书本和笔记本哦！
        💓{inspirit[random.randint(0, 19)]}"""
        wcf.send_text(msg=msg, receiver=receiver1)

    datas = Utils.read_csv_to_dict("users.csv")

    # 设置学期开始日期
    semester_start_date = "2024-09-01"

    for data in datas:
        weekday = int(data[0])
        start_time = data[3]
        end_week = int(data[5])
        course_name = data[1]
        room = data[2]
        name = data[6]
        receiver_back = data[7]

        # 计算结束日期
        end_date = (datetime.strptime(semester_start_date, "%Y-%m-%d") + timedelta(days=(end_week - 1) * 7)).strftime(
            "%Y-%m-%d")
        end_time = data[4]

        # 提前15分钟计算开始时间
        start_time_obj = datetime.strptime(start_time, "%H:%M")
        start_time_obj = start_time_obj - timedelta(minutes=15)
        start_time = start_time_obj.strftime("%H:%M")

        start_Time = data[3]

        # 检查是否已经过了结束日期
        if datetime.now().date() < datetime.strptime(end_date, "%Y-%m-%d").date():
            if datetime.now().weekday() == weekday - 1:
                schedule.every().day.at(start_time).do(job, start_Time, course_name, room, end_date, end_time, name,
                                                       receiver_back)

    while True:
        schedule.run_pending()
        time.sleep(1)


def manu():
    T_datas = Utils.read_csv_to_dict("table.csv")
    table = {}
    for T_data in T_datas:
        table[T_data[1]] = T_data[0]

    def processMsg(msg: WxMsg):
        if not msg.from_group():
            if msg.sender in table.keys():
                if msg.content == "课表":
                    wcf.forward_msg(id=table[msg.sender], receiver=msg.sender)

    # 启用接收消息功能
    def enableReceivingMsg():
        # 内部线程函数，用于处理接收到的消息
        def innerWcFerryProcessMsg():
            while wcf.is_receiving_msg():
                try:
                    msg = wcf.get_msg()
                    processMsg(msg)
                except Empty:
                    continue
                except Exception as e:
                    print(f"ERROR: {e}")

        # 启用接收消息功能并启动线程
        wcf.enable_receiving_msg()
        Thread(target=innerWcFerryProcessMsg, name="ListenMessageThread", daemon=True).start()

    # 启用接收消息功能
    enableReceivingMsg()

    # 保持程序运行
    wcf.keep_running()


# 创建线程对象t1和t2
t1 = threading.Thread(target=auto)
t2 = threading.Thread(target=manu)

# 启动线程
t1.start()
t2.start()

# 等待线程执行完成
t1.join()
t2.join()
