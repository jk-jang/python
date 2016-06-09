'''
Pandas 패키지에서 제공하는 함수 이용 시각화 

  형식) pandas 객체 이용 시각화
  pandas객체.plot(속성값, ... ) -> 차트 생성
  plt.show() -> matplot 제공 함수 차트 보이기 
  pandas객체 : Series객체, DataFrame객체   
  
  cf) Matplot 객체 이용 시각화 
  plt.plot(data객체) -> 차트 생성
  plt.show()
'''

from pandas import Series, DataFrame
import numpy as np

# 1. Series 객체 시각화 
# index : x축 이름, random : y축 
se = Series(np.random.randn(10).cumsum(),
            index = np.arange(0,100,10))
se.plot(color='g') # default : color='b' - 차트 생성 

import matplotlib.pyplot as plt
plt.show() # 차트 보이기 

# 2. DataFrame 객체 시각화 - 10행4열 
df = DataFrame(np.random.randn(10,4), 
               index=np.arange(0,100,10), 
               columns=['one','two','three','four'])
print(df)

df.plot() # 기본 속성(선 그래프)으로 차트 생성 
plt.show()

# 행렬 데이터 시각화 - 밀도분포 곡선 : kde
df.plot(alpha=0.8, kind='kde', title='density curve chart') # 차트 생성
plt.show()

df.plot(alpha=0.8, kind='bar', title='bar chart') # 세로 막대 차트 생성
plt.show()

df.plot(alpha=0.8, kind='barh', title='barh chart') # 가로 막대 차트 생성
plt.show()

# 가로 누적 막대 차트 생성
df.plot(alpha=0.8, kind='barh', stacked=True,  title='stacked chart')
plt.show()


'''
 tips.csv 데이터 셋 설명 
  - 요일별로 파티 규모(size)와 총 결제금액 대비 팁 비율로
    기록된 데이터 셋 이다.
'''

import pandas as pd
tips = pd.read_csv('tips.csv')
print(tips.info())

# day(요일)와 size(파티규모) 교차테이블 -> 빈도분석
party_count = pd.crosstab(tips['day'], tips['size']) # 교차테이블 생성 
print(party_count)
'''
size  1   2   3   4  5  6
day                      
Fri   1  16   1   1  0  0
Sat   2  53  18  13  1  0
Sun   0  39  15  18  3  1
Thur  1  48   4   5  1  3
'''

# size = 2 ~ 5 선택 
party_result = party_count.ix[:, 2:5] # 2~5칼럼 선택
print(party_result)

party_result.plot(kind='barh', stacked=True, title='day and size')
plt.show()

'''
평일 보다 주말에 파티 행사가 많고,
특히 규모가 큰 파티 행사가 주말에 많았다.
'''




