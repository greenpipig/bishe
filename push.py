#!/usr/bin/env python3
import os
from tool import bea_bar
import time
import urllib.request
import threading
from time import sleep

# 性能测试页面
# PERF_TEST_URL = "http://127.0.0.1:5000/"

# 配置:模拟运行状态
THREAD_NUM = 20  # 并发线程总数
ONE_WORKER_NUM = 100  # 每个线程的循环次数
LOOP_SLEEP = 0.01  # 每次请求时间间隔(秒)

# 出错数
ERROR_NUM = 0


# 具体的处理函数，负责处理单个任务
def doWork(index, url1):
    t = threading.currentThread()
    try:
        html = urllib.request.urlopen(url1).read()
    except Exception as e:
        print(e)
        global ERROR_NUM
        ERROR_NUM += 1


def working(url):
    t = threading.currentThread()
    # print( "["+t.name+"] Sub Thread Begin" )
    i = 0
    while i < ONE_WORKER_NUM:
        i += 1
        doWork(i, url)
        sleep(LOOP_SLEEP)
    # print( "["+t.name+"] Sub Thread End" )


def more_thread(ip, port):
    testurl = "http://" + ip + ":" + port + "/"
    t1 = time.time()
    Threads = []
    # 创建线程
    for i in range(THREAD_NUM):
        print(bea_bar(i, THREAD_NUM))
        t = threading.Thread(target=working(testurl), name="T" + str(i))
        t.setDaemon(True)
        Threads.append(t)
        os.system('cls')
    for t in Threads:
        t.start()
    for t in Threads:
        t.join()
    print("thread end")
    t2 = time.time()
    print("========================================")
    print("URL:", testurl)
    print("任务数量:", THREAD_NUM, "*", ONE_WORKER_NUM, "=", THREAD_NUM * ONE_WORKER_NUM)
    print("总耗时(秒):", t2 - t1)
    print("每次请求耗时(秒):", (t2 - t1) / (THREAD_NUM * ONE_WORKER_NUM))
    print("每秒承载请求数:", 1 / ((t2 - t1) / (THREAD_NUM * ONE_WORKER_NUM)))
    print("错误数量:", ERROR_NUM)


if __name__ == '__main__':
    more_thread('127.0.0.1', '5000')
