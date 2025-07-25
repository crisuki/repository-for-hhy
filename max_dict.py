dict={'a':10,'b':20,'c':15}
max_key=max(dict,key=dict.get)
max_value=dict[max_key]
print(f'最大的值是{max_value}')