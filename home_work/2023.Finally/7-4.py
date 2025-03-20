# 提取电话号码

import re

def extract_phone_numbers(input_string):
    pattern = r'\b0\d{2,3}-\d{7,8}\b'
    phone_numbers = re.findall(pattern, input_string)
    return phone_numbers

input_string = input()
phone_numbers = extract_phone_numbers(input_string)

for number in phone_numbers:
    start_index = input_string.find(number)
    print(start_index, number)