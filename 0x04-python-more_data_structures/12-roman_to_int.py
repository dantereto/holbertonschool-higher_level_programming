#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string == None
    return (0)
    sum = 0
    r_dic = {"I": 1, "V": 5, "X": 10, "L": 50
             , "C": 100, "D": 500, "M": 1000}
    for i in range(len(roman_string)):
        if i == len(roman_string) - 1:  
            sum += r_dic[roman_string[i]]
        elif r_dic[roman_string[i]] >= r_dic[roman_string[i + 1]]:
            sum += r_dic[roman_string[i]]
        else:
            sum -= r_dic[roman_string[i]]
    return (sum)
