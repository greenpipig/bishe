# -*- coding：utf-8 -*-
import os
import re
import time

PING_RESULT = 0
NETWORK_RESULT = 0


def surface():
    print("=====================================================")
    print("                  test                       ")
    print("               press 1 in udpflood                     ")
    print("                 press 2 in ddos                      ")
    print("                  press 3 in cc")
    print("                press 4 in DBattack")
    print("=====================================================")


def getipports():
    ip = input("Please input the ip you wanna attack")  # todo 校验ip
    port = input("Please input the ip you wanna attack")  # todo 校验port
    return ip, port


def ping(ip):
    yesno = input("do you wanna check ip is useful Y/N")

    if yesno == "Y":
        result = os.system(u"ping " + ip)
        # result = os.system(u"ping www.baidu.com -n 3")
        if result == 0:
            print("network success")
        else:
            print("network down")
        return result
    elif yesno == "N":
        return
    else:
        print("input wrong please try again")
        ping(ip)


def testport(ip, port):
    # todo curl解析码
    result = os.system(u"curl " + ip + ":" + port)
    if result == 1:
        print("yes")
    else:
        print("no")


def check_ip(ipAddr):
    compile_ip = re.compile('^(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[1-9])\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)$')
    check=True
    while check:
        if compile_ip.match(ipAddr):
            print("right")
            check=False
        else:
            ipAddr = input("wrong ip please input again:")
            check=True
    return ipAddr