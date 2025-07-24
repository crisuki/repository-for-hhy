def is_prime(a):
    for i in range (2,int(a**0.5+1)):
        if a%i==0:
            return 1
    return 0 

a=int(input('请输入一个数字：'))
if is_prime(a):
    print(a,'不是质数')   
else :
    print(a,'是质数')
    
'''
参考答案：
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 测试函数
number = 29
if is_prime(number):
    print(f"{number} 是质数")
else:
    print(f"{number} 不是质数")
'''