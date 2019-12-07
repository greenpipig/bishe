def surface():
    print("=====================================================")
    print("                  恶意流量生成器                       ")
    print("               press 1 in udpflood                     ")
    print("                 press 2 in ddos                      ")
    print("                  press 3 in cc")
    print("                press 4 in DBattack")
    print("=====================================================")

def getipport():
    ip = input("Please input the ip you wanna attack")  # todo 校验ip
    port = input("Please input the ip you wanna attack") #todo 校验port
    return ip,port