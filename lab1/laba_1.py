ZERO = '0000000000000000'
ONE = '0000000000000001'
ONE_ADDITION = '1111111111111111'


def to_straight(num):
    straight = ''
    if num < 0:
        num *= -1
        flag = True
    else:
        flag = False
    while num > 0:
        straight = str(num % 2) + straight
        num = num // 2
    for _ in range(len(straight), 15):
        straight = '0' + straight
    if flag:
        straight = '1' + straight
    else:
        straight = '0' + straight
    return straight


def to_reverse(num):
    straight = to_straight(num)
    return from_straight_to_reverse(straight)


def to_additional(num):
    straight = to_straight(num)
    return from_straight_to_additional(straight)


def from_straight_to_reverse(straight):
    reverse = ''
    if straight[0] == '1':
        for i in straight[1:]:
            if i == '0':
                reverse += '1'
            elif i == '1':
                reverse += '0'
        return '1' + reverse
    else:
        return straight


def from_straight_to_additional(straight):
    if straight[0] == '0':
        return straight
    else:
        additional = from_straight_to_reverse(straight)
        additional = addition(additional, ONE)
        return additional


def from_additional_to_straight(num_additional):
    num_additional = from_additional_to_reverse(num_additional)
    num_additional = from_straight_to_reverse(num_additional)
    return num_additional


def from_additional_to_reverse(num_additional):
    if num_additional[0] == '1':
        num_additional = addition(num_additional, ONE_ADDITION)    
    return num_additional


def addition(summand1, summand2, keyword=None):
    sum_value = ''
    summand1 = summand1[::-1]
    summand2 = summand2[::-1]
    remnant = 0
    for i in range(len(summand2)):
        sum_in_place = int(summand1[i]) + int(summand2[i]) + remnant
        if sum_in_place == 0:
            sum_value = '0' + sum_value
            remnant = 0
        elif sum_in_place == 1:
            sum_value = '1' + sum_value
            remnant = 0
        elif sum_in_place == 2:
            sum_value = '0' + sum_value
            remnant = 1
        elif sum_in_place == 3:
            sum_value = '1' + sum_value
            remnant = 1
    if keyword == 'reverse' and remnant == 1:
        sum_value = addition(sum_value, ONE)
    return sum_value


def multiplication(multiplier1, multiplier2):
    result = ZERO
    flag = multiplier1[0] == multiplier2[0]
    if multiplier2[0] == '1':
        multiplier2 = '0' + multiplier2[1:]
    while multiplier2 != ZERO:
        result = addition(multiplier1, result)
        multiplier2 = addition(multiplier2, ONE_ADDITION)
    if flag:
        result = '0' + result[1:]
    else:
        result = '1' + result[1:]
    return result


def division(dividend, divisor):
    quotient = ZERO
    if dividend[0] != divisor[0]:
        quotient = '-' + quotient
    difference = dividend = '0' + dividend[1:]
    divisor = '1' + divisor[1:]
    check = addition(dividend, from_straight_to_additional(divisor))
    if check[0] == '0':
        while difference[0] != '1':
            difference = addition(difference, from_straight_to_additional(divisor))
            if difference[0] != '1':
                quotient = addition(quotient, ONE)
            if difference == ZERO:
                return quotient + ',00000'
        difference = addition(difference, '0' + divisor[1:])
    return f'{quotient},{difference[11:]}'
            

def float_addition(summand1, summand2):
    mantissa1, index1 = summand1.split(',')
    mantissa2, index2 = summand2.split(',')
    mantissa1 = '00' + mantissa1[mantissa1.find('1'):]
    mantissa2 = '00' + mantissa2[mantissa2.find('1'):]
    while index1 != index2:
        index1 = addition(index1, ONE)
        mantissa1 = '0' + mantissa1
    result = addition(mantissa1, mantissa2)
    index1 = index1[index1.find('1'):]
    return f'{result[:2]},{result[2:]}*2^{index1}'


