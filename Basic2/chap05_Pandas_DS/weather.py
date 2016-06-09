'''
날씨 데이터 처리 및 시각화
'''

import pandas as pd

# 날씨 관려 파일 가져오기
weather = pd.read_csv('weatherAUS.csv')
print(weather.info())

print(weather.head())
print(weather.tail())

# 특정 행 보기 
print(weather.ix[0]) # ix[행]

# 특정 칼럼 보기 
print(weather['MaxTemp'][:10]) # ['칼럼명'][:행수]
print(weather['Rainfall'][:20])

# 특정 칼럼에 대한 빈도수 구하기
# 형식) frame['칼럼명'].value_counts()
 
# 오후3시 바람방향 = WindDir3pm
windDir3pm_count = weather['WindDir3pm'].value_counts()
print(windDir3pm_count)

# 차트 모듈 추가
import matplotlib.pyplot as plt

windDir3pm_count.plot(kind='bar', rot=45, title='Wind Direction 3pm')
# kind='barh' - 가로막대차트 
plt.show() # 차트 보이기 

# 특정 칼럼을 list 저장 - RainTomorrow - Yes/No/NaN
rainTom = [] # 빈 list

for i in  weather['RainTomorrow'] :
    rainTom.append(i)

print(rainTom[:10])
# ['No', 'No', 'No', 'No', 'No', 'Yes', 'No', 'No', 'No', 'No'] 

# 문) rainTom 변수를 대상으로 Yes,No,NaN의 빈도수를 구하시오.
# NaN = Yes or No가 아닌 경우 
yes = 0; no = 0; nan = 0

for i in rainTom :
    if i == 'Yes' :
        yes += 1
    elif i == 'No' :
        no += 1
    else :
        nan += 1

print('yes:', yes, 'no:', no, 'nan:', nan)

# dict 형식으로 빈도수 구하기 
counts = {} # 빈 set -> dict {yes/no/nan : count} 
for rain in rainTom :
    counts[rain] = counts.get(rain, 0) + 1

print(counts)

# 빈도수를 구하는 함수 정의
def rain_count(data) :
    # 지역변수 
    counts = {} # 빈 set -> dict 생성 
    for rain in data :
        if rain in counts : # counts에 rain이 있는 경우 
            counts[rain] += 1  # 1씩 카운터
        else : # counts에 rain이 없는 경우 
            counts[rain] = 1 # 1 초기화    
    return counts        

# 함수 호출 
counts = rain_count(rainTom)    
print(counts)     

print('내일 비가 오는 경우 = %d'%counts['Yes'])
print('내일 비가 안오는 경우 = %d'%counts['No'])

# 문1) 돌풍의방향(WindGustDir) 칼럼을 대상으로 바람의 방향 별로 빈도수를
# 계산하고 결과를 가로막대차트로 시각화 하시오.
                 
windGustDir_count = weather['WindGustDir'].value_counts()
print('돌풍의 방향 빈도수')
print(windGustDir_count) 

windGustDir_count.plot(kind='barh', rot=45, title='Wind Gust Direction')
plt.show() # 차트 보이기 

# 문2) 바람의 방향별로 카운트하여 dict 자료구조에 저장하는 함수를 정의하시오.
def windGustDir_count(data) :
    # 지역변수 
    counts = {} # 빈 set -> dict 생성 
    for wind in data :
        if wind in counts : # counts에 wind가 있는 경우 
            counts[wind] += 1  # 1씩 카운터
        else : # counts에 wind가 없는 경우 
            counts[wind] = 1 # 1 초기화    
    return counts   

# 함수 호출 : 돌풍의방향을 실인수로 호출 
wind_count = windGustDir_count(weather['WindGustDir'])
print(wind_count)
 
import numpy as np
 
# 3항 연산자 형태로 빈도수 구하기 
# 변수 = np.where('조건식', '참', '거짓')
rainTom2 = np.where(weather['RainTomorrow'].str.contains('Yes'), 'Yes', 'No')
print(type(rainTom2))
print(rainTom2[:20])

# 돌풍의 방향에 따라서 내일 비 유뮤 측정
# 특정 칼럼으로 그룹화 하기
# 형식) frame.groupby(['칼럼명', 그룹화대상변수])
windGustDir_group = weather.groupby(['WindGustDir', rainTom2])
print(windGustDir_group.size())

# 내일 비 유무 결과를 테이블 형식으로 작성 
rainTom_result = windGustDir_group.size().unstack()
print(rainTom_result) 

# 돌풍의방향에 따른 비 유무 시각화 
# stacked=True : 누적형 차트 
rainTom_result.plot(kind='barh', stacked=True) # 가로막대차트
plt.show()








   




