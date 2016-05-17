'''
Created on 2016. 5. 13.
반복문(while)
형식)
    while 조건:
        실행문
        실행문
'''

a=1
while a<=5:
    print(a,end=' ')
    a+=1 #a=a+1 카운터 변수
else: #조건이 거짓인 경우, 생략가능
    print('while수행문 - 반드시 수정')
    
print('\다중 반복분')
i=1
while i <=3:
    j=1
    while j<=4:
        print('i=', str(i), ',j=', str(j))
        j +=1 #inner 카운터
    i += 1 #outer 카운터

#문제) 1~100사이에서 5의 배수의 합을 출력
# i = 1~100
# if i % 5 == 0
i = s= 0
while i<=100:
    if i % 5 == 0 :
        s += i #5의 배수이면 s에 누적
    i += 1 #카운터 변수
print('1~100 사이 중에서 5의 배수의 합: ' + str(s))

#import + 모듈명
import random
print('\랜덤으로 이름 선택')
names=['통일신라', '문무왕','백제','땅따먹기','근초고왕']
print(names)
n = 0 #index = 0
while n<4 :
    r = random.randint(0,3) #난수 정수 생성: 0~3
    print(r,':', str(names[r]), end='')
    n += 1

print('\n별 출력하기')
i=1
while i<=10:
    j=1
    re = '' #별 누적변수 
    while j <= i:
        re= re + '*'
        j += 1
    print(re)
    i += 1

#문제) 1~100 사이 중에서 3의 배수이나 2의 배수가 아닌 수를 출력, 합계 계산
# 3,6,9
i=tot=0
while i<=100:
    i += 1
    if i % 3 == 0 and i % 2 !=0:
        print(i, end=',')#콤마로 같은 줄에 중복 출력
        tot += i #합계 변수에 누적
print('\n합계=',tot)

#문제2)-1,3,-5,7...99와 같은 형태로 출력하고, 합계 계산해
i= cnt= 1
tot = 0 
while i <= 100:
    if cnt%2 !=0:
        k= -1 * i
        tot += k
        print(k,end='')
    else:
        tot +=i
        print(i,end=',')
    i +=2
    cnt +=1
print('\n전체합계=',tot)

'''
continue, break
'''

a=0
while a < 10:
    a +=1
    if a==5 : continue #조건 문장 skip
    if a == 7 : break #조건에서 탈출 exit
    print(a,end=' ')

'''
무한루프(loop): 무한 반복
    - 탈출 조건이 필요
'''
while True: #무한 루프
    a = int(input('숫자입력해: '))
    if a == 0:
        print('프로그램 종료')
        break
    print('입력값: ',a)

#from + 모듈명
#    vs
#from + 모듈명 import + 사용하고자 하는 함수명
#from random import randint
#후자로 할 경우 r = random.randint(0,3) #난수 정수 생성: 0~3
#여기에서 r=randint(0,3)이라 단축시켜서 사용가능
#num = randint(1,10)
'''
print('\n컴퓨터 숫자 맞히기')
while True:
    print('1~10사이 예상되는 숫자 입력:')
    guess=input()
    su = int(guess)
    if num == su:
        print('성공')
        break
    elif num > su:
        print('더 큰 숫자를 넣어봥')
    elif num < su:
        print('더 작은 숫자를 넣어봥')
'''      
#문제) 키보드로 입력한 숫자를 대상으로 홀수/짝수를 판별해
#조건> 만약 1000 이상의 숫자를 입력하면 loop 탈출

while True:
    print('숫자 입력해:')
    guess=int(input())
    if guess >= 1000:
        print('종료')
        break 
    elif guess % 2 == 0:
        print('홀수')
    else:
        print('짝수')



































