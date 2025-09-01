# decorator.py - 데코레이터 : 기존 함수를 바꾸지 않고 기능을 추가할 수 있게 만드는 함수. ex) elapsed 등.

import time

# def myfunc():
#    start = time.time()
#    print('함수가 실행됩니다.')
#    end = time.time()
#    print(f'함수 수행시간 : {end-start}초')

#myfunc()

#위의 식 또는 아래 식.

def elapsed(func):   #경과시간
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print(f'함수 수행시간 : {end-start}초')
        return result
    return wrapper

def myfunc():
    print('함수가 실행됩니다.')

elapsed(myfunc)()