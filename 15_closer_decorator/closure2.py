# closure.py

class Mul:
    def __init__(self, m):    #초기값 설정
        self.m = m

    # def  mul(self, n):
    def __call__(self, n):
        return n *self.m
    
if __name__ == '__main__':
    mul3 = Mul(3)
    mul5 = Mul(5)

# print(mul3.mul(10))
# print(mul5.mul(10))

print(mul3(10))
print(mul5(10))
