# repository-for-hhy
学习目标：掌握python的基本用法，并在项目学习中，了解python具体的功能与应用。
知识点笔记：
一、list列表函数用法：
1。元素操作
list.append(obj)           # 在列表末尾添加一个元素。
list.extend(iterable)      # 将可迭代对象（如列表、元组）的所有元素添加到列表末尾。
list.insert(index, obj)    # 在指定位置 index 插入一个元素。
list.remove(value)         # 删除列表中第一个值等于 value 的元素。
list.pop([index])          # 删除并返回指定位置 index 的元素（默认删除最后一个元素）。
list.clear()               # 清空列表中的所有元素。
2.查找与统计
list.index(value[, start[, end]])  # 返回第一个值等于 value 的元素的索引（可指定搜索范围）。
list.count(value)                  # 统计列表中值等于 value 的元素个数。
3.排序与反转
list.sort(key=None, reverse=False)  # 对列表进行原地排序（升序或降序）。
list.reverse()                      # 反转列表中元素的顺序。
4.其他常用方法
list.copy()    # 返回列表的浅拷贝（创建新列表，但元素引用相同）。
len(list)      # 返回列表的长度（元素个数）。（注意：len() 是函数而非列表方法）

二、dict字典函数用法：
1.元素操作
dict.get(key[, default])         # 返回指定键的值，如果键不存在则返回 default（默认 None）。
dict[key] = value                # 设置键 key 的值为 value（若键不存在则创建）。
dict.setdefault(key[, default])  # 如果键存在，返回其值；否则设置为 default 并返回。
dict.update(other_dict)          # 用另一个字典的键值对更新当前字典（覆盖重复键）。
del dict[key]                    # 删除指定键的项。
dict.pop(key[, default])         # 删除并返回指定键的值，若键不存在则返回 default。
dict.popitem()                   # 删除并返回字典的最后一对键值（Python 3.7+ 有序）。
dict.clear()                     # 清空字典中的所有项。
2.查找与判断
key in dict                      # 判断字典是否包含键 key（返回布尔值）。
dict.keys()                      # 返回包含所有键的视图对象。
dict.values()                    # 返回包含所有值的视图对象。
dict.items()                     # 返回包含所有键值对的视图对象（元组形式）。
3.复制与创建
dict.copy()                      # 返回字典的浅拷贝。
dict.fromkeys(iterable[, value]) # 创建一个新字典，以 iterable 中的元素为键，值均为 value。
