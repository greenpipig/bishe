import random
import threading
import time


def random_ip():
    ip = ".".join(map(str, (random.randint(0, 255) for i in range(4))))
    return ip


def randomPort():
    port = random.randint(1000, 10000)
    return port


def run(func, thread_num, one_work_num, dst_ip, dst_port):
    # 创建数组存放线程
    threads = []
    try:
        # 创建线程
        # 针对函数创建线程
        for i in range(thread_num):
            if dst_port == 0:
                t = threading.Thread(target=func, args=(dst_ip, one_work_num))
            else:
                t = threading.Thread(target=func, args=(dst_ip, dst_port, one_work_num))
            # 把创建的线程加入线程组
            threads.append(t)
    except Exception as e:
        print(e)
    try:
        # 启动线程
        for thread in threads:
            thread.setDaemon(True)
            thread.start()
            # 等待所有线程结束
        for thread in threads:
            thread.join()
    except Exception as e:
        print(e)


def start_attack(func, thread_num, one_work_num, dst_ip, dst_port):
    # 创建十个线程每个线程运行1000次
    t1 = time.time()
    run(func, thread_num, one_work_num, dst_ip, dst_port)
    t2 = time.time()
    print("任务数量:", thread_num, "*", one_work_num, "=", thread_num * one_work_num)
    print("总耗时(秒):", t2 - t1)
    print("每次请求耗时(秒):", (t2 - t1) / (thread_num * one_work_num))
    print("每秒承载请求数:", 1 / ((t2 - t1) / (thread_num * one_work_num)))
