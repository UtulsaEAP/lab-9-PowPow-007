def fibonacci(n):
    
    #write your code here
    a,b = 0,1
    if n < 0:
        return -1
    elif n == 0:
        return 0
    else:
        for _ in range(1, n+1):
            a,b = b,a+b
            return b


if __name__ == '__main__':
    start_num = int(input())
    if start_num < 0:
        print('-1')
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')