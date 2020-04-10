# -*- coding：utf-8 -*-
import os
import re
import time

PING_RESULT = 0
NETWORK_RESULT = 0


def surface():
    print("=" * 40)
    print("test                       ")
    print("press 1 in udp-flood                     ")
    print("press 2 in http-push                      ")
    print("press 3 in syn-flood")
    print("press 4 in syn&ack-flood")
    print("=" * 40)


def get_ip_ports():
    ip = input("Please input the ip you wanna attack")  # todo 校验ip
    port = input("Please input the ip you wanna attack")  # todo 校验port
    return ip, port


def ping(ip):
    yesno = input("do you wanna check ip is useful Y/N:")

    if yesno == "Y":
        result = os.system(u"ping -c 1 -w 1 " + ip)
        # result = os.system(u"ping www.baidu.com -n 3")
        if result == 0:
            print("network success")
        else:
            print("network down")
        return result
    elif yesno == "N":
        return
    else:
        print("input wrong please try again:")
        ping(ip)


def test_port(ip, port):
    # todo curl解析码
    result = os.system(u"curl " + ip + ":" + port)
    if result == 0:
        print("yes")
    else:
        print("no")


def check_ip(ip_addr):
    compile_ip = re.compile(
        '^(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[1-9])\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)$')
    check = True
    while check:
        if compile_ip.match(ip_addr):
            print("right")
            check = False
        else:
            ip_addr = input("wrong ip please input again:")
            check = True
    return ip_addr


def bea_bar(now, num):
    bar1 = ""
    for i in range(0, now):
        bar1 = bar1 + '#'
        i += 1

    bar2 = ""
    for j in range(0, num - now):
        bar2 = bar2 + ' '
        j += 1
    bar = bar1 + bar2 + "进度条" + str((now / num) * 100) + "%"
    return bar


if __name__ == '__main__':
    ping('127.0.0.1')
