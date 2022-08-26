import re


def main():
    email_address = input("请输入你的163邮箱地址:")
    # \.转义 ()分组 group(1) group(2) group(3)
    result = re.match(r'^[a-zA-Z1-9]{4,20}@(163|qq)\.com$',email_address)
    if result:
        print(result.group(), '符合规范')
    else:
        print(email_address, '不符合规范')


if __name__ == '__main__':
    main()