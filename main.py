import numpy as np


def sort(list):
    sorted = True
    for i in range(len(list) - 1):
        if (list[i+1] < list[i]):
            temp = list[i+1]
            list[i+1] = list[i]
            list[i] = temp
            sorted = False
    if sorted == False:
        return sort(list)
    else:
        return list


length = 50
values = []
values = np.random.randint(1, 100, length)

print(values)
print(sort(values))

