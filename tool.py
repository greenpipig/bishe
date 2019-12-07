import os
import time

PING_RESULT = 0
NETWORK_RESULT = 0


def surface():
    print("=====================================================")
    print("                  恶意流量生成器                       ")
    print("               press 1 in udpflood                     ")
    print("                 press 2 in ddos                      ")
    print("                  press 3 in cc")
    print("                press 4 in DBattack")
    print("=====================================================")


def getipports():
    ip = input("Please input the ip you wanna attack")  # todo 校验ip
    port = input("Please input the ip you wanna attack")  # todo 校验port
    return ip, port


def disableNetwork():
    ''' disable network card '''
    result = os.system(u"netsh interface set interface 以太网 disable")
    if result == 1:
        print("disable network card failed")
    else:
        print("disable network card successfully")


def ping(ip):
    ''' ping 主备网络 '''
    result = os.system(u"ping "+ip)
    # result = os.system(u"ping www.baidu.com -n 3")
    if result == 0:
        print("A网正常")
    else:
        print("网络故障")
    return result


def testping(ip):
    PING_RESULT = ping(ip)
    if PING_RESULT == 0:
        time.sleep(20)
    else:
        disableNetwork()
        time.sleep(10)


def testport(ip, port):
    #todo 解析码
    result = os.system(u"curl " + ip+":" + port)
    if result== 1:
        print("yes")
    else:
        print("no")