#!/bin/env/python

import socket
import struct
import os
import time

# create icmp socket
def create_socket():
    proto = 'ICMP'
    try:
        icmp_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
        print (icmp_socket)
    except Exception as e:
        raise e
    return icmp_socket


def checksum(source_string):
    """
    I'm not too confident that this is right but testing seems
    to suggest that it gives the same answers as in_cksum in ping.c
    """
    source_string=str(source_string)
    sum = 0
    countTo = (len(source_string)/2)*2
    count = 0
    while count<countTo:
        thisVal = ord(source_string[count + 1])*256 + ord(source_string[count])
        sum = sum + thisVal
        sum = sum & 0xffffffff # Necessary?
        count = count + 2

    if countTo<len(source_string):
        sum = sum + ord(source_string[len(source_string) - 1])
        sum = sum & 0xffffffff # Necessary?

    sum = (sum >> 16)  +  (sum & 0xffff)
    sum = sum + (sum >> 16)
    answer = ~sum
    answer = answer & 0xffff

    # Swap bytes. Bugger me if I know why.
    answer = answer >> 8 | (answer << 8 & 0xff00)

    return answer

def uchar_checksum(data, byteorder='big'):
    '''
    char_checksum 按字节计算校验和。每个字节被翻译为无符号整数
    @param data: 字节串
    @param byteorder: 大/小端
    '''
    length = len(data)
    checksum = 0
    for i in range(0, length):
        checksum += int.from_bytes(data[i:i+1], byteorder, signed=False)
        checksum &= 0xFF # 强制截断
    return checksum

# generate icmp data
def generate_pkg():
   ## ICMP pkg header
   pkt_id = os.getpid()
   ident = 0
   pkg_header_pre = struct.pack("!BBHHH", 8, 0, 0, pkt_id, ident)
   payload = struct.pack("d", time.time())
   pkgheader_check = uchar_checksum(pkg_header_pre+payload)
   pkg_header = struct.pack("!BBHHH", 8, 0, pkgheader_check, pkt_id, ident)
   pkg = pkg_header+payload
   return pkg


def send_pkg(icmp_socket,pkt,dst_addr):
    icmp_socket.sendto(pkt,dst_addr)


if __name__ == '__main__':
    icmp_socket = create_socket()
    pkt = generate_pkg()
    dst_addr = '127.0.0.1'
    real_dst_addr = (dst_addr, 6000)
    send_pkg(icmp_socket, pkt, real_dst_addr)