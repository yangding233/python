
# print("hello world")
#
# # print("hello world")
#
# a = 100
# print("the number of a:" ,a)
#
# a = a - 10
#
# print("the number of a:" ,a)
# # ctrl + d 复制当前行代码
#
#
# #type()变量存储的数据类型信息
#
# a_type = type(a)
# name_type = type("杨家和")
# print("the type of a:" ,a_type)
# print("the type of name:" ,name_type)
#
# # 数据类型转换！！！
#
# num_str = str(11)
# print(type(num_str) ,num_str)
#
# float_str = str(11.345)
# print(type(float_str) ,float_str)
#
# # 将字符串转换为数字
#
# num = int("11")
# print(type(num) ,num)
#
# num2 = float("11.345")
# print(type(num2) ,num2)
#
# # num3 = int("只因你太美")   错误示范，转换要符合类型
# # print(type(num3) ,num3)
#
# #算数运算符
#
# print("1 + 1 =", 1 + 1)
# print("2 - 1 =", 2 - 1)
# print("3 * 3 =", 3 * 3)
# print("4 / 2 =", 4 / 2)
# print("11 // 2 =", 11 // 2)  #整除运算符
# print("11 % 2 =", 11 % 2)    #取余运算符
# print("10 ** 2 =", 10 ** 2)  #指数运算符
#
# #多种字符串接受方式
# name00 = '程序员'
# name01 = "程序员"
# name02 = """程序员"""
#
# # "\"  转义字符\ 能够解除后面符号的效用
#
# # 字符串字面量之间的拼接  注：无法和非字符串类型进行拼接
#
# name000 = "程序员"
# address = "china"
# print("i am " + name000 + ", i am in " + address )
#
# # 通过占位的形式，完成拼接
# name = "程序员"
#
# #字符串格式化
#
# # % 表示：我要占位
# #s 表示：将变量变成字符串放入占位的地方 注意，这里是将数字转化为字符串放入
# # %d ：将内容转化为整数，放入占位位置
# # %f ： 将内容换成浮点型，放入占位位置
#
# num3 = 10
# num4 = 20
# message = "the number is %s and %s" % (num3 , num4)
# print(message)
#
# #格式化的精度控制
# # m.n ： m控制宽度，要求时数字（很少使用），设置宽度小于数字自身，不生效
# #       .n控制小数点精度，要求是数字，会进行小数的四舍五入
# # #eg： %5d 含义：将整数的输出宽度控制为5位。
# # 示例：数字 11使用 %5d格式化后，结果为 ␣␣␣11（其中␣代表空格）。即用三个空格在左侧填充，以补足5位的宽度。
# #
# # %5.2f 含义：将浮点数的输出宽度控制为5位，并将小数点后的精度设置为2位（小数部分限制2位，会进行四舍五入）。注意：小数点本身和小数部分都计入总宽度。
# # 示例：数字 11.345使用 %7.2f格式化后，结果为 ␣␣11.35。首先对小数部分四舍五入到两位（.345变为.35），然后计算总宽度为5（1,1,.,3,5），最后在左侧用两个空格填充，以补足7位的总宽度。
# #
# # %.2f 含义：不限制输出宽度，只设置小数点后的精度为2位（会进行四舍五入）。
# # 示例：数字 11.345使用 %.2f格式化后，结果为 11.35。仅对小数部分四舍五入到两位，输出宽度由数字本身决定。
#
# num1 = 11
# num2 = 11.345
# print("数字11宽度限制5，结果是：%5d" % num1)
# print("数字11宽度限制1，结果是：%1d" % num1)
# print("数字11.345宽度限制7，小数精度2，结果是：%7.2f" % num2)
# print("数字11.345不限制，小数精度2，结果是：%.2f" % num2)
#
#
# #字符串格式化-快速写法
# #语法：f“内容{变量}”的格式来快熟格式化
#
# name03 = "test"
# year = 2025
# price = 10.01
# print( f"我是{name03},今年是{year},面的价格是{price}")


# #input语句：输入
#
# print("tell me who you are:")
# name04 = input()
# print("you name is:%s" % name04)
# name05 = input("tell me who you are:")
# print("you name is:%s" % name05)#input输入默认都是字符串，如果需要转换浮点数等需要自行转换
# price01 = input("tell me the number is: ")
# print("价格的数据类型是:",type(price01))
# print("价格现在的数据类型是:",type(int(price01)))


# # bool 运算符
#
# result = 10 > 5
# print(f"result is {result},the type of result is {type(result)}")#运算符： == != > < >= <=
# print(f"the type of True is {type(True)}")
# print(f"the type of False is {type(False)}")
# num1 = 10
# num2 = 10
# print(f"10==10的结果是{num1 == num2}")
# print(f"10!=10的结果是{num1 != num2}")
# name1 = "y"
# name2 = "b"
# print(f"y>=b的结果是{name1 >= name2}")

