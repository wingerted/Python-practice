def fibs(num):
    fibs = [0, 1]
    for i in range(num):
        fibs.append(fibs[-2] + fibs[-1])
    return fibs

num = int(input("处理数据的数量："))

fibs = fibs(num)

print(fibs)

