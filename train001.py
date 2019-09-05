"""
Python 练习实例1
题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。
"""
count = 0
for bai_wei in range(1, 5):
    for shi_wei in range(1, 5):
        for ge_wei in range(1, 5):
            if bai_wei != shi_wei and bai_wei != ge_wei and shi_wei != ge_wei:
                print(bai_wei, shi_wei, ge_wei)
                count += 1

print('一共有%d个组合' % count)