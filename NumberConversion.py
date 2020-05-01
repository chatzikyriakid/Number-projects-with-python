hex_symbols = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
hex_numbers = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}


def decimal_to_other():
    # user enters number
    while True:
        base = int(input('Give number system from 2 to 16: '))
        if base < 2 or base > 16:
            print('Value must be between 2 and 16, try again')
        else:
            break
    num = int(input('Give the number in decimal format: '))
    number = num
    remainder = []
    if base != 16:
        while num >= 1:
            remainder.append(num % base)
            num = int(num / base)
    else:
        # in case of base 16 we must cover the case of A,B,C,D,E,F
        while num >= 1:
            if 10 <= num % base <= 15:
                remainder.append(hex_numbers.get(num % base))
            else:
                remainder.append(num % base)
            num = int(num / base)
    print(f'Base {base} conversion of decimal number {number} is: ', end='')
    print(*remainder[::-1], sep='')


def other_to_decimal():
    # user enters number
    while True:
        base = int(input('Give number system from 2 to 16: '))
        if base < 2 or base > 16:
            print('Value must be between 2 and 16, try again')
        else:
            break
    digits = int(input('Enter number of bits: '))
    number = []
    while digits > 0:
        if base == 16:
            bit = int(input(f'Give {digits}th bit '), 16)
        else:
            bit = int(input(f'Give {digits}th bit '))
        if bit >= base:
            print(f'You use base {base} so bit value must be lower than {base}')
        else:
            number.append(bit)
            digits -= 1
    number = number[::-1]
    print(f'You entered:', end='')
    print(*number[::-1], sep='')

    # conversion
    dec_number = 0
    for i in range(len(number)):
        dec_number += (number[i] * base ** i)
    print(f'Decimal value of ', end='')
    print(*number[::-1], sep='', end='')
    print(' is: ', end='')
    print(dec_number)


while True:
    print('Welcome to number conversion choose the type of conversion:')
    print('Decimal to other base - [1]')
    print('From other base to decimal - [2]')
    choice = input('')
    if choice != '1' and choice != '2':
        print('Please choose between 1 or 2')
    else:
        break
if choice == '1':
    decimal_to_other()
else:
    other_to_decimal()
