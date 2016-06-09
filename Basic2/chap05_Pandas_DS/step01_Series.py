'''
Series 객체 특징
 - 1차 배열구조를 갖는다.
 - pandas에서 제공하는 자료구조
 - DataFrame에서 특정 칼럼을 추출 -> Series
   -> DataFrame의 칼럼 구성시 사용
 - numpy 객체와 공통점
   -> 유니버설 함수 적용
   -> index와 슬라이싱 가능
   -> DF에 칼럼으로 구성
 - numpy 객체와차이점 
   -> numpy vs pandas 제공
   -> 다차원배열 vs 1차 배열     
'''

#import pandas

from pandas import Series
import numpy as np

# list vs Series 차이점
li = [2,8,-5,4,7]
print(li) # [2, 8, -5, 4, 7]

obj = Series([2,8,-5,4,7]) 
print(obj)

'''
  list vs Series 차이점
    - 행 index가 자동으로 생성
'''
print(obj.values) # [ 2  8 -5  4  7]
print(obj.index) 

# Series에서 index 
obj2 = Series([1,2,3,4,5], index=['a','b','c','d','e'])
print(obj2)

# index 활용
print(obj2['d']) # 4
print(obj2['b':'d']) # index 범위 지정 
obj2['d'] = 40 # index 값 수정 
print(obj2)
obj2['a':'c'] = 400 # index 범위로 값 수정 
print(obj2)

# 특정 원소 대상 연산 가능 
obj3 = obj2 * 2 # 연산 -> new object 생성 
print(obj3)

# 유니버설 함수 적용
rsum = np.sum(obj3) # obj3 합계 
print(rsum)

rmean = np.mean(obj3)
print(rmean)

rmax = np.max(obj3)
print(rmax)

rmin = np.min(obj3)
print(rmin)

'''
 numpy vs series 공통점
  - 유니버설 함수 적용
  - indexing과 슬라이싱 
  - index를 이용하여 범위 수정 가능 
  - 원소별 연산이 가능
'''

# python 자료구조 이용 Series 객체 생성 

# 1) dict 자료구조 -> Series 객체 생성 
data = {'name':'홍길동','age':35, 'pay':350}

obj4 = Series(data)
print(obj4)

# 2) list 자료구조 -> Series 객체 생성 
name = ['홍길동','이순신','유관순']
pay = [350, 400, 250]

obj5 = Series(pay, index = name)
print(obj5)

name2 = ['강감찬','이순신','유관순']
bonus = [0, 100, 25]
obj6 = Series(bonus, index = name2)
print(obj6)

obj7 = obj5 + obj6
print(obj7)
print(type(obj7))
'''
강감찬      NaN <- ojb5 없음
유관순    275.0
이순신    500.0
홍길동      NaN <- obj6 없음 
'''

# NaN 특정 값으로 채우기
result = obj7.fillna(obj7.mean())
print(result)

# NaN 특정 값으로 채우는 함수 정의 
def userFillNa(obj):
    return obj.fillna(obj.mean())

# 함수 호출 
result2 = userFillNa(obj7) # 외부함수 적용 
print(result2)


