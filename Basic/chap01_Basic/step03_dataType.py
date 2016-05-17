'''
Created on 2016. 5. 12.
    자료형(data Type)
    1. python 자료형
    2. 형 변환(문자열 -> 숫자)
    3. 문자열 객체 처리
    4. python 자료구조(list, tuple, set, dict)
'''
# 키보드로 데이터 입력
'''
v1 = input('v1 입력 : ')#콘솔창에서 입력
v2 = input('v2 입력 : ')
print(v1);print(v2)
v1=int(v1) #문자열 -> 숫자
'''
#자료형 선언이 없다
#데이터에 의해서 자료형이 결정된다.(R이랑 동일)
print(7, type(7))
print(7.2, type(7.2))
print(True, type(True))
print('abc', type('abc'))
a=100
print(a,type(a))
'''
7 <class 'int'>
7.2 <class 'float'>
True <class 'bool'>
abc <class 'str'>
100 <class 'int'>
'''
#2, 8, 16진수
print('\n진법표현')
print(10, bin(10),oct(10),hex(10))
#10 0b1010 0o12 0xa
print(10, 0b1010, 0o12, 0xa)
'''
문자열 처리 방법
- 문자열 객체 = 문자열 상수(수정 불가)
    --> 수정할 시, 새로운 객체가 생성
- 문자열을 슬라이싱 가능: index 이용해 개별 문자 분리

python index 0부터 시작 R은 1부터 시작
'''
st='0백2제 5땅7따9먹기 근초고왕 신라통일 문무왕'
#글자 길이 
print(len(st)) #16
#글자 갯수
print('왕 글자 갯수: ', st.count('왕'))
#Index 적용
print(st.find('왕',10))#Index(10)이후의 '왕'을 찾아
#15가 나오는데 문자 길이가 16이고 젤 끝의 글자가 '왕'이다
#파이썬은 0부터 시작이니깐 길이와 index는 다름
#따라서 위치가 15면 1부터 시작할 경우 16을 뜻함
#첫 글자 확인
print(st.startswith('백')) 
#문자열 슬라이싱
print(st)
print(st[0],st[0:4],st[:4]) #4이전까지
print(st[2:])#2제 5땅7따9먹기 근초고왕 신라통일 문무왕

#문자 슬라이싱
print(st[::2])#:: 2씩 증가하여 슬라이싱
#오른쪽 기준 슬라이싱
print(st[-1],st[-4:-1]) 

st4 = st.split(sep=' ')
print(st4) #list 객체 리턴

#문자 결합
print(': '.join(st4))

#문자 교체
print(st)
st5 = st.replace('근초고왕','준규')
print('st5: ',st5)
'''
자료구조(index 사용가능:1,2)
    1. list: 1차원 배열
    2. tuple: 1차원 배열
    3. set: 순서없는 공간으로 저장(index가 없다)
    4. dict: key:value 저장
'''
#1. list
li=['a',1,'b']
print(li,type(li))
li.append(st5[1:4])
print(li)

#2. tuple
t=(1,3,4)
print(t[1])

#3. set
s = {1,2,3}
print(s, type(s))

#4. dict
d = {'name' : '문무왕', 'country' : '통일신라'}
print(d, type(d)) #random하게 출력 
#key 접근 가능
print(d['name'])
