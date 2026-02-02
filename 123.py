
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
# num3 = int("只因你太美")   错误示范，转换要符合类型
# print(type(num3) ,num3)
#
# #算数运算符
#
# print("1 + 1 =", 1 + 1)
# print("2 - 1 =", 2 - 1)
# print("3 * 3 =", 3 * 3)
# print("5 / 3 =", 5 / 3)
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
##print("他说：\"你好\"") 输出：他说："你好"

# \n：换行
#
# \t：制表符（Tab键）

# # 字符串字面量之间的拼接  注：无法和非字符串类型进行拼接



# name000 = "程序员"
# address = "china"
# print("i am " + name000 + ", i am in " + address )


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
# 格式化的精度控制
# m.n ： m控制宽度，要求时数字（很少使用），设置宽度小于数字自身，不生效
#       .n控制小数点精度，要求是数字，会进行小数的四舍五入
# #eg： %5d 含义：将整数的输出宽度控制为5位。
# 示例：数字 11使用 %5d格式化后，结果为 ␣␣␣11（其中␣代表空格）。即用三个空格在左侧填充，以补足5位的宽度。
#
# %5.2f 含义：将浮点数的输出宽度控制为5位，并将小数点后的精度设置为2位（小数部分限制2位，会进行四舍五入）。注意：小数点本身和小数部分都计入总宽度。
# 示例：数字 11.345使用 %7.2f格式化后，结果为 ␣␣11.35。首先对小数部分四舍五入到两位（.345变为.35），然后计算总宽度为5（1,1,.,3,5），最后在左侧用两个空格填充，以补足7位的总宽度。
#
# %.2f 含义：不限制输出宽度，只设置小数点后的精度为2位（会进行四舍五入）。
# 示例：数字 11.345使用 %.2f格式化后，结果为 11.35。仅对小数部分四舍五入到两位，输出宽度由数字本身决定。

# num1 = 11
# num2 = 11.345
# print("数字11宽度限制5，结果是：%5d" % num1)
# print("数字11宽度限制1，结果是：%1d" % num1)
# print("数字11.345宽度限制7，小数精度2，结果是：%7.2f" % num2)
# print("数字11.345不限制，小数精度2，结果是：%.2f" % num2)


#--------------------------------------1.28------------------------
# #字符串格式化-快速写法
# #语法：f“内容{变量}”的格式来快速格式化
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
# print("you name is:%s %s " % (name05,name04)) #两个%s的情况
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

# 不需要考虑变量在不在末尾，直接填进去，最不容易出错
# print(f"商品是：{name}，价格是：{price:.2f} 元")


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
# 无return语句的函数返回值
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




#
# #全局变量与局部变量
#
# # global关键字，在函数内声明变量为全局变量
# num = 200
#
# def test_a():
#     print(f"test_a: {num}")
#
# def test_b():
#     global num  # 设置内部定义的变量为全局变量
#     num = 500
#     print(f"test_b: {num}")
#
# test_a()
# test_b()
# print(num)

#61

#银行存款取款案例

# 定义全局变量money name
# money = 5000000
# name = None
# # 要求客户输入姓名
# name = input("请输入您的姓名：")
# # 定义查询函数
# def query(show_header):
#     if show_header:
#         print("-------------查询余额-------------")
#     print(f"{name}，您好，您的余额剩余：{money}元")
#
# # 定义存款函数
# def saving(num):
#     global money    # money在函数内部定义为全局变量
#     money += num
#     print("-------------存款-------------")
#     print(f"{name}，您好，您存款{num}元成功。")
#
#     # 调用query函数查询余额
#     query(False)
# # 定义取款函数
# def get_money(num):
#     global money
#     money -= num
#     print("-------------取款-------------")
#     print(f"{name}，您好，您取款{num}元成功。")
#
#     # 调用query函数查询余额
#     query(False)
#
# # 定义主菜单函数
# def main():
#     print("-------------主菜单-------------")
#     print(f"{name}，您好，欢迎来到黑马银行ATM。请选择操作：")
#     print("查询余额\t\t[输入1]")
#     print("存款\t\t[输入2]")
#     print("取款\t\t[输入3]")
#     print("退出\t\t[输入4]")
#     return input("请输入你的选择：")
#
#
# # 设置无限循环，确保程序不退出
# while True:
#     keyboard_input = main()
#     if keyboard_input == "1":
#         query(True)
#         continue    # 通过continue继续下一次循环，一进来就是回到了主菜单
#     elif keyboard_input == "2":
#         num = int(input("您想要存多少钱？请输入："))
#         saving(num)
#         continue
#     elif keyboard_input == "3":
#         num = int(input("您想要取多少钱？请输入："))
#         get_money(num)
#         continue
#     else:
#         print("程序退出啦")
#         break       # 通过break退出循环










