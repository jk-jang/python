'''
Created on 2016. 5. 12.

예외처리 - run time 과정에서 오류가 발생되는 현상
    형식)
        try: 
            if,예외발생 코드->except로 넘어감
        except: 
            예외처리 구분
        변수: 예외정보가 저장되는 변수
'''
print('프로그램 시작')
try:
    x = 10 / 2
    print(x)
    x = 10 / 0
except: 
        print('예외 발생')
print('프로그램 종료')

#다중 예외 처리 #처음 발생 하는 예외를 뿌려줌
print('프로그램 시작')
try: 
    re = 10 / 2
    re2 = 10 / 0 #산술적 예외
    re3 = 10 / '3' #Type 예외
    re4 = open('c:/test.txt') #파일 불러오기 예외
except ZeroDivisionError as e:
    print('0으로 나눈 산술적 예외')
except TypeError as e:
    print('데이터 타입 예외 발생')
except Exception as e:
    print('나도 모르는 예외, 만능임')
print('프로그램 종료')











