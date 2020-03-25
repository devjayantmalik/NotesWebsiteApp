def sumAll(*args):
    sum = 0

    for num in args:
        sum += num

    return sum

def multiplyAll(*args):
    answer = 1

    for num in args:
        answer *= num

    return answer
