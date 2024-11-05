def int_to_reverse_binary(num1):
    binary_val = ''
#write your while loop here
    #while num1 > 0:
        #write your code
    if num1 == 0:
        return '0'
    while num1 > 0:
        binary_val += str(num1 % 2)
        num1 = num1 // 2

    return binary_val;


def string_reverse(input_string): 
    reverse_input = ''
    
   #write your for loop here
    
    return input_string[::-1]

if __name__ == '__main__':
    user_input = int(input())
    
    reverse_binary = str(int_to_reverse_binary(user_input))
    binary = str(string_reverse(reverse_binary))
    
    print(binary)