def combination(data, n):  # 순서 없는 조합 -> set
    ret = []
    if n == 0 or n > len(data):
        return ret
    if n == 1:
        ret += list(map(lambda x: {x}, data))
    else:
        for i in range(len(data)):
            ret += list(map(lambda x: {data[i]} | x, combination(data[i + 1:], n - 1)))

    return ret


def permutation(data, n):  # 순열: 순서 있는 조합 -> tuple
    ret = []
    if n == 0 or n > len(data):
        return ret
    if n == 1:
        return list(map(lambda x: (x,), data))
    for i in range(len(data)):
        temp = [] + data
        temp.remove(data[i])
        ret += tuple(map(lambda x: (data[i],) + x, permutation(temp, n - 1)))
    return ret


target= list(map(int, input("data: ").split()))
N = int(input("N: "))
print("permutation: ", permutation(target[:], N))
print("combination:", combination(target[:],N))