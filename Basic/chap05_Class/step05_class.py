'''
Created on 2016. 5. 24.

클래스 다중 상속
    - python, c++ : 다중 상속 가능
        class Child(Parent1, Parent2,...)
    - java: 단일 상속
        class Child(parent): 
'''
class Tiger:
    data = '수양대군(이정재)'
    def Cry(self):
        print('세조되다')
    def Eat(self):
        print('단종 꺼져 왕위 내놔')
class Lion:
    def Cry(self):
        print('밀리터리덕, 문종')
    def Hobby(self):
        print('동생아(수양대군) 단종 잘 부탁해')

####다중 상속1
class Liger1(Tiger, Lion):
    pass # 클래스 내용 없음
#위에서 Cry어느것이 우선순위일까
#먼저 상속받은 Tiger 의 Cry가 우선순위

l1 = Liger1() #객체 생성
#참조 변수를 통해서 메서드 호출
l1.Cry()
l1.Eat()
l1.Hobby()

####다중 상속2
class Liger2(Tiger, Lion):
    #부모(Tiger)가 data를 이미 선언했는데 자식에서 선언하면 우에 될까?
    data = '예종'
    def Play(self):
        print('아빠(세조)나 1년만에 하늘간당')
        super().Hobby() #부모클래스의 메서드 호출
    def Printing_data(self):
        print('현재클래스data:',self.data)
        print('부모클래스data:',super().data)

l2 = Liger2()        
print(l2.data)
l2.Play()
l2.Printing_data()

'''
자식클래스에서 부모 멤버 호출
    멤버(member): 변수 + 메서드
    형식) super().메서드() or super().변수
'''


























    
