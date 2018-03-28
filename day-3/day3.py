#-*- coding: utf-8 -*-
# 소문자 -> 대문자 / 대문자 -> 소문자 변환 코드
def change(string):
    result = ''
    for check in string:
        if check.islower() is True:
            result += check.upper()
        else:
            result += check.lower()
    return result
string = raw_input("입력:")
print change(string)
