def Fibonacci(n):
    i=1
    x=1
    y=1
    z=0
    print(x)
    print(y)
    while i<=n:
        if z<x and z<y : 
            z=x+y
            print(z)
        elif x<=y and x<z :
            x=y+z
            print(x)
        else :
            y=x+z
            print (y)
        i+=1
            
Fibonacci(int(input('请输入斐波那契数列项数：')))

'''
参考答案：
def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

n = 10  # 打印前10项
print(fibonacci(n))
'''