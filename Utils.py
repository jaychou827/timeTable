import csv
from datetime import datetime


def read_csv_to_dict(file_path):
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        data = [row for row in reader]
    return data


def get_welcome_msg(name):
    current_time = datetime.now().hour

    if 5 <= current_time < 9:
        welcome = "早上好"
    elif 9 <= current_time < 14:
        welcome = "中午好"
    elif 14 <= current_time < 18:
        welcome = "下午好"
    elif 18 <= current_time < 21:
        welcome = "晚上好"
    else:
        welcome = "夜深了，早点休息哦"

    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    welcome_msg = "🌟" + welcome + f"！\n👑{name}👑 \n✨我是您的私人管家A8 \n🎀现在是：" + now_time + "\n💓我会在您每节课上课之前15分钟\n🌷发信息提醒您！"

    return welcome_msg


def get_good_bye_msg(name):
    current_time = datetime.now().hour

    good_bye = "夜深了，早些休息哦！"

    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    welcome_msg = "🌟" + good_bye + f"！\n👑{name}👑 \n✨您的私人管家A8下线啦！🎀"

    return welcome_msg
