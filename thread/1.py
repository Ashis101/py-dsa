import threading
import time


def p1(name,ti):
    i=0
    while i <= ti:
        if i % 2 == 0:
            time.sleep(2)
        print("p1:",name)
        i+=1
def p2(name,ti):
    j=0
    while j <= ti:
        if j % 2 == 1:
            time.sleep(2)
        print("p2:",name)
        j+=1


if __name__=="__main__":
    try:
        t1=threading.Thread(target=p1,args=("ashis",20))
        t2=threading.Thread(target=p2,args=("banerjee",20))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
    except:
        print("Problem in threading")
