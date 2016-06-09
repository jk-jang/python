'''
data frame 모양변경과 범주화
'''

from pandas import DataFrame
import pandas as pd
import numpy as np

df = DataFrame(1000 + np.arange(6).reshape(2,3),
               index = ['대전시', '서울시'],
               columns = ['2015', '2016', '2017'])
print(df)

# 1. 칼럼 -> 행으로 구조변경 
print()
df_row = df.stack()
print(df_row)
'''
대전시  2015    1000
       2016    1001
       2017    1002
서울시  2015    1003
       2016    1004
       2017    1005
'''

# 2. 행 -> 칼럼 구조 변경
df_col = df_row.unstack()
print(df_col)     
'''
     2015  2016  2017
대전시  1000  1001  1002
서울시  1003  1004  1005
'''


# 3. 중복데이터 제거
df2 = DataFrame({'data1':['a']*4 + ['b']*4, 'data2':[1,1,2,2,3,3,4,4]})
print(df2)
'''
  data1  data2
0     a      1
1     a      1
2     a      2
3     a      2
4     b      3
5     b      3
6     b      4
7     b      4
'''

result = df2.drop_duplicates()
print(result)
'''
  data1  data2
0     a      1
2     a      2
4     b      3
6     b      4
'''

# data1 빈도수 구하기
counter = result['data1'].value_counts() # 빈도수 
print(counter)
'''
a    2
b    2
'''










