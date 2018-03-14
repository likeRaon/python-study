'''

Day 2

#카이사르 암호

def encrypt(plain,shift_key=1): #plain 암호화 할 단어 / shift_key = 넘길 숫자
    # shift_key
    result = ''
    for letter in plain:
        result += chr(ord(letter) + shift_key)

    return result
encrypted_text = encrypt("Ssibal")
print encrypted_text

# import os 로 특정 디렉토리 파싱

import os

data = {'file' : {'py':[], 'txt':[], 'png':[], 'etc':[]}}

for root,dirs,files in os.walk("."): #디렉토리 내 모든 파일 확인
    for filename in files:
        if filename.endswith('.py'): #파이썬 확장자 확인 후 데이터 전송입력
            data['file']['py'].append(filename)
        elif filename.endswith('.png'): #상동 / png 확장자
            data['file']['png'].append(filename)
        elif filename.endswith('.txt'): #상동 / txt 확장자
            data['file']['txt'].append(filename)
        else: #위에서 분류된 파일 외에 나머지 데이터 전송입력
            data['file']['etc'].append(filename)


print data['file']['py'] #데이터 딕셔너리 안의 [파일][파이썬] 실행

# 파일 생성 / 이름 변경 / 삭제
import os

with open("new_file.txt", "w") as f:
    f.write("cuty sexy moai")

os.rename("new_file.txt", "renamed_new_file.txt") # 파일 이름 변경

if os.path.exists("renamed_new_file.txt"): #정상 변경 됐는지 확인
    print "your file was renamed"

os.remove("renamed_new_file.txt") # 삭제

'''
