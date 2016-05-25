'''
Created on 2016. 5. 23.

1. 기본 생성자 = 묵시적 생성자
2. 클래스 변수(멤버 변수) 초기화
    1) 참조변수 이용
    2) 클래스 이름 이용
'''

class Singer:
    #멤버 변수 = 전역변수7
    title_song = '아름다운 대한민국'
    #기본 생성자 = 묵시적 생성자 정의
    #아래 타이핑 안해도 묵시적으로 생성자 있다고 봄
    #def __init__(self):
    
    #일반 메서드 정의
    def sing(self):
        title = '노래는' #지역변수
        print(title, self.title_song,'랄랄랄')

sing1 = Singer() #객체 생성
#생성자(def __init__) 없이 어떻게 객체가 생성되지? A.묵시적 생성자임, 아래처럼 하면됨
sing1.sing()

sing2 = Singer()
sing2.sing()
print(id(sing1),id(sing2)) #35905776 35907792 두개 다름 

####변수 변경####

#참조 변수 이용
sing2.title_song = '아름다운 파이썬'
sing2.sing()

#클래스 이름 이용
Singer.title_song = '아름다운 우리나라'
print(Singer.title_song)

#멤버 변수 추가 - 참조변수.새로운 변수
sing2.co = 'SM'
print('소속사: ', sing2.co)

print('\nCell phone')
class CallPhone:
    color = None #초기 값 없음
    memory = 32
    price = 500000
    #묵시적 생성
    #일반 메서드 정의
    #변수 초기화 용도
    def setData(self,color):
        self.color = color #초기화
        print('폰 생성 -> 색상:{0}, 메모리:{1},가격:{2}'\
              .format(self.color,self.memory,self.price))
        
        
phone1= CallPhone() #객체 생성
phone1.setData('red')
