def main():
    pos_num1 = int(input('Enter first num: '))
    neg_num1 = pos_num1 * (-1)
    pos_num2 = int(input('Enter second num: '))
    neg_num2 = pos_num2 * (-1)
    print()
    print(f' X1 = {pos_num1}, X2 = {pos_num2}')
    print('                 |    Straight code    |    Reverse code    |   Additional code    ')
    print('------------------------------------------------------------------------------------')
    print(f'        X1       |   {to_straight(pos_num1)}  |  {to_reverse(pos_num1)}  |   {to_additional(pos_num1)}')
    print('------------------------------------------------------------------------------------')
    print(f'      - X1       |   {to_straight(neg_num1)}  |  {to_reverse(neg_num1)}  |   {to_additional(neg_num1)}')
    print('------------------------------------------------------------------------------------')
    print(f'        X2       |   {to_straight(pos_num2)}  |  {to_reverse(pos_num2)}  |   {to_additional(pos_num2)}')
    print('------------------------------------------------------------------------------------')
    print(f'      - X2       |   {to_straight(neg_num2)}  |  {to_reverse(neg_num2)}  |   {to_additional(neg_num2)}')
    print('------------------------------------------------------------------------------------')
    print('                                       Summa                                        ')
    print('------------------------------------------------------------------------------------')
    print('     X1 + X2     |', end = '')
    print(f'   {addition(to_straight(pos_num1), to_straight(pos_num2))}\
    |  {addition(to_reverse(pos_num1), to_reverse(pos_num2), "reverse")}\
    |   {addition(to_additional(pos_num1), to_additional(pos_num2))}')
    print('------------------------------------------------------------------------------------')
    print('   - X1 - X2     |', end = '')
    print(f'   {from_additional_to_straight(addition(to_additional(neg_num1), to_additional(neg_num2)))}\
    |  {addition(to_reverse(neg_num1), to_reverse(neg_num2), "reverse")}\
    |   {addition(to_additional(neg_num1), to_additional(neg_num2))}')
    print('------------------------------------------------------------------------------------')
    print('   - X1 + X2     |', end = '')
    print(f'   {from_additional_to_straight(addition(to_additional(neg_num1), to_straight(pos_num2)))}\
    |  {addition(to_reverse(neg_num1), to_reverse(pos_num2), "reverse")}\
    |   {addition(to_additional(neg_num1), to_additional(pos_num2))}')
    print('------------------------------------------------------------------------------------')
    print('     X1 - X2     |', end = '')
    print(f'   {from_additional_to_straight(addition(to_straight(pos_num1), to_additional(neg_num2)))}\
    |  {addition(to_reverse(pos_num1), to_reverse(neg_num2), "reverse")}\
    |   {addition(to_additional(pos_num1), to_additional(neg_num2))}')
    print('------------------------------------------------------------------------------------')
    print('                                  Proizvedenie                                      ')
    print('------------------------------------------------------------------------------------')
    print('     X1 * X2     |', end = '')
    print(f'   {multiplication(to_straight(pos_num1), to_straight(pos_num2))}\
    |  {multiplication(to_reverse(pos_num1), to_reverse(pos_num2))}\
    |   {multiplication(to_additional(pos_num1), to_additional(pos_num2))}')
    print('------------------------------------------------------------------------------------')
    print(' (- X1) * (- X2) |', end = '')
    print(f'   {multiplication(to_straight(neg_num1), to_straight(neg_num2))}\
    |  {from_straight_to_reverse(multiplication(to_straight(neg_num1), to_straight(neg_num2)))}\
    |   {from_straight_to_additional(multiplication(to_straight(neg_num1), to_straight(neg_num2)))}')
    print('------------------------------------------------------------------------------------')
    print('   (- X1) * X2   |', end = '')
    print(f'   {multiplication(to_straight(neg_num1), to_straight(pos_num2))}\
    |  {from_straight_to_reverse(multiplication(to_straight(neg_num1), to_straight(pos_num2)))}\
    |   {from_straight_to_additional(multiplication(to_straight(neg_num1), to_straight(pos_num2)))}')
    print('------------------------------------------------------------------------------------')
    print('   X1 * (- X2)   |', end = '')
    print(f'   {multiplication(to_straight(pos_num1), to_straight(neg_num2))}\
    |  {from_straight_to_reverse(multiplication(to_straight(pos_num1), to_straight(neg_num2)))}\
    |   {from_straight_to_additional(multiplication(to_straight(pos_num1), to_straight(neg_num2)))}')
    print('------------------------------------------------------------------------------------')
    print('                                     Delenie                                        ')
    print('------------------------------------------------------------------------------------')
    print(f'     X1 / X2     |    {division(to_straight(pos_num1), to_straight(pos_num2))}')
    print('------------------------------------------------------------------------------------')
    print(f'  - X1 / (- X2)  |    {division(to_straight(neg_num1), to_straight(neg_num2))}')
    print('------------------------------------------------------------------------------------')
    print(f'   X1 / (- X2)   |    {division(to_straight(pos_num1), to_straight(neg_num2))}')
    print('------------------------------------------------------------------------------------')
    print(f'   - X1 / X2     |    {division(to_straight(neg_num1), to_straight(pos_num2))}')
    print('------------------------------------------------------------------------------------')

    print(float_addition(to_straight(pos_num1) + ',0000000000000100', to_straight(pos_num2) + ',0000000000000101'))


if __name__ == '__main__':
    main()