from cs50 import get_string
from math import floor
import re

p = re.compile('^\d+$')

match = None
card_type = ""
num_str1 = ""
num_str2 = ""
pos_num1 = 0
pos_num2 = 0
total_pos_num1 = 0
total_pos_num2 = 0

while match == None:
    number = get_string('Number: ')
    match = p.match(number)


length = len(number)
pos1 = length - 2
pos2 = length - 1

for i in range(int(length / 2)):
    pos_num1 = number[pos1]
    pos_num1 = int(pos_num1) * 2
    num_str1 += str(pos_num1)
    pos1 -= 2

for j in range(len(num_str1)):
    total_pos_num1 += int(num_str1[j])

for k in range(int((length+1) / 2)):
    pos_num2 = number[pos2]
    pos_num2 = int(pos_num2)
    num_str2 += str(pos_num2)
    pos2 -= 2

for k in range(len(num_str2)):
    total_pos_num2 += int(num_str2[k])

checksum = total_pos_num1 + total_pos_num2

number = int(number)

if checksum % 10 != 0:
    card_type = "INVALID"
elif checksum % 10 == 0:
    if number > 340000000000000 and number < 349999999999999:
        card_type = "AMEX"
    elif number > 370000000000000 and number < 379999999999999:
        card_type = "AMEX"
    elif number > 5100000000000000 and number < 5599999999999999:
        card_type = "MASTERCARD"
    elif number > 4000000000000 and number < 4999999999999:
        card_type = "VISA"
    elif number > 4000000000000000 and number < 4999999999999999:
        card_type = "VISA"
    else:
        card_type = "INVALID"

print(card_type)
