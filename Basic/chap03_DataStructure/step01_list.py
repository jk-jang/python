'''
Created on 2016. 5. 16.
List 자료 구조
    - 1차원 배열 구조
    형식) 변수 = [값1, 값2, ...]
    - 여러개 값 저장 가능
    - 변수에 저장된 값은 index 참조 가능
        형식) 변수[index]->num[2]:3번째 원소 참조
    - 순서 존재, 값 변경(추가, 수정, 삽입, 삭제) 가능
'''
#list 생성
a = ['a','b',',','d']
print(a)

#list 중첩
b = [10, a, 20.5, True,'문자열'] #R에서는 동일한 유형만 저장가능
print(b)
#[10, ['a', 'b', ',', 'd'], 20.5, True, '문자열']

print('\n')
num = ['one', 'two','three','four']
print(num)
print('길이:',len(num))
print('index값 보기:',num[2])

#원소 추가
num.append('five') 
print(num)

#원소 삭제
num.remove('five')
print(num)

#원소 삽입
num.insert(0, 'zero')
print(num)

#원소 확장
expension=['육']
num.extend(expension)
print(num)

#원소 결합
y=[1,2]
z=num + y
print(z)

#list 검색
print('\n list 검색')
print(num.index('three'))
print('two' in num,'사' in num)

#list 중첩에서 첨자 사용
data = [1,2,3,['a','b','c'],4,5]
print(data[2]) #3
print(data[3]) #['a', 'b', 'c']
print(data[3][1]) #b

#list 중첩에서 원소 제거
data.remove(4)
print(data)
del data[3]
print(data)

#list 정렬
data.sort(reverse=True) #내림차순
print(data)
data.sort()
print(data)

#list의 matrix
matrix = [[1,2,3],[4,5,6]]
print(matrix)
a = matrix[1][2] #2행 3열
print('2행3열:',a) #6

#문자열을 대상으로 문자를 list에 저장
st = '대한민국 우리나라'
ch = [] #빈 list 생성
'''
    for 변수 in 자료구조(list,tuple,set)& string:
        실행문
'''

for s in st:
    ch.append(s)
print(ch)

print('\성적 처리(국어 영어 수학)')
hong = [50,30,30]
lee = [10,50,20]
kang = [64,60,16]
student = [hong, lee, kang]
print('\n학생성적: ',student)
chh =[]
for s in student:
    chh.append(s)
print('\n',chh)


'''
문제) 홍길동 --> 국어:90, 영어:85, 수학:78
      이     -->             "
'''
names= ['홍','이','강']
i = 0
for score in student:
    print('{0}==>국어:{1} 영어:{2} 수학:{3}'\
          .format(names[i],score[0],score[1],score[2]))
    i = i+ 1

#list 복사: 주소 복사(얕은 복사)
names2 = names

names[0]= '수잔'
print(names2, names)
#['수잔', '이', '강'] ['수잔', '이', '강']
print(id(names2),id(names))
#36308680 36308680

#list 복사: 깊은 복사
#!깊은 복사 vs 얕은 복사
#!얕은 복사는 주소를 복사, 깊은 복사는 객체를 복사
import copy #copy모듈 추가
names3 = copy.deepcopy(names)
print(names3,names)
names[0] = '탐'
print(names3,names)
#['수잔', '이', '강'] ['탐', '이', '강']
print(id(names3),id(names))
#36278984 36308680
























