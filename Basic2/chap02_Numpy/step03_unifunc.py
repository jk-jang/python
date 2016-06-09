'''
Created on 2016. 5. 27.

유니버셜 함수
    - np 객체를 대상으로 수학/통계량을 구하는 함수
'''
import numpy as np
from numpy import intersect1d
from docutils.utils.punctuation_chars import delimiters

arr = np.arange(10)
print(arr)

print(np.sqrt(arr))#원소별 sqrt
print(arr ** 0.5)

print(np.exp(arr)) #log2 ** n
print(np.max(arr))

'''
list VS np 차이점
    - np객체에 수학/통계량 관련 함수 적용 가능
'''

#1. 차트 그리기
import matplotlib.pyplot as plt
#차트를 위한 data 생성
dataset = np.arange(1,5)
print('dataset',dataset)
x,y = np.meshgrid(dataset, dataset) #격자행렬 생성
print('x',x)
print(y)

z = np.sqrt(x**2 + y**2)
print(z)
plt.plot(z) #차트 생성
#plt.show() #차트 보이기

#z 값으로 타원형 차트
plt.imshow(z) #차트 생성
#plt.show()

####기술통계량 구하기
arr = np.arange(20).reshape(5,4)
print('유니버설 함수를 이용한 기술통계량')
print('평균=',arr.mean())
print('표준편차=',arr.std())
print('누적합=',arr.cumsum())

#집합 함수
x = np.array([1,2,3,4,5])
y = np.array([4,9,7])
print('교집합=',intersect1d(x,y))
#합집합 uni     , 차집합

#변수 -> 파일 저장
data = np.random.randn(5,4)
print(data)

#data - > data.txt파일 저장
np.savetxt('data.txt',data,delimiter=',')

#data.txt 가져오기
data_txt=np.loadtxt('data.txt',delimiter=',')
print(data_txt)









































