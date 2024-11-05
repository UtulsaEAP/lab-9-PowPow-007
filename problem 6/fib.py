def fibonacci(n):
    
    #write your code here
    if n < 0:
        return -1
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a,b = 0,1
        for _ in range(1,n):
            a,b = b,a+b
        return a if n == 1 else b


if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')