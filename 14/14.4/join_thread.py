import threading

def action(max):
    for i in range(max):
        print(threading.current_thread().name + " " + str(i))


# 启动子线程
threading.Thread(target=action, args=(100,), name="新线程").start()
for i in range(100):
    if i == 20:
        jt = threading.Thread(target=action, args=(100,), name="被join的线程")
        jt.start()
        jt.join()
    print(threading.current_thread().name + " " + str(i))
