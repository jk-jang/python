'''
Created on 2016. 5. 16.

set 자료구조
    - 집합 구조
    형식) 변수 = {값1, 값2, ...}
    - 순서 없음(index 불가)
    - 값 변경(추가, 제거)
    - 범주 조회(성별: 남, 여)
'''
#set 객체 생성
s = {1,2,3,4,2}
print(s,'길이',len(s)) #중복되면 삭제 됨, 길이 4

s2 = {3,4,5}
print(s.union(s2)) #합집합
print(s.difference(s2)) #차집합
print(s.intersection(s2)) #교집합

#연산자 이용 방법
print(s - s2, s|s2, s&s2)#차집합, 합집합, 교집합
print('\n원소추가')
s2.add(6)
print(s2)

print('\n원소제거')
s2.discard(6)
print(s2)
s2.remove(5)
print(s2)

print('\n새로운 객체를 원소 추가')
s2.update({6,7}) #set 추가
s2.update([8,9]) #list 추가
s2.update((10,11)) #tuple 추가
print(s2)

#list 중복 원소 제거
gender = ['남자','여자','남자']
print(gender)
#sgender = set(gender)
#sgender = list(sgender)
sgender = list(set(gender))
print(sgender)
#











