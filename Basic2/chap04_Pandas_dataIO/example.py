'''
문제) 다음과 같은 웹 주소에서 파일을 직접 읽어서 조건에 맞게 처리하시오.
    조건1> http://databank.worldbank.org/data/download/GDP.csv
    조건2> pandas에서 제공되는 read_csv() 이용 파일 읽기
    조건3> 행 번호 없이 'Code','Ranking','Nation','GDP' 칼럼만 파일 저장 
    조건4> 파일 데이터를 읽어와서 상위 20위 국가만 추출하여 변수 저장 
    조건5> 상위 20위 국가의 GDP 대상으로 차트 그리기  
'''

import pandas as pd 

# 1. 웹에서 파일 다운받기-GDP.csv
print('\n웹에서 파일 다운받기-GDP.csv') 
info_url2 = 'http://databank.worldbank.org/data/download/GDP.csv'
data = pd.read_csv(info_url2)
print(data.info()) # DataFrame
print(data[:6]) # 상위 20위 까지 보여줌


# 2. data 전처리 
# (1) 행 번호 없이 파일 저장
data.to_csv('gdp_ranking.csv', index=False)

# (2) 0,1,3행 제외, 칼럼명 지정 파일 읽어오기
name=['Code','Ranking', 'na', 'Nation', 'GDP', 'na', 'na', 'na', 'na', 'na']
gdp_df = pd.read_csv('gdp_ranking.csv', skiprows=[0,1,3], names=name) # 2 : 제목행
print(gdp_df)

# (3) 행 번호 없이, 지정한 칼럼만 파일에 저장
gdp_df.to_csv('gdp_ranking2.csv', index=False, columns=['Code','Ranking','Nation','GDP'])

# (4) 상위 20위 국가만 추출 
gdp_final = pd.read_csv('gdp_ranking2.csv') # skiprows=[1,2]
gdp_ranking20 = gdp_final[2:22] # (millions of에 의해서 생긴 1,2행 제거)


# 3. 상위 20국가의 GDP 순위로 차트 그리기
import matplotlib.pyplot as plt

# 1) DataFrame에서 추출된 칼럼 타입 - Series 객체
gdp20 = gdp_ranking20['GDP'] 
print(type(gdp20)) # Series 객체 

# 2) list 형 변환 
lgdp20 = list(gdp20) # list 변환 
print(type(lgdp20)) # <class 'list'>
print(lgdp20)

# 3) data에서 콤마 제거  -> 숫자형 변환 
num_gdp20 = [] 
for s in lgdp20 :
    num_gdp20.append(int(s.replace(',', '')))
print(num_gdp20)

# 4) 차트 그리기 
plt.plot(num_gdp20)
plt.title('GDP Ranking Top 20') # 차트 제목 
plt.ylabel('GDP') # Y축 이름
plt.xlabel('Nation') # X축 이름 
plt.show() # 차트 보이기 