# #if 语句
#
# print("欢迎来到黑马动物园。")
# height = int(input("请输入你的身高(cm)："))
# vip_level = int(input("请输入你的vip级别(1~5)："))
#
# if height < 120:
#     print("您的身高小于120cm，可以免费游玩。")
# elif vip_level > 3:                              #elif == else if
#     print("您的vip级别大于3，可以免费游玩。")
# else:
#     print("不好意思，所有条件都不满足，需要购票10元。")
#
# print("祝您游玩愉快。")
#
#
#
# if int(input("请输入你的身高(cm):")) < 120:
#     print("身高小于120cm，可以免费。")
# elif int(input("请输入你的VIP等级(1-5):")) > 3:
#     print("vip级别大于3，可以免费。")
# elif int(input("请告诉我今天几号:")) == 1:
#     print("今天是1号免费日，可以免费")
# else:
#     print("不好意思，条件都不满足，需要买票10元。")
# #34

# #随机数产生
#
# import random
# num = random.randint(1,10)
# print(num)
#
# #while 语法

# i= 1
# while i <= 10:
#     print(i)
#     i += 1



# import random
# num = random.randint(1,10)
# count = 0
# num = 20  # 假设要猜测的数字是20，可根据需求修改
# flag = True
# while flag:
#     guess_num = int(input("请输入你猜测的数字:"))
#     count += 1
#     if guess_num == num:
#         print("猜中了")
#         flag = False
#     else:
#         if guess_num > num:
#             print("你猜的大了")
#         else:
#             print("你猜的小了")
# print(f"你总共猜了{count}次")
#41

#
#
# #演示for循环的基础语法
#
# name = "itheima"
# for x in name:
#     # 将name的内容，挨个取出赋予x临时变量
#     # 就可以在循环体内对x进行处理
#     print(x)
#
#
# #演示Python中的range()语句的基本使用
#
# # range语法1 range(num)
# for x in range(10):
#     print(x)
#
# # range 语法2 range(num1, num2)
# for x in range(5, 10):
#     # 从5开始，到10结束（不包含10本身）的一个数字序列，数字之间间隔是1
#     print(x)
#
# # range 语法3 range(num1, num2, step)
# for x in range(5, 10, 2):
#     # 从5开始，到10结束（不包含10本身）的一个数字序列，数字之间的间隔是2
#     print(x)
#
#
#
# # 演示continue的嵌套应用
# for i in range(1, 6):
#     print("语句1")
#     for j in range(1, 6):
#         print("语句2")
#         continue
#         print("语句3")
#     print("语句4")
#
#     # 演示break的嵌套应用
#     for j in range(1, 6):
#         print("语句1")
#         for j in range(1, 6):
#             print("语句2")
#             break
#             print("语句3")
#         print("语句4")


# def 函数名(传入参数):
#     函数体：这里编写函数的具体功能逻辑
#     处理逻辑 = 传入参数的操作
#     return 处理逻辑的结果

# 示例：定义一个计算两数之和的函数
# def add_numbers(num1, num2):
#     sum_result = num1 + num2
#     return sum_result
#
# def add(x, y):
#     result = x + y
#     print(f"{x} + {y}的结果是:{result}")
#
#
#
#
# """
# 演示特殊字面量：None
# """
#
# # 无return语句的函数返回值
# def say_hi():
#     print("你好呀")
#
# result = say_hi()
# print(f"无返回值函数，返回的内容是：{result}")
# print(f"无返回值函数，返回的内容类型是：{type(result)}")
#
# # 主动返回None的函数
# def return_none():
#     return None
#
# res = return_none()
# print(f"无返回值函数，返回的内容是：{res}")
# print(f"主动返回None，内容是：{res}，类型是：{type(res)}")



#在PyCharm中查看函数说明文档
#
# def add(x, y):
#     """
#     add函数可以接收2个参数，进行2数相加的功能/n
#
#     :param x: 相加的数字1
#     :param y: 相加的数字2
#     :return: 返回相加的结果
#
#     """
#     return x + y
#
# add(1, 2)


#函数的嵌套调用

# def func_b():
#     print("---2---")
#
# def func_a():
#     print("---1---")
#     func_b()
#     print("---3---")
#
# # 调用函数func_a
# func_a()





#全局变量与局部变量

# global关键字，在函数内声明变量为全局变量
num = 200

def test_a():
    print(f"test_a: {num}")

def test_b():
    global num  # 设置内部定义的变量为全局变量
    num = 500
    print(f"test_b: {num}")

test_a()
test_b()
print(num)

#61







