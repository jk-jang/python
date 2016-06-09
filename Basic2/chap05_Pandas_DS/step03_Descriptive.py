'''
DataFrame을 이용한 기술통계량 구하기 
'''

# list를 이용 DF 생성 
name = ['홍길동','이순신','유관순','강강찬']
kor = [70,95,70,76]
eng = [89,75,85,63]
mat = [78,96,74,68]

import pandas as pd 
frame =  pd.DataFrame({'name':name, 'kor':kor, 'eng':eng, 'mat': mat},
                      columns=['name','kor','eng','mat'])
print(frame)

# 기술통계량 구하기 
print(frame.sum(axis = 1)) # 행 단위 합계 - 사람별   
print(frame.sum(axis = 0)) # 열 단위 합계 - 과목별 

print(frame.mean(axis = 0)) # 과목별 평균 
print(frame.max()) # 과목별 최댓값
print(frame.min()) # 과목별 최솟값 

# 요약 통계량 - summary() 유사함
des = frame.describe()
print(des)

# 자료구조 보기 - str() 유사함
info = frame.info()
print(info)

# data 정렬 
sort = frame.sort_values('kor') # 국어점수 오름차순 정렬 
print(sort)

sort = frame.sort_values('kor', ascending=False) # 내림차순 정렬 
print(sort)

sort = frame.sort_values(by=['kor', 'eng'], ascending=False) # 내림차순 정렬 
print(sort)

import numpy as np

# 특정 칼럼 값을 NaN
frame.mat[0, 2] = np.NaN
print(frame)
result1 = frame.sum(axis = 0, skipna = True) # skipna = True
result2 = frame.sum(axis = 1, skipna = True)
print(result1) # 열 단위 합계 - mat    NaN
print(result2) # 행 단위 합계   

# product.csv
product = pd.read_csv('product.csv')
print(product)

print(product.head(10)) # 앞부분 5줄
print(product.tail()) # 뒷부분 5줄   

# 칼럼의 유일한 값 구하기 
a_unique = product['a'].unique()
print('특정 칼럼 유일한 값 구하기')
print(a_unique) # [3 4 2 5 1]

# 칼럼 단위 빈도수 구하기 
# 특정 칼럼 빈도수
a_count = product['a'].value_counts()
print('특정 칼럼 빈도수')
print(a_count)
 
# 전체 칼럼 빈도수 
count = product.apply(pd.value_counts)
print('전체 칼럼 빈도수')
print(count)
'''
     a    b    c
1   30    8    9
2   37   48   45
3  126  119  129
4   64   79   74
5    7   10    7
'''

print('apply()함수 적용')
re = product.apply(sum) # 칼럼 단위 합계 
print(re)





