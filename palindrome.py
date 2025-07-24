is_palindrome=True
s=input('请输入一个字符串')

for i in range(0,len(s)//2):
    if s[i]!=s[len(s)-i-1]:
        is_palindrome=False
        break

if is_palindrome:
    print(s+'是回文')
else :
    print(s+'不是回文')
    
'''
参考答案：
def is_palindrome(s):
    # 将字符串转换为小写并移除空格
    s = s.lower().replace(" ", "")
    # 比较字符串和它的反转
    return s == s[::-1]

# 测试
test_string = "A man a plan a canal Panama"
print(is_palindrome(test_string))'''

