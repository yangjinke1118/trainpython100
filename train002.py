"""
题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，
低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，
高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，
高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，
求应发放奖金总数？
程序分析：请利用数轴来分界，定位。注意定义时需把奖金定义成长整型。

程序源代码：
实例(Python 2.0+)
#!/usr/bin/python
# -*- coding: UTF-8 -*-

i = int(raw_input('净利润:'))
arr = [1000000,600000,400000,200000,100000,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
r = 0
for idx in range(0,6):
    if i>arr[idx]:
        r+=(i-arr[idx])*rat[idx]
        print (i-arr[idx])*rat[idx]
        i=arr[idx]
print r
"""

#  自己实现


def get_reward_range(reward_set):
    reward_range = []
    for i in range(len(reward_set)):
        if i == 0:
            reward_range.append(reward_set[i])
        else:
            reward_range.append(reward_set[i] - reward_set[i-1])
    return reward_range


def get_reward(money, reward_set, percent_rate):
    reward_range = get_reward_range(reward_set)
    reward = 0.0
    _money = money
    if money == 100:  # 输入的money=100
        for i, num in enumerate(reward_range, 0):
            reward += num * percent_rate[i]
    elif money < 100:
        for i, num in enumerate(reward_range, 0):
            if _money > num:
                reward += num * percent_rate[i]
                _money -= num
            elif _money <= num:
                reward += _money * percent_rate[i]
                break
    elif money > 100:
        for i, num in enumerate(reward_range, 0):
            reward += num * percent_rate[i]
            _money -= num
        reward += _money * percent_rate[i+1]
    return reward


reward_set = [10, 20, 40, 60, 100]
percent_rate = [10, 7.5, 5, 3, 1.5, 1]


print('获得的奖金为:', get_reward(int(input('请输入利润金额:')), reward_set, percent_rate)/100)

input()

"""
1、示例代码程序更精简。
2、我自己的代码能够适应任何的奖金区间变化，只需要在reward_set和percent_rate
更新即可。
3、当然示例代码适当修改即可实现适应任何奖金区间变化

"""



