#两种写法，第一种放在函数里面，第二种放在类里面


from threading import Thread


def thread():
    list1=[]
    for i in range(10):
        list1.append(i)
    print(list1)



if __name__ == '__main__':
    t=Thread(target=thread)
    t.start()
    for i in range(10):
        print('主线程',i)
