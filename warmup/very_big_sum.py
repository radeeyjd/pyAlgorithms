__author__ = 'jd'


def very_big_sum():
    size = int(input())
    array = input().split(" ")
    result = 0
    for i in range(0, size):
        result += int(array[i])
    print(result)


very_big_sum()
