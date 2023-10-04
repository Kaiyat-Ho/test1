# Exercise0828 finished by 20354209 Jiayi He

# 3文本输出练习
# 3(1)
print("Hello Python")

# 3(2)
for i in range(5):
    print(i + 1)

# 3(3)
delimiter = input("指定输出的分隔符：")
print(1, 2, 3, 4, 5, sep=delimiter)
# 法2：
delimiter = input("指定输出的分隔符：")
for i in range(1, 6):
    print(i, end=delimiter)


# 4变量练习
int_20354209 = 1
float_20354209 = 2.0
bool_20354209 = True
str_20354209 = '4'
print('int_20354209=', int_20354209, ", 数据类型=", type(int_20354209), ", 地址=", id(int_20354209))
print('float_20354209=', float_20354209, ", 数据类型=", type(float_20354209), ", 地址=", id(float_20354209))
print('int_20354209=', bool_20354209, ", 数据类型=", type(bool_20354209), ", 地址=", id(bool_20354209))
print('int_20354209=', str_20354209, ", 数据类型=", type(str_20354209), ", 地址=", id(str_20354209))


# 5运算符练习
# 5（1）
x = int(input("x="))
ans_int = ((x + 10) ** 3) * 6 // 7
ans_rem = ((x + 10) ** 3) * 6 % 7
print('计算答案整数部分：', ans_int)
print('计算答案余数部分：', ans_rem)

# 5（2）
a = input("请输入第一个整数或浮点数：")
b = input("请输入第二个整数或浮点数：")
print(a < b)

# 5（3）
print(type(int_20354209) == type(float_20354209))

# 5（4）
print(bool_20354209 and int_20354209)


# 6循环语句练习
import random as r
ans_age = r.randint(0, 100)  # 随机年龄为答案
mark = False  # 用于控制是否退出游戏的标志

while mark == False:

    for i in range(3):  # 每次允许用户尝试3次
        ans_guess = input("猜年龄=")
        if ans_guess == ans_age:  # 回答正确，退出
            mark = True
            break
        print("回答错误！")

    if mark == False:  # 失败3次后，用户决定是否继续玩
        willings = input("想继续玩，回答Y或y；想退出，回答N或n")
        if willings == 'N' or willings == 'n':  # 用户不想玩，退出
            mark = True

print("游戏已退出")


# 7选择语句练习
weight = float(input("please input the weight(kg)="))
height = float(input("please input the height(m)="))
bmi = weight / (height ** 2)
if bmi < 18.5:
    print("体重过轻")
elif bmi < 25:
    print("标准体重")
elif bmi <= 28:
    print("有点微胖")
else:
    print("注意多运动")
