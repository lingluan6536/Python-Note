# 装饰器
# 目标：将凤姐整容成范冰冰，并保留其凤姐的身份(即相关部门看到她时会认为她是凤姐而不是 范冰冰)
# 实现方法： ①将被装饰函数作为装饰器的内部调用函数，并在装饰函数中添加额外的功能，
#           ②将装饰后的函数名称改为被装饰的函数的函数名
#           ③更改其他函数的相关属性

# 以下是错误做法：

# def say_hello():
#     print("Hello")
#
#
# def say_more():
#     say_hello() #被装饰的函数
#     print("Nice to meet you") #装饰
#
#
# say_hello = say_more
#
# say_hello()

# 错误原因： 造成无限迭代

# 改进如下： 对函数添加两层函数包裹，通过返回函数入口的方式，隔离迭代

# def say_hello():
#     print("Hello")
#
# def decorator(func):
#     def say_more():
#         func() #被装饰的函数
#         print("Nice to meet you") #装饰
#     return say_more
#
# say_hello = decorator(say_hello)
#
# say_hello()

# 弊端： 如果函数带有参数则， 装饰器也需要相应的添加相当的参数，对可变参数函数不友好

# 改进如下：

# def say_hello ():
#     print("Hello")
#
#
# def get_sum(a, b):
#     print(f'a + b = {a+b} ')
#
#
# def decorator(func):
#     def say_more(*args, **kwargs):
#         func(*args, **kwargs) #被装饰的函数
#         print("Nice to meet you") #装饰
#     return say_more
#
#
# say_hello = decorator(say_hello)
# get_sum = decorator(get_sum)
#
# say_hello()
#

# 一种简写的方法   say_hello = decorator(say_hello) 的方法　@decorator ：

# def decorator(func):
#     def wrapper(*args, **kwargs):
#         func(*args, **kwargs) #被装饰的函数
#         print("Nice to meet you") #装饰
#     return wrapper
#
# @decorator
# def say_hello():
#     print("Hello")
#
#
# say_hello()
# print(say_hello)

# 弊端： 对带有返回值的函数，则返回值消失,  以下示例返回值为None


# def decorator(func):
#     def wrapper(*args, **kwargs):
#         func(*args, **kwargs) #被装饰的函数
#         print("Nice to meet you") #装饰
#     return wrapper
#
#
# @decorator
# def get_sum(a, b):
#     return a + b
#
#
# print(f'sum = {get_sum(1, 2)}')


# 改进：加入return 代码作用于被装饰函数 得到返回值

# def decorator(func):
#     def wrapper(*args, **kwargs):
#         r = func(*args, **kwargs) #被装饰的函数
#         print("Nice to meet you") #装饰
#         return r
#     return wrapper
#
#
# @decorator
# def get_sum(a, b):
#     return a + b
#
#
# print(f'sum = {get_sum(1, 2)}')


# 缺陷， 如果print(get_sum) 得到的函数名仍为 decorator
# 改进 利用@functool 装饰器修改函数名
# 如下：


# import functools
#
#
# def decorator(func):
#       @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         r = func(*args, **kwargs)  #被装饰的函数
#         print("Nice to meet you")  #装饰
#         return r
#     return wrapper
#
#
# @decorator
# def get_sum(a, b):
#     return a + b
#
# #print(decorator)
# print(get_sum)
# print(f'sum = {get_sum(1, 2)}')


