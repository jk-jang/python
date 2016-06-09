'''
DataFrame 기본 연산
'''

from pandas import DataFrame
import numpy as np

# DataFrame 생성 
frame1 = DataFrame(np.arange(0,9).reshape(3,3),
                   columns=list('abc'))
frame2 = DataFrame(np.arange(1,10).reshape(3,3),
                   columns=list('abc'))
print(frame1)
print(frame2)

# frame 덧셈
add = frame1.add(frame2)
print(add)

# frame 뺄셈
sub = frame2.sub(frame1)
print(sub)

# frame 나눗셈 div = frame2 / frame1
div = frame2.div(frame1)
print(div) # inf : 부모가 0인 경우 

# frame 곱셈 
mul = frame1.mul(frame2)
print(mul)

# 행/열 단위 합계/평균/최댓값/최솟값

sum1 = mul.sum(axis = 1) # 행 단위
sum2 = mul.sum(axis = 0) # 열 단위
print('행 단위 합계:\n',sum1)
print('열 단위 합계:\n',sum2)


avg1 = mul.mean(axis = 1) # 행 단위 평균
avg2 = mul.mean(axis = 0) # 열 단위 평균
print('행 단위 평균:\n',avg1)
print('열 단위 평균:\n',avg2)


mx = mul.max(axis = 0) # 열 단위 최댓값
mn = mul.min(axis = 0) # 열 단위 최솟값
print(mx)
print(mn)

# apply()함수 이용 외부함수 적용 
asum = mul.apply(sum)
print(asum)

# 요약통계량
des = mul.describe()
print(des)














