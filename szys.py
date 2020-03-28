import random
# 四则运算
def szys():

    ysf = ['＋', '－', '×', '÷']

    f = random.randint(0, 3)

    n1 = random.randint(1, 100)

    n2 = random.randint(1, 100)

    result = 0

    if f == 0:  # 加法

        while n1 + n2 >=100:
          n1 = random.randint(1, 100)

          n2 = random.randint(1, 100)

        result = int(n1 + n2)

    elif f == 1:  # 减法，要先比较大小，防止输出负数

        n1, n2 = max(n1, n2), min(n1, n2)

        result = n1 - n2

    elif f == 2:  # 乘法

        while n1 * n2 >=100:
            n1 = random.randint(1, 100)

            n2 = random.randint(1, 100)

        result = int(n1 * n2)

    elif f == 3:  # 除法，要比较大小，并循环取整除

        n1, n2 = max(n1, n2), min(n1, n2)

        while n1 % n2 != 0:
            n1 = random.randint(1, 100)

            n2 = random.randint(1, 100)

            n1, n2 = max(n1, n2), min(n1, n2)

        result = int(n1 / n2)

    print(n1, ysf[f], n2, '= ', end='')

    return result

print('进行四则运算')

m=0
n=10
while n>0:

        result = szys()

        j = input()

        s = int(j)

        if s == result:

            print('right')
            m = m + 1
        else:

            print('error.the answer is', result)

        n=n-1
print('正确', m,'道题目','错误', 10-m,'道题目','得',m*10,'分')

