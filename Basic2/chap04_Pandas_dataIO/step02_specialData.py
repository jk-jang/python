'''
1. DataFrame 형식으로 저장
2. json 데이터 처리
3. excel 데이터 처리
4. web에서 주식 데이터 읽기 
5. web에서 파일 다운로드
'''

# from 패키지명 import 함수 
import pandas as pd # 별칭 
from pandas import DataFrame # table 객체 생성 

# 1. DataFrame 형식으로 저장 - 학번 이름 성적 

# 1) dict 객체 -> DataFrame 
# 형식1) key(1) : [value(1)] <- 주의 사항 
data = {'name':['홍길동'], 'age':[35], 'addr':['서울시 강남구']}
print(data) # key는 random

# columns : 칼럼명, 순서 지정 
frame = DataFrame(data, columns=['name','age','addr'])
print(frame)

# 형식2) key(1) : [value(n)]
data2 = {'name':['홍길동','유관순'], 'age':[35,20], 'addr':['서울시 강남구','인천시 인천구']}
frame2 = DataFrame(data2, columns=['name', 'age', 'addr'])
print(frame2)

# 2. json 데이터 처리
 
# (1) 멀티라인으로 json 데이터 생성 
# - 형식1) {"key":["value"]}
obj = """
{
  "name":["홍길동"],
  "age" : [35],
  "pay" : [350],
  "addr" : ["서울시 강남구"]
}
""" 

# json 데이터 -> 객체 생성
import json # json 모듈 추가
result = json.loads(obj) # 1) json 변수 로드 -> dict 객체 리턴  
print(result)
# {'age': [35], 'addr': ['서울시 강남구'], 'pay': [350], 'name': ['홍길동']}

# 2) dict -> DataFrame 객체 생성 
data3 = DataFrame(result, columns=['name','age','addr','pay'])
print(data3)

# - 형식2) {"key":[{"key": "value"}]}
obj2 = """
{
  "products" : [
    {"name" : "우유", "price" : "2000"},
    {"name" : "커피", "price" : "3000"},
    {"name" : "주스", "price" : "2500"}
  ]
}  
"""

# json 데이터 가져오기 -> dict 객체 
result2 = json.loads(obj2) # dict 객체 리턴 
print(result2)

# dict -> DataFrame 변환 
data4 = DataFrame(result2['products'], columns=['name','price'])
print(data4)

# (2) 파일로 제공하는 json 데이터 처리 
import codecs # 모듈 추가

# 유니코드 파일 읽기 
f = codecs.open('usagov_bitly.txt', mode='r', encoding='utf-8')
# 줄 단위 데이터 읽기
recodes = [json.loads(data)  for data in f]
# 1줄 읽기(data) -> json 데이터를 dict 변환 -> 변수 저장 
print(recodes[0]) # 첫줄 보기 
print(len(recodes)) # 3560
print(recodes[3559]) # 마지막줄 보기 
data5 = DataFrame(recodes)
print(data5.info())
'''
RangeIndex: 3560 entries, 0 to 3559
Data columns (total 18 columns):
'''

# 3. excel 파일 가져오기 
std_xlsx = pd.ExcelFile('student.xlsx')
print(std_xlsx) # ExcelFile 정보 출력 
table = std_xlsx.parse('student') # 엑셀의 시트 이름으로 파싱
print(table)

# 4. web에서 주식 데이터 가져오기
'''
pandas 라이브러리에서 제공하는 DataReader()함수로
야후, 구글의 주식데이터를 가져올 수 있음
'''

from pandas.io import data
import datetime

# 조회할 시작과 종료 날짜 지정 
start = datetime.datetime(2016, 5, 1)
end =  datetime.datetime(2016, 5, 30)

''' 
yahoo 주식 정보 
1. www.yahoo.com
2. Finance 링크 클릭
3. 기업 입력 -> 주식 코드 제공 
'''

samsung = data.DataReader("005930.KS","yahoo", start, end)
print('yahoo에서 가져온 삼성 주식정보')
print(samsung)


gs_holding = data.DataReader("078930.KS","yahoo", start, end)
print('yahoo에서 가져온 GS 홀딩스 주식정보')
print(gs_holding)

'''
1. www.google.com/finance
2. 기업정보 -> 주식코드 확인
'''

samsung2 = data.DataReader("KRX:005930", "google", start, end)
print('구글에서 가져온 삼성 주가정보')
print(samsung2)

# 기아 모터스 주식data 가져오기 - 2015.5 ~ 2016.5
start = datetime.datetime(2015, 5, 1)
end = datetime.datetime(2016, 5, 30)
kia = data.DataReader("KRX:000270", "google", start, end)
print('구글에서 가져온 기아 모터스 주가정보')
print(kia)
print(kia.info())

# 5. 웹에서 파일 다운로드하기
import requests

# 1. 해당 url에서 data 요청 
url = "https://api.github.com/repos/pydata/pandas/milestones/28/labels"
result = requests.get(url) # 해당 url에서 data 요청 
print(result) # <Response [200]> -> 요청 성공시 200번 

# 2. json 형식으로 data 가져옴
data = result.json() # json 형태로 data 가져옴
print(data) # json data 출력 

# 3, json -> DataFrame 형 변환 
data_df = pd.DataFrame(data)
print(data_df) # color     name     url



