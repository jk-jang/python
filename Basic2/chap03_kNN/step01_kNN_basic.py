'''
kNN 알고리즘 
 - 유클리드안 거래계산식을 적용하여 가장 가까운 k개를
   투표(vote)방식으로 선정하여 분류하는 알고리즘 
'''

import numpy as np # 별칭 
import matplotlib.pyplot as plt # 별칭 

# 1. 두 집단의 x,y 산점도 시각화 
plt.scatter(1.2, 1.1) # A집단 
plt.scatter(1, 1) # A집단
plt.scatter(1.8, 0.8) # B집단
plt.scatter(2, 0.9) # B집단

# 분류 대상 
plt.scatter(1.6, 0.85) # new data 

#plt.show() # 차트 보이기 

# 2. data 생성과 함수 정의
p1 = [1.2, 1.1]
p2 = [1, 1]
p3 = [1.8, 0.8]
p4 = [2, 0.9]
p5 = [1.6, 0.85] # 분류 data 

# data 생성 함수 정의
def data_set() :
    # 두 집단 data 생성 
    points = np.array([p1, p2, p3, p4]) # 4행 2열 다차원 객체 
    labels = np.array(['A','A','B','B']) # y변수
    size = len(points) # 4
    
    # 분류 data 생성 
    xdata = np.tile(p5, (size, 1)) # (반복행수, 반복열수)
    return points, labels, xdata 

# 함수 호출 
points, labels, xdata = data_set()
#print(points)
#print(labels)
#print(xdata)

# 3. 두 집단과 분류데이터와 거리계산
# 유클리안 거리계산식 : 차 -> 제곱 -> 합 -> sqrt()

#xdata = np.array([p5, p5, p5, p5]) # 분류 data 생성 
# tile(data, (반복행수, 반복열수))
#xdata = np.tile(p5, (4, 1))
#print(xdata)

# (1) 점 간의 차 구하기
diffMet  = xdata - points
#print(diffMet)

# (2) 제곱 구하기
sqDiffMet = diffMet ** 2
#print(sqDiffMet)

# (3) 합 구하기
row_sum = sqDiffMet.sum(axis = 1) # 행 단위 합계 
#print(row_sum)

# (4) 제곱근 구하기
distance = np.sqrt(row_sum)
#print(distance) # K=3 -> B:2, A:1
# [ 0.47169906  0.61846584  0.20615528  0.40311289]
#       2(A)        3(A)        0(B)        1(B) 
# [1.6, 0.85] -> B
 

# 4. 거리가 가까운 순서대로 정렬 
sortedDist = distance.argsort() # 오름차순 정렬 -> index 리턴 
#print(sortedDist) # [2 3 0 1]

#print(labels) # ['A' 'A' 'B' 'B']
# 가장 짧은 거리의 범주 출력

# k = 3
#print('가장 짧은 거리의 범주 : %s'%labels[sortedDist[0]])
# 가장 짧은 거리의 범주 : B
#print('가장 짧은 거리의 범주 : %s'%labels[sortedDist[1]])
# 가장 짧은 거리의 범주 : B
#print('가장 짧은 거리의 범주 : %s'%labels[sortedDist[2]])
# 가장 짧은 거리의 범주 : A











