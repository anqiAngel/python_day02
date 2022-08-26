import re


def main():
    names = ['age', '_age', '1age', 'A_age', 'age!']
    for name in names:
        result = re.match(r'^[a-zA-Z_][a-zA-Z1-9_]*$', name)
        if result:
            print(result.group(), '符合要求的变量名')
        else:
            print(name, '不符合要求的变量名~~')


if __name__ == '__main__':
    main()
