"""
题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，
低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，
高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，
高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，
求应发放奖金总数？
程序分析：请利用数轴来分界，定位。注意定义时需把奖金定义成长整型。
"""
reward_set = [10, 20, 40, 60, 100]
percent_rate = [10, 7.5, 5, 3, 1.5, 1]

def get_reward_range(reward_set):
    reward_range = []
    for i in range(len(reward_set)):
        if i == 0:
            reward_range[i] = reward_set[i]
        else:
            reward_range[i] = reward_set[i] - reward_set[i-1]
    return reward_range

def get_reward(money, reward_range, percent_rate):
    reward = 0.0
    if money <= 100:
        for i, num in enumerate(reward_range, 0):
            if money <= num:
                reward += money * percent_rate[i]
                break
            else:
                reward += num * percent_rate[i]
                money -= num
    else:
        for i, num in enumerate(reward_range, 0):
            if money <= num:
                reward += money * percent_rate[i]
                break
            else:
                reward += num * percent_rate[i]
                money -= num



