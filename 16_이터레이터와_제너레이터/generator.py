# generator2.py

import time

def longtime_jop():
    print('jop start')
    time.sleep(1)
    return "done"

# list_jop = [longtime_jop() for i in range(5)]
list_jop = (longtime_jop() for i in range(5))  # 제너레이터 표현식
print(next(list_jop))