def binary(num):
    if num == 0:
        return ''
    number = num % 2
    return binary(num // 2) + str(number)


print(binary(10))
print(binary(7))

#  without recursion
'''
def convert_num(number):
    final = ''
    while number != 0:
        num = number % 2
        number = number // 2
        final = str(num) + final
    return final


print(convert_num(10))
print(convert_num(7))
'''
