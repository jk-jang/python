'''
data frame 병합(합치기)
'''

from pandas import DataFrame, Series
import pandas as pd

key1 = ['a','b','c','d','e']
key2 = ['e','a','c']

# range(n) : 0 ~ n-1 정수 = np.arange(n)
df1 = DataFrame({'data1':range(5), 'key':key1})
df2 = DataFrame({'data2':range(3), 'key':key2})

print(df1); print(df2)

# 1. key 항목으로 DF 병합
df_merge = pd.merge(df1, df2)
print(df_merge)
'''
   data1 key  data2
0      0   a      1
1      2   c      2
2      4   e      0
'''

# Outer 조인 = 왼쪽 df 대상 full 조인 
df_outer = pd.merge(df1, df2, how='outer')
print(df_outer)

# Inner 조인
df_inner = pd.merge(df1, df2, how='inner')
print(df_inner) # merge() 동일함 


# 2. Series 객체 병합

s1 = Series([1,3], index=['a','b'])
s2 = Series([5,6,7], index=['a','b','c'])
s3 = Series([11,13], index=['a','b'])

# 행 단위 결합 
result = pd.concat([s1, s2, s3], axis = 0) # 행 단위 결합 
print(result)

# 열 단위 결합
result2 = pd.concat([s1, s2, s3], axis = 1) # 열 단위 결합 
print(result2)


# 3. DataFrame 객체 결합 

import numpy as np

df1 = DataFrame(np.arange(1, 7).reshape(3,2), index=['a','b','c'],
                columns=['one', 'two'])
df2 = DataFrame(3 + np.arange(4).reshape(2,2), index=['a','b'],
                columns=['three', 'four'])

print(df1); print(df2)
'''
   one  two
a    1    2
b    3    4
c    5    6
   three  four
a      3     4
b      5     6
'''

# 칼럼단위 df 붙이기
result3 = pd.concat([df1, df2], axis = 1)
print(result3)
'''
   one  two  three  four
a    1    2    3.0   4.0
b    3    4    5.0   6.0
c    5    6    NaN   NaN
'''
