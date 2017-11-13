def str_reverse1(string):
    return string[::-1]


def str_reverse2(string):
    return ''.join(reversed(string))


if __name__ == '__main__':
    s = input('Stage 2. Reverse string: ')
    print(f'Reverse version 1: {str_reverse1(s)}')
    print(f'Reverse version 2: {str_reverse2(s)}')
