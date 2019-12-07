import udpflood
import tool

tool.surface()
choose=input("Please input your choose:")#todo 校验输入
print(choose)
if choose == 1:
    print("Now you in udpflood method")
    ip=input("Please input the ip you wanna attack")#todo 校验ip
    port=input()
    usertime=input()
    udpflood.udpfloods(ip,port,usertime)
elif choose == 2:
    #todo ddos
    input()
elif choose == 3:
    #todo cc
    input()
elif choose == 4:
    #todo DBattack
    input()
else:
    quit()