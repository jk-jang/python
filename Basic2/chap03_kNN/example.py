'''
문) 다음과 같은 3개의 범주를 갖는 6개의 데이터 셋을 대상으로 kNN 알고리즘을 적용하여 
      특정 품목을 분류하시오. 
      
    <조건1> 데이터 셋  
    -------------------------
        품목      단맛   아삭거림  분류 범주
    -------------------------
    grape   8   5     과일
    fish    2   3     단백질 
    carrot  7   10    채소
    orange  7   3     과일 
    celery  3   8     채소
    cheese  1   1     단백질 
    ------------------------
   <조건2> 분류 대상과 k값은 키보드 입력
   
  <<출력 예시 1 : k=3인 경우 >>
     단맛 입력(1~10) : 8
     아삭거림 입력(1~10) : 4
   k값 입력(1~3) : 3
   calssCount: {'과일': 1}
   calssCount: {'과일': 2}
   calssCount: {'과일': 2, '단백질': 1}
     분류결과: 과일

  <<출력 예시 2 : k=2인 경우>>
     단맛 입력(1~10) : 5
     아삭거림 입력(1~10) :8
   k값 입력(1~3) : 2
   calssCount: {'채소': 1}
   calssCount: {'채소': 2}
     분류결과 : 채소

  <<출력 예시 3 : k=1인 경우>>
     단맛 입력(1~10) : 2
     아삭거림 입력(1~10) :3
   k값 입력(1~3) :1
   calssCount: {'단백질': 1}
     분류결과 : 단백질
'''

import numpy as np

p1 = [8, 5]
p2 = [2, 3]
p3 = [7, 10]
p4 = [7, 3]
p5 = [3, 8]
p6 = [1, 1]

x = int(input('단맛 입력(1~10) : '))
y = int(input('아삭거림 입력(1~10) :'))
k = int(input('k값 입력(1~3) :'))

p7 = [x, y] # 분류 대상 

def data_set():   
    points = np.array([p1, p2, p3, p4, p5, p6]) # np의 array() 함수 
    labels = ['과일','단백질', '채소', '과일', '채소', '단백질'] # 분류 범주 
    size = len(points) # 4
    xdata = np.tile(p7, (size, 1)) # 4행 1열 
    return points, labels, xdata # return points, labels - 1차 작성 
 
points, labels, xdata = data_set() # points, labels = data_set() - 1차 작성 

def classify(x, dataSet, labels, k): # 분류 data, 데이터 셋, 분류범주, k값     
    # 단계1 : x와 데이터셋 사이 거리 계산 - 유클리드안 거래 계산식 적용  
    
    # 1) 두 점 간의 차    
    diffMet = xdata - dataSet   
    # 2) 각 원소 제곱  - square
    sqDiffMet = diffMet ** 2 # 각 원소에 제곱        
    # 3) 행 단위 합
    sqDistances = sqDiffMet.sum(axis = 1) # 행 합계     
    # 4) sqrt
    distance = sqDistances ** 0.5 # 각 원소에 0.5 제곱 
        
    # 단계2: 거리가 짧은 순서대로 오름차순 정렬 -> index 반환  
    sortedDist = distance.argsort() # 오름차순 정렬 -> index 리턴  
    
    # 단계3 : 가장 이웃한 k개 선택 : 거리가 가장 짧은 k개 선택  
    classResult = {} # 빈 set 객체 - 분류결과 저장  
    
    for i in range(k) : # 이웃한 k개의 labels과 빈도수를 빈 set에 저장  
        label = labels[sortedDist[i]] # 분류범주 선택       
        classResult[label] = classResult.get(label, 0) + 1
        print('calssCount:', classResult) # calssCount: {'B': 1}
    return classResult 

# 3. 함수 호출  
class_Result = classify(xdata, points, labels, k) # 분류 data, 데이터 셋, 분류범주, k값

# 단계4 : 가장 이웃한 k개 대상 vote 방식으로 분류범주 선택  
cnt_a = 0 ; cnt_b = 0; cnt_c = 0
for i in class_Result.keys() :
    if i == '과일' :
        cnt_a = class_Result[i]
    elif i == '채소' :
        cnt_b = class_Result[i]
    else : # 단백질 
        cnt_c = class_Result[i]

result = [cnt_a, cnt_b, cnt_c]
print(result)

    
if cnt_a >= cnt_b :
    if cnt_a >= cnt_c :
        print('분류결과: 과일')
    elif cnt_c >= cnt_b : # cnt_a < cnt_c 
        print('분류결과 : 단백질')    
elif cnt_b >= cnt_c :
    print('분류결과 : 채소')
else :     
    print('분류결과 : 단백질')
