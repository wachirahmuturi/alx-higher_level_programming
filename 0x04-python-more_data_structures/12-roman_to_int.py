#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return None
    if roman_string == "":
        return 0
    dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    str_to_list = list(roman_string.strip())
#for i in str_to_list:
    result = 0
    if ord('I') in str_to_list and ord('V') in str_to_list and (abs(str_to_list.index('V') - str_to_list.index('I')) in range(1,4)):

        for i in str_to_list:
            if i == 'I':
                if str_to_list.index('I') < str_to_list.index('V'):
                    result += -1
                else:
                    result += 1
            else:
                result += dic[i]
    elif ord('X') in str_to_list and ord('I') in str_to_list and (abs(str_to_list.index('X') - str_to_list.index('I')) in range(1,4)):
        for i in str_to_list:
            if i == 'I':
                if str_to_list.index('I') < str_to_list.index('X'):
                    result += -1
                else:
                    result += 1
            else:   
                result += dic[i]

    else:
        for i in str_to_list:
            result += dic[i]
    return result
