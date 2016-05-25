'''
Created on 2016. 5. 23.

class 상속
    - 기존에 만든 class 재사용
    형식) class 자식클래스(부모클래스):
    - 상속 대상: 속성(변수), 메서드(함수)
    - 구조가 유사한 클래스를 정의하는 경우
      부모클래스를 이용하여 공통 멤버 정의
      자식클래스로 상속하여 새로운 클래스 정의
'''
#부모 클래스
class Person:
    say = '난 홍길동 입니다'
    age = 20
    #생성자 정의
    def __init__(self, age):
        print('person 객체 생성')
        self.age = age #변수 초기화
    def PrintInfo(self):
        print('age: {}, say{}'.format(self.age, self.say))
    def Hello(self):
        print('안녕하세요')

#class 이름으로 변수 호출
print(Person.say, Person.age)

#Person 객체
p = Person(33)
print(p.say,p.age)#난 홍길동 입니다 33
p.PrintInfo()
p.Hello()

print()
print('--'*10)

#자식클래스 정의: 부모클래스 상속받아서 자식클래스 정의
#class 자식클래스(부모클래스)
class Employee(Person): 
    say = '일하는 사람이닷'
    def __init__(self):
        print('Employee 객체 생성')
    #객체 정보 출력
    def EmPrintInfo(self):
        self.PrintInfo() #부모에 상속한 메서드 호출!!!
e =  Employee()
print('say:', e.say)
print('say:', e.age)
e.PrintInfo()
e.Hello()

#Woker 클래스 정의: 부모클래스 상속으로 클래스 정의
class Woker(Person):
    say = '작업하는 사아람' #say 내용 수정
    #생성자
    def __init__(self,age):
        self.age = age #변수 초기화 방법1
        #super().__init__(age) <--변수 초기화 방법2
        print('woker 객체 생성')
    #객체 정보 출력
    def WoPrintInfo(self):
        self.PrintInfo()#부모에 상속한 메서드 호출

print('--'*10)
w = Woker(30)
print(w.say)
print(w.age)
w.WoPrintInfo()#객체 정보 출력

#class type 보기 - 출처(조상 확인)
print('\nclass type 보기')
print(Person.__bases__)#(<class 'object'>,)

print(Employee.__bases__)#(<class '__main__.Person'>,) 조상이 Person
print(Woker.__bases__)













































