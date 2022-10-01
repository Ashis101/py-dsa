import threading

# when threads working on  single variable  

x=0

def p1(lock):
    global x

    while x != 100000:
        lock.aquire()
        x+=1
        lock.release()


t1=threading.Thread(target=p1,args=(threading.Lock(),))