#数据容器 : list (列表)、tuple (元组)、str (字符串)、set (集合)、dict (字典)

# # 字面量
# [元素1, 元素2, 元素3, 元素4, ...]
#
# # 定义变量
# 变量名称 = [元素1, 元素2, 元素3, 元素4, ...]
#
# # 定义空列表
# 变量名称 = []
# 变量名称 = list()

# name_list = ['itheima', 'itcast', 'python']
# print(name_list)
# print(type(name_list))
#
# my_list = ['itheima', 666, True]
# print(my_list)
# print(type(my_list))
#
# #list列表可以一次性储存多个不同数据类型的数据，支持嵌套
# my_list = [[1, 2, 3], [4, 5, 6]]
# print(my_list)
# print(type(my_list))




# #list列表的功能
#
#
# mylist = ["itcast", "itheima", "python"]
# # 1.1 查找某元素在列表内的下标索引
# index = mylist.index("itheima")
# print(f"itheima在列表中的下标索引值是：{index}")
#
# # 1.2 如果被查找的元素不存在，会报错
# # index = mylist.index("ithe")
# print(f"hello在列表中的下标索引值是：{index}")
#
#
# mylist = ["itcast", "itheima", "python"]
# # 2. 修改特定下标索引的值
# mylist[0] = "传智教育"
# print(f"列表被修改后，结果是：{mylist}")
#
#
# 3. 在指定下标位置插入新元素
# mylist.insert(1, "best")
# print(f"列表插入元素后，结果是：{mylist}")
#
#
# # 4. 在列表的尾部追加单个新元素
# mylist.append("黑马程序员")
# print(f"列表在追加了元素后，结果是：{mylist}")
#
#
# # 5. 在列表的尾部追加一批新元素
# mylist2 = [1, 2, 3]
# mylist.extend(mylist2)
# print(f"列表在追加了一个新的列表后，结果是：{mylist}")
#
#
# mylist = ["itcast", "itheima", "python"]
# # 6.1 方式1：del 列表[下标]
# del mylist[2]
# print(f"列表删除元素后结果是：{mylist}")
#
# # 6.2 方式2：列表.pop(下标)
# mylist = ["itcast", "itheima", "python"]
# element = mylist.pop(2)
# print(f"通过pop方法取出元素后列表内容：{mylist}，取出的元素是：{element}")
#
# # 7. 删除某元素在列表中的第一个匹配项
# mylist = ["itcast", "itheima", "itcast", "itheima", "python"]
# mylist.remove("itheima")
# print(f"通过remove方法移除元素后，列表的结果是：{mylist}")
#
# # 8. 清空列表
# mylist.clear()
# print(f"列表被清空了，结果是：{mylist}")
#
# # 9. 统计列表内某元素的数量
# mylist = ["itcast", "itheima", "itcast", "itheima", "python"]
# count = mylist.count("itheima")
# print(f"列表中itheima的数量是：{count}")
#
# # 10. 统计列表中全部的元素数量
# mylist = ["itcast", "itheima", "itcast", "itheima", "python"]
# count = len(mylist)
# print(f"列表的元素数量总共有：{count}个")
#
# #67
# """
# 演示对list列表的循环，使用while和for循环2种方式
# """
#
# def list_while_func():
#     """
#     使用while循环遍历列表的演示函数
#     :return: None
#     """
#     my_list = ["传智教育", "黑马程序员", "Python"]
#     # 初始化索引
#     index = 0
#     while index < len(my_list):
#         print(my_list[index])
#         index += 1
#
# def list_for_func():
#     """
#     使用for循环遍历列表的演示函数
#     :return: None
#     """
#     my_list = ["传智教育", "黑马程序员", "Python"]
#     for element in my_list:
#         print(element)
#
# # 调用两个函数来演示
# if __name__ == "__main__":
#     print("使用while循环遍历列表：")
#     list_while_func()
#     print("\n使用for循环遍历列表：")
#     list_for_func()



