'''
Created on 2016. 5. 23.

클래스(class): 사용자가 직접정의한 자료구조
보통 첫글자 대문자로 씀 ㅋ
자료구조 유형: 1. 내장형 2. 사용자 정의형
내장형: python에서 제공
사용자 정의형: 클래스
자료구조 역할: 객체를 생성하는 역할
    ex) list = [10,20] : data 대상 객체(메모리) ->참조변수(주소 저장)
자료구조 구성요소: 속성(변수)과 기능(메서드)
    1) 속성: data 저장 변수
    2) 기능: data 조작 메서드(함수)
'''
####python의 내장형 자료구조####
print('내장형 자료구조')

#날짜와 시간을 읽을 수 있는 모듈 datetime
import datetime
#1. 날짜 객체 생성: 생성자 메서드
today=datetime.date(2016,5,23) 
#참조변수: 객체의 주소를 갖는 변수, today가 참조변수 
print(today)

#2. 객체 속성: 형식) 참조변수.속성
#today치고 . 누르면 사용가능한 속성 나옴
#ctime()<-메서드, 괄호 없으면 속성,아래 3.참고
print(today.year, '년')
print(today.month,'월')
print(today.day,'일')

#3. 객체 기능: 형식) 참조변수, 메서드()
print('요일:',today.weekday())
#요일: 0 <- 0~4 : 평일, 5:토, 6:일
if today.weekday() == 0:
    print('월요일')
#월요일


'''
클래스: 사용자가 직접정의한 자료구조
    - 구성요소: 속성 = 변수, 기능 = 매서드(함수)
'''
####사용자 정의 함수####
#날짜와 요일을 출력하는 클래스 정의
class Today:
    #클래스 변수 선언
    year = 2016
    month = 5
    day = 23
    #생성자 메서드: 객체를 생성하는 함수
    def __init__(self): #1개 이상의 실인수를 갖는다.
        print('Today 객체 생성')
        print('오늘은{}년 {}월{}일'.format(self.year, self.month, self.day))
        #self: 메서드 내에서 클래스 변수 사용
    
    #일반 메서드: 일반 기능을 제공하는 함수
    def weekDay(self):
        week = today.weekday()
        if week == 0:
            print('월요일입니다')
        
#1. Today 클래스 대상 객체 생성
today2 = Today() #클래스명() -> 생성자(여기서 __init__이 생성됨)->객체(메모리)->참조변수(주소)
#Today 객체 생성
#오늘은2016년 5월23일

#2. 객체 
print('year:',today2.year,'년')
print('month:',today2.month)
print('day:',today2.day)

#3. 객체 기능: 참조변수.메서드(함수)
today2.weekDay()


#생성자 이용 변수 초기화
class Today2:
    #클래스 변수 선언
    year = 0
    month = 0
    day = 0
    #생성자: 객체 생성, 변수 초기화 역할
    def __init__(self, y, m, d): #self - 참조변수(클래스 변수 참조 역할)
        #클래스 변수 초기화 과정
        self.year = y #year에 초기화
        self.month = m
        self.day = d
    #일반 메서드 정의: 날짜 출력
    def datePrint(self):
        print('오늘은{}년 {}월{}일'\
              .format(self.year, self.month, self.day))
    #일반 메서드 정의: 요일 출력
    def weekDay(self):
        week = today.weekday() #요일 리턴
        if week >= 5:
            print('주말입니다')
        else:
            print('평일입니다')

#1. 객체 생성: 생성자(객체 + 초기화)
today3 = Today2(2016,5,23) #3개 실인수로 객체 생성

#2. 객체 속성: 참조변수.속성(변수)
print(today3.year,'년')
print(today3.month)

#3. 객체 기능: 참조변수.메서드(함수)
today3.datePrint() #->오늘은2016년 5월23일
today3.weekDay() #평일입니다

#1개 클래스는 다수 객체 생성 가능
#클래스: 설계도(1개), 객체: 클래스로 만들어진 결과물, 제품(n개)

print('\n자동차 클래스')
class Car:
    cc = 0 #엔진
    door = 4 #문짝
    name = ''
    
    #생성자(이름 없음): 객체 + 변수 초기화
    def __init__(self, cc, name):
        self.cc = cc #self.클래스변수 = 매개변수(앞에꺼가 앞에 있는 cc), __init__에 있는 cc는 뒤에 cc
        self.name = name #name 클래스 변수 추가
    
    #자동차 정보 출력
    def display(self):
        print('자동차 정보: %s의 엔진은 %dcc이고, 문짝은 %d 입니다.'\
              %(self.name,self.cc,self.door))
    #Setter()/Getter()
    #Setter(): 변수 값 지정 역할 메서드(함수임)
    #Getter(): 변수 값 획득 역할 메서드(함수임)
    def setCc(self,cc): #매개변수 있음
        self.cc = cc
    def getCc(self): #return 있음
        return self.cc

car1 = Car(2000,'소나타') #객체 생성
print(car1.cc,car1.name)
car1.display() #참조변수.메서드()

car2 = Car(4000,'그랜져') #객체 생성
print(car2.cc,car2.name)
car2.display() #참조변수.메서드()

car2.setCc(3500) #cc변경
print(car2.getCc()) #cc호출
car2.display() #참조변수.메서드()

#클래스 원형 변수 호출
#원형 변수: 클래스 정의 시 선언한 변수 
print(Car.cc) #cc 원형 변수 호출
print(Car.door)
#Car.name 얘는 원형변수가 아니라 error발생->참조변수.name 호출해야함