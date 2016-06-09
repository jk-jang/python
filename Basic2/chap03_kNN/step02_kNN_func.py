'''
kNN 알고리즘 적용 사용자 함수 정의
'''

# 1. data set 가져오기

# from 패키지명.모듈명 import 함수명 
from ex.step01_kNN_basic import data_set
import numpy as np 

points, labels, xdata = data_set() # 함수 호출
print(points)
print(labels)
print(xdata)

# 2. 분류알고리즘 적용 함수 
def classify(x, dataSet, lables, k) : # 분류대상, 두집단, y변수, k값
    # 단계 1: 유클리드안 거리계산식 이용 - 거리 계산
    diffMet = x - dataSet # 차 구하기
    sqDiffMet = diffMet ** 2 # 곱 구하기
    row_sum = sqDiffMet.sum(axis = 1) # 행 단위 합계
    distance = np.sqrt(row_sum) # 제곱근 구하기 
    
    # 단계 2: 가까운 거리 순으로 오름차순 정렬 
    sortedDist = distance.argsort() # index 리턴 
    
    # 단계 3: 이웃한 k개를 선정하여 리턴
    classResult = {} # 빈 set 생성 -> key:value(dict) -> B : 2, A : 1
    for i in range(k) : # k만큼 반복(0~2)
        label = labels[sortedDist[i]] # B -> A
        # {label : value} -> classResult(B : 2)
        classResult[label] = classResult.get(label, 0) + 1
        print('classResult:', classResult)
    return classResult
    
# 함수 호출 
classResult = classify(xdata, points, labels, 3)
print(classResult)  # {'B': 2, 'A': 1}

# 단계4 : 투표방식으로 분류 결정
a_cnt = 0; b_cnt=0
for c in classResult.keys() :
    if c == 'A' : # key가 A인 경우 
        a_cnt = classResult[c] # A의 value 값
    if c == 'B' : # key가 B인 경우 
        b_cnt = classResult[c] # B의 value 값
            
if a_cnt >= b_cnt :
    print(a_cnt) # 1
    print('새로운 data는 A로 분류됩니다.')
else :
    print(b_cnt) # 2 
    print('새로운 data는 B로 분류됩니다.')    
        


li = ['a','b','a','a','b']
classTest = {} # 빈 set 생성
for i in li : # 5회 반복
    # classTest 변수에 key:value 객체 생성 -> a : 3, b : 1
    classTest[i] = classTest.get(i, 0) + 1

print(classTest) # {'a': 3, 'b': 2}    
    
    







