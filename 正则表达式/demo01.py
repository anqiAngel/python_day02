import re

str1 = 'Hello world'
result = re.match(r'[Hh]ello', str1)
# print(result)
print(result.group())
str2 = '速度与激情12'
result1 = re.match(r'速度与激情\d{1,2}', str2)
print(result1.group())