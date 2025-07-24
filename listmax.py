numlist=[1,10,25,30,65,12,22,53]
max=numlist[0]
for i in range(0,len(numlist)):
    if numlist[i]>max:
        max=numlist[i]
print('最大的数字是：',max)

'''
参考答案：
# 定义一个列表
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# 使用 max() 函数找到最大值
max_value = max(numbers)

# 使用 min() 函数找到最小值
min_value = min(numbers)

# 输出结果
print("列表中的最大值是:", max_value)
print("列表中的最小值是:", min_value)
'''