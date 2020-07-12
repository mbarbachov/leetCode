# Valid Phone Numbers
file = open('file.txt', 'r')

for phone_number in file:
    phone_number = phone_number.strip()
    if len(phone_number) == 12:
        if phone_number[3] == phone_number[7] == '-':
            print(phone_number)
    elif len(phone_number) == 14:
        if phone_number[0] == '(' and phone_number[4] == ')':
            if phone_number[5] == ' ' and phone_number[10] == '-':
                print(phone_number)

file.close()
