'''
Created on 2016. 5. 12.

@author: user
조건문(if)
형식1)
    if 조건식:
        실행문
형식2)
    if 조건식:
        실행문
    else:
        실행문
'''

#형식2
'''
var=5
if var >= 10:
    print('d')
else:
    print('10미만이다')
'''
#문제) 100~90: '우수', 89~70: '보통' 그 이하: '저조'
'''
score=int(input('숫자 입력해: '))
if score>= 90:
   print('우수')
else:
    if score<=70:
        print('저조')
    else:
        print('보통')
'''
#시스템의 날짜/시간 가져오기
import datetime #datetime모듈을 import

today = datetime.datetime.now() #모듈명.클래스명.함수()
print(today)

#요일 리턴 받기
day = today.weekday()
print(day) #3-> 목요일 0~4 : 평일

#형식3
'''
    if 조건식1:
        실행문 <-조건식1이 참인 경우
    elif 조건식2:
        실행문 <-조건식1이 거짓인 경우
    else:
        실행문 <-모든 조건이 거짓인 경우

score=int(input('숫자 입력해: '))
if score>= 90:
    print('우수')
elif score>=80:
    print('준수')
elif score>=70:
    print('보통')
else:
    print('준수')
'''  
# 3항 연산자
#형식) 참인 경우 계산 if 조건식 else 거짓일 경우 계산
num=9
re = print(num * 2) if num >= 5 else num +2 

#문제) 아래를 3항 연산자로 변환해라
num = 4
if num >= 5:
    print('5보다 큼')
else:
    print('5보다 작음')

re = print('5보다 큼') if num >=5 else print('5보다 작음')



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    

    
    
    

    
    
    

    
    
    

    
    
    
