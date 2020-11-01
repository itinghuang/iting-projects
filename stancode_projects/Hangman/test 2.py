
def main():
    num = int(input('Run?'))
    if num != 'Y':
        if num != 'N':
            print('Illegal format')
        else:
            print('Have a good one!')
    else:
        num2 = int(input('n: '))
        if is_prime(num2) is True:
            print(str(num2)+'is a prime number.')
        else:
            print(str(num2) + 'is not a prime number')


def is_prime(n):
    k = 2
    while n !=1:
        if k != n:
            if n % k == 0:
                break
            else:
                k += 1
        else:
            return False
    return True

