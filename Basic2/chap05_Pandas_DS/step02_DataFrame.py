'''
DataFrame 자료구조 특징
 - DB Table과 유사한 자료구조
   -> 서로 상이한 칼럼을 갖는다.
 - 2차원 행렬구조 갖는다.
 - python 기본 자료구조, Series, Numpy 이용 객체 생성 
 - R의 dataframe과 유사함  
'''

import pandas as pd

# 1. python 기본 자료구조 이용 객체 생성 

# 1) list 객체 이용
name= ['홍길동','이순신','강감찬','유관순']
age = [35,45,55,25]
pay = [350,450,500,250]
addr = ['한양시','전남시','평양시','충남시']

frame = pd.DataFrame({'name':name, 'age':age, 'pay':pay, 'addr':addr})
print(frame)

# 2) dict 객체 생성
data = {'name':name, 'age':age, 'pay':pay, 'addr':addr}
frame2 = pd.DataFrame(data) # dict 객체 이용 
print(frame2) # 칼럼명은 오름차순 정렬 

# DataFrame 객체 생성 - 칼럼 순서 지정
frame3 = pd.DataFrame(data, columns=['name', 'age', 'pay', 'addr'])
print(frame3)

# 칼럼명으로 검색 
print(frame3['name']) # ['칼럼명']
print(frame3.pay) # 참조변수.칼럼명
print(frame3.columns) # ['name', 'age', 'pay', 'addr']

# 2개 이상 칼럼 검색 
# print(frame['name', 'addr']) # error 발생 
col = ['name', 'addr', 'pay'] # 2개 이상 칼럼 검색 
print(frame3[col])


# 2. index 적용 DataFrame 생성 
# - 기본 index : 0 1 ...

frame4 = pd.DataFrame(data, columns=['name','age','pay','addr'],
                      index=['a','b','c','d'])
print(frame4)

# DF에 새로운 칼럼 추가하기 
gender = pd.Series([1,1,2], index=['b','c','d'])
frame4['gender'] = gender
print(frame4) # 홍길동 NaN

# DF에서 칼럼 제거하기 
del frame4['gender'] # del ['제거할 칼럼명']
print(frame4)


import numpy as np 

# 3. DataFrame에서 다양한 검색방법
# numpy 객체 생성 - 0 ~ 11 ->  3행 4열
frame5 = pd.DataFrame(np.arange(12).reshape((3,4)),
                      columns = ['one','two','three','four'])
print(frame5)
'''
   one  two  three  four
0    0    1      2     3
1    4    5      6     7
2    8    9     10    11
'''

# 1개 칼럼 검색
print(frame5['three'])

# 2개 칼럼 검색
#print(frame5['two', 'four']) # error 발생 
print(frame5[['two', 'four']]) # 방법2

# 조건으로 검색
print(frame5[frame5 >= 5])

# 특정 조건의 원소를 0으로 처리
frame5[frame5 < 5] = 0  # 5미만인 원소는 0으로 처리 
print(frame5)


# ix 속성 - index 이용 행 검색
print(frame5.ix[1]) # 2행 검색
print(frame5.ix[2]) # 3행 검색   

# 행과 열 검색 
print(frame5.ix[1,2]) # 2행 3열 - 6
print(frame5.ix[[1,2]]) # 2~3행 
print(frame5.ix[[1,2], [3,2,1]]) # 2,3행 4,3,2열 

# 4. DataFrame 행과 열 제거 
print(frame5) 
'''
   one  two  three  four
0    0    0      0     0
1    0    5      6     7
2    8    9     10    11
'''
# 행 제거 
frame6 = frame5.drop(1, axis=0)
print(frame6) # axis=0 : row 의미 
# 열(칼럼) 제거

print(frame6.drop('three', axis = 1)) # axis=1 : column 의미 