#元组

# 元组是 Python 中有序、不可变的序列数据类型，用圆括号 ()
# 包裹元素，元素之间用逗号分隔。“不可变” 意味着元组创建后，无法修改、添加或删除其中的元素

# # 定义元组
# t1 = (1, "Hello", True)
# t2 = ()
# t3 = tuple()
#
# print(f"t1的类型是：{type(t1)}，内容是：{t1}")
# print(f"t2的类型是：{type(t2)}，内容是：{t2}")
# print(f"t3的类型是：{type(t3)}，内容是：{t3}")
#
# # 定义单个元素的元组
# t4 = ("hello",)#定义单个元素的元组时，必须在元素后面加逗号
# print(f"t4的类型是：{type(t4)}，t4的内容是：{t4}")
#
# # 元组的嵌套
# t5 = ((1, 2, 3), (4, 5, 6))
# print(f"t5的类型是：{type(t5)}，内容是：{t5}")
#
# # 下标索引去取出内容
# num = t5[1][2]
# print(f"从嵌套元组中取出的数据是：{num}")
#
# # 元组的操作：index查找方法
# t6 = ("传智教育", "黑马程序员", "Python")
# index = t6.index("黑马程序员")
# print(f"在元组t6中查找黑马程序员，的下标是：{index}")
#
# # 元组的操作：count统计方法
# t7 = ("传智教育", "黑马程序员", "黑马程序员", "黑马程序员", "Python")
# num = t7.count("黑马程序员")
# print(f"在元组t7中统计黑马程序员的数量有：{num}个")
#
# # 元组的操作：len函数统计元组元素数量
# t8 = ("传智教育", "黑马程序员", "黑马程序员", "黑马程序员", "Python")
# num = len(t8)
# print(f"t8元组中的元素有：{num}个")
#
# # 元组的遍历：while
# index = 0
# while index < len(t8):
#     print(f"元组的元素有：{t8[index]}")
#     index += 1
#
# # 元组的遍历：for
# for element in t8:
#     print(f"元组的元素有：{element}")



#字符串

"""
只可以存储字符串
长度任意（取决于内存大小）
支持下标索引
允许重复字符串存在
不可以修改（增加或删除元素等）
支持 for 循环
"""

my_str = "itheima and itcast"

# # 通过下标索引取值
# value = my_str[2]
# value2 = my_str[-16]
# print(f"从字符串{my_str}取下标为2的元素，值是：{value}, 取下标为-16的元素。值是：{value2}")
#
# # my_str[2] = "H"  # ❌ 字符串是不可变类型，直接修改会报错
#
# # index方法：查找子串的起始下标
# value = my_str.index("and")
# print(f"在字符串{my_str}中查找and，其起始下标是：{value}")
#
# # replace方法
# new_my_str = my_str.replace("it", "程序")
# print(f"将字符串{my_str}，进行替换后得到：{new_my_str}")
#
# # ❷ 只替换第一个"it"：指定count=1
# replace_first = my_str.replace("it", "程序", 1)
# print(f"只替换第一个'it'的结果：{replace_first}")
#
#
#
# # split方法
# my_str = "hello python itheima itcast"
# my_str_list = my_str.split(" ")
# print(f"将字符串{my_str}进行split切分后得到：{my_str_list}，类型是：{type(my_str_list)}")
#
# # strip方法
# my_str = "  itheima and itcast  "
# new_my_str = my_str.strip()  # 不传入参数，去除首尾空格
# print(f"字符串{my_str}被strip后，结果：{new_my_str}")
#
# my_str = "12itheima and itcast21"
# new_my_str = my_str.strip("12")
# print(f"字符串{my_str}被strip('12')后，结果：{new_my_str}")
#
# # 统计字符串中某字符串的出现次数，count
# my_str = "itheima and itcast"
# count = my_str.count("it")
# print(f"字符串{my_str}中it出现的次数是：{count}")
#
# # 统计字符串的长度，len()
# num = len(my_str)
# print(f"字符串{my_str}的长度是：{num}")


#练习
# a = "itheima itcast boxuegu"
# count = a.count("it")
# print(count)
# ax = a.replace(" ","|")
# print(ax)
# ab = ax.split("|")
# print(ab)

#70



































