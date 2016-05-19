'''
Created on 2016. 5. 17.

함수(function)
    - 내장함수와 사용자 정의 함수
    1. 내장함수 : 기본제공
    형식) 함수명([인수])
    2. 사용자 정의함수
    형식) def 함수명([인수]):
        실행문
        실행문
        [return<반환값>] <--요건 생략가능
'''
ldata = [1,2,3,4,5]
print('합:',sum(ldata))

#문자열을 숫자로 변경
a = 10.3
b = eval('a + 23.145')
#a를 숫자로 인식하고 돌아감
print(b)
#반올림
print(round(b,2))

#수학관련 모듈 추가
import math
#무조건 반올림
print(math.ceil(b))
#무조건 절삭
print(math.floor(b))

ldata2=[1,2,3,9,5,5,3,4]
print('모든 숫자가 10미만?')
print(all(ldata2))
print(all(a <10 for a in ldata2)) #and - True
print(any(a <10 for a in ldata2)) #or - True

#여러 개의 자료구조를 하나로 묶기
x = [10, 20 ,30]
y = [100, 200, 300]
z= zip(x, y)
print(z) #object
#z객체 내용 확인
for i in z:
    print(i)

##메모리 상의 객체 확인
print(globals()) 

#인수가 없는 함수 정의
def userFunc():
    print('userFunc 함수 실행')

userFunc() #userFunc 함수 실행

print(userFunc) #<function userFunc at 0x00000000020FCC80>
userFunc2 = userFunc #주소할당 
userFunc2() #userFunc 함수 실행 <-동일한 함수가 되었음

#인수가 있는 함수 정의
def userFunc2(x,y): #가인수
    add  = x + y
    print(add)

userFunc2(10, 20) #30

#리턴 값이 있는 함수 정의
def userFunc3(x,y):
    tot = x + y
    return tot #반환값

print(userFunc3(100, 200)) #300
new_tot = userFunc3(1000, 2000)
print(new_tot * 2)

print(userFunc3('장', '김')) #장김

#사다리꼴 넓이 계산 함수 
def areaCalc(x,y,z):
    area = ((x+y)*z)/2
    areaPrint(area) #함수 내에서 다른 함수 호출!!
    print('사다리꼴 넓이 %d'%area)

def areaPrint(area):
    print('사다리꼴 넓이 %d'%area)
    
areaCalc(1, 3, 30)