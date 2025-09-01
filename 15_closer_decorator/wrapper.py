# wrapper.py

def mul(m):
    def wrapper(n):
        return m * n
    return wrapper

    # def  mul(self, n):
    def __call__(self, n):
        return n *self.m
    
if __name__ == '__main__':
    #mul3 = mul(3)    # 호출하면 def mul(m):의 m에 3, 5가 들어감.
    #mul5 = mul(5)


    #print(mul3(10))    # 호출하면 def wrapper(n):의 n에 10이 들어감.
    #print(mul5(10))
    
    print(mul(3)(10))   # 3,5는 m 10은 n (위의 방식을 간단히 정리한 것.)
    print(mul(5)(10))
