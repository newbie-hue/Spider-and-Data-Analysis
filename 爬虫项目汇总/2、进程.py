



from multiprocessing import Process

def func():
    list=[]
    for i in range(10):
        list.append(i)
    print(list)

if __name__ == '__main__':
    p1=Process(target=func)
    p2=Process(target=func)
    p3=Process(target=func)
    p1.start()
    p2.start()
    p3.start()
    for i in range(10):
        print('主',i)