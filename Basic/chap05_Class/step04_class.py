'''
Created on 2016. 5. 23.

메서드 재정의(method overriding)
    - 클래스 상속에서 발생하는 용어
    - 자식클래스에서 부모의 메서드 원형을 수정
'''
#부모클래스
from _ast import Num
class Parent: 
    #일반 매서드 - 매개변수 없음
    def PrintData(self):
        pass #내용없음

#자식클래스
class Child1(Parent):#자식클래스(부모클래스)-상속
    def PrintData(self): #매서드 재정의
        print('child1 클래스 재정의~~')

ch1 = Child1() #객체 생성 - 기본 생성자 위에서 객체가 만들어짐
ch1.PrintData() #참조변수.매서드명()

#자식클래스2
class Child2(Parent):
    #자체변수(속성) 선언
    num = 0
    def __init__(self, num):
        print('child2 클래스 객체 생성 완료')
        self.num = num #변수 초기화
    #매서드 재정의, 요건 부모로부터 받은 거 
    def PrintData(self):
        print('child2 클래스~') 
    #일반 매서드 정의
    def PrintNum(self): 
        print('num=%d'%self.num)

ch2 = Child2(100) #생성자 -> 객체(Object) -> 주소 리턴 -> ch2(참조변수)
print(ch2.num) #참조변수.속성
ch2.PrintData()
ch2.PrintNum()
#########################<---??????????????###########################
####클래스 형변환=객체 다형성#### 

#자식들
print()
ch1 = Child1()
ch1.PrintData()
ch2 = Child2(100)
ch2.PrintData()
#부모
#자식에서 전한 걸 내가 쓸래
p = Parent()
p = ch1 #업캐스팅(형변환): 자식 -> 부모
print('자식1 -> 부모')
p.PrintData()#부모 참조변수로 자식 멤버 호출

p = ch2 
print('자식1 -> 부모')
p.PrintData()

        



































