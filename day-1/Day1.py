'''

Day 1

# 삼항 연산자 팩토리얼
def factorial(number):

    return number if number <= 1 else number * factorial(number-1)

print (factorial(5))

# 구구단
def multi(i):
  a = 1
  for a in range(a,10):
      print ("{} X {} = {}".format(i,a,i*a))
      
multi(5) 

# 이름 나이 직업 취미 / 함수 구현
data = {'name' : 'minsoo', 'age' : '22', 'job' : 'army sir', 'hobby' : 'longboard'}

print (data) # 전체 데이터 출력
print (data['name']) # 원하는 결과값 출력

# 환율

def exchange(money):  
    USD = 1084 # 달러  
    JPY = 1008 # 엔  
    CNY = 170  # 위안  
    EUR = 1330 # 유로  
    if money <= 0: 
        print (" 1 이상의 숫자 입력")  
        else:      
            print ("{} KRW ->  {:.2f} USD".format(money,money/USD))      
            print ("{} KRW ->  {:.2f} YEN".format(money,money/JPY*100))      
            print ("{} KRW ->  {:.2f} CNY".format(money,money/CNY))      
            print ("{} KRW ->  {:.2f} EUR".format(money,money/EUR)) exchange(0) 
맨위로

'''
