'''
Created on 2016. 5. 18.

1. 함수의 지역 변수와 전역변수
2. 변수영역(scope) 및 접근 순서
'''
#전역변수보다 지역변수가 우선
#전역변수
player = '전국대표'

def FuncPlayer():
    name ='홍길동' #지역변수
    player = '지역대표' #지역변수
    print(name, player)
    
FuncPlayer()#->홍길동 지역대표
#똑같은 player에 '전국대표' 와 '지역대표'생성 but 지역변수가 우선

#중첩 함수: 함수 내 함수
'''
def outer():
    바깥쪽 함수
    def inner():
        안쪽 함수
'''
a = 10 ; b = 20 ;c= 30 #전역변수
def Outer():
    a = 100 # 지역변수
    def Inner():
        global a, c #a,c를 전역변수로 선언
        a = 1000 #전역변수
        c = 300 #전역변수
        print('a:{},b:{},c:{}'.format(a,b,c))
    Inner() #바깥쪽 함수에 안쪽 호출
    print('a: ', a)
    print('c: ', c)

Outer()
#-->a:1000,b:20,c:300
#    a:  100
#    c:  300

#변수영역
v1 = 1 #전역변수
def Var(v1): #매개변수(가인수) - 지역변수
    v1 = v1 + 1
    print(v1)

Var(v1) #전역변수(실인수) -->2  
print(v1) #-->1
Var(b) #b=20, --> 21

'''
지역변수
    - 함수 내에서 선언된 변수
    - 해당 함수가 종료되면 메모리에서 소멸
'''

#Calc()함수 선언 후, 두 숫자를 키보드로 입력받아서 사칙연산을 출력해
def Calc(x,y):
    a = x + y; print('덧셈: ',a)
    b = x - y; print('뺄셈: ',b)
    c = x * y; print('곱셈: ',c)
    d = x / y; print('나눗셈1: ',d)
    e = x % y; print('나눗셈2: ',e)
    return a,b,c,d,e #return으로 해주면 변수에 값 지정, so 함수끝나도 print(a)하면 값이 나옴
    
x = int(input('첫번째 수 입력: '))
y = int(input('두번째 수 입력: '))

#여러개의 값 리턴 가능
a,b,c,d,e = Calc(x, y)
#리턴 변수 값으로 출력 가능
print('a: ',a)
print('e: ',e)