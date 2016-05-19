'''
Created on 2016. 5. 18.

함수의 가변 인수
    형식) 함수명(*가변인수):
    - 여러개의 실인수를 한 개의 변수로 받음!
    - 실인수를 tuple 타입으로 저장
'''
def Func1(*name): #가변인수 선언
    print(name)
    for i in name:
        print(i)
        
Func1('홍길동', '이순신','강감찬') #실인수 3개

def Func2(addr1, *addr2):
    print(addr1) #서울시
    for a in addr2:
        print(a) #인천 광주 부산

Func2('서울시','인천시','광주시','부산시')

'''
문)Func3(func, *data), 
    func = max 이면 data의 최댓값 출력
    func = sum 이면 data의 합계 출력
    func = avg 이면 data를 대상으로 평균 출력
'''
def Func3(func,*data):
    if func == 'max':
        print('max= ', max(data))
    elif func == 'sum':
        print('sum =',sum(data))
    else:
        print('avg= ', sum(data)/len(data))

#함수 호출
Func3('max',1,2,3,4,5)
Func3('sum',1,2,3,4,5)
Func3('avg',1,2,3,4,5)

print('\n잔여 데이터')
def Person(w, h, **other): #**other: 가변인수->dict타입으로 저장
    print('몸무게: ',w) 
    print('키: ', h)
    print(other)
    for o in other.keys():
        print(o)

Person(65,175, name='홍길동',age=35)
'''
잔여 데이터
몸무게:  65
키:  175
{'name': '홍길동', 'age': 35}
name
age
'''
'''
1. 축약함수(lambda)
    - 함수명이 없는 한 줄짜리 함수를 의미
    형식) lambda + 가인수: (반환값) 
    ㅇㅖ) lambda x,y: x + y #함수 정의 
    ㅇㅖ) (lambda x,y: x + y)(10,2) #정의 및 호출 동시에~ -->12
     
2. 중첩함수(inner)
    - 

'''
#사용자 정의 함수def vs #축약함수lambda
#1. 사용자 정의 
def Add(x,y):
    return x+y
print(Add(10,20)) #30

#축약함수
print((lambda x,y:x+y)(10,20)) #30

#중첩함수
def main_def(init_value): #1. outer함수
    result = init_value #result 변수 초기화
    def getResult():#Inner 함수1 : result 변수값 확인
        print(result)
    def plus(x,y):
        nonlocal result #outer 함수에 선언된 변수(1.에있는 변수) 사용
        print('result +x:',result + x)
        result = x + y
        print(result)
    def minus(x,y):
        result = x - y
        print(result)
    return getResult, plus, minus #함수 주소가 리턴!!->내부함수(inner)를 쓸 수 있음 파이썬 장점

g, p, m = main_def(100)
g()
p(10,20)
m(100,50)

#재귀함수 호출: 자기 자신을 함수로 호출
#if문 + for문 결합한 형식
def Counter(n):
    if n == 0:
        print('완료')
    else:
        print(n, end=' ')
        Counter(n-1) #재귀함수

Counter(5) #5 4 3 2 1 완료

#문) 팩토리얼 계산하는 재귀함수 정의
#ex)n=5 5*4*3*2*1 = 120

def Factory(n):
    result = 0
    if n == 1:
        return 1 #n=1인 경우 1 리턴
    else:
        result = n*Factory(n -1) #Factory만 계속 바뀜,앞에 있는 n은 안바뀜
        #5*factory(5-1)*factory(4-1)*factory(3-1)*factory(2-1)*1
        print(result)
        return result

n = int(input('n값을 입력하시오: '))
result = Factory(n)
print('%d의 팩토리어 값 = %d'%(n, result))
