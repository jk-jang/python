'''
Created on 2016. 5. 26.

Numpy 패키지
    - Numerical Python
    - 선형대수(vector, matrix 연산) 연산에 효과적인 패키지
        -> 효율적인 메모리 관리, 접근 속도 빠름
    - list 구조와 유사함
    - 다차원 배열 구조 생성(다중 행렬 구조)
    - 주요 패키지 제공 함수
        ->randn(): 표준정규분포를 따르는 난수 생성
        ->array(): 다차원 배열 생성(python 자료구조 이용)
        ->arange(n): n 크기의 정수 생성 함수
'''
#1. 표준정규분포를 따르는 난수 생성
import numpy as np #별칭 as + 별칭, numpy넘 기니깐 별칭np로 써도됨 ㅋ

data = np.random.randn(3,4) #다차원 배열
print(data)

#data 블럭 단위 연산
print(data * 5)
print('\n',data + data)

#2. python 자료구조 이용 다차원 배열 객체 생성
data1 = [3, 5.6, 5,8, 9.5] #list
#np.array(data) ->여기서 쓸 수 있는 데이터 종류: list,set,...
arr1 = np.array(data1)
print(arr1)
#print(data1.max()) <-list는 계산이 안됨
print(arr1.max()) #<-list랑 달리 많은 계산이 됨

#정렬 기능
data1.sort()
print(data1) #[3, 5, 5.6, 8, 9.5]
arr1.sort()
print(arr1) #[ 3.   5.   5.6  8.   9.5]

#자료구조 타입
print(type(data1),type(arr1))#<class 'list'> <class 'numpy.ndarray'>

#다차원 배열 객체 생성
data2 = [[1,2,3,4,5],[6,7,8,9,10]] #이중리스트
print(data2)

arr2 = np.array(data2)
print(arr2)

#블럭 연산
print(arr2 * 0.5) #곱셈
#[[ 0.5  1.   1.5  2.   2.5]
#[ 3.   3.5  4.   4.5  5. ]]
print(arr2** 0.5) #제곱 = sqrt
#[[ 1.          1.41421356  1.73205081  2.          2.23606798]
# [ 2.44948974  2.64575131  2.82842712  3.          3.16227766]]

print(data1)
#print(data1 + 5) 블록 연산불가능

'''
*정리*
    list vs np 차이점
        - np 객체는 수학함수 적용가능
        - np 객체는 산술연순(블럭연산) 적용 가능
'''
# 0으로 채워진 다차원 객체 생성 
zarr = np.zeros((3,6)) # tuple 타입으로 지정 
print(zarr)

''' 문)for문 이용 index 
1 1 1 1 1 1 - 0
2 2 2 2 2 2 - 1
3 3 3 3 3 3 - 2
'''
i = [0,1,2]
print(i)
for n in i :
    zarr[n] = n + 1
    
print(zarr)  

'''문제)
1  2  3  4  5  6
7  8  9  10 11 12
13 14 15 16 17 18
'''  

cnt = 1
for n in range(3) : # 0 ~ 2
    for i in range(6) : # 0 ~ 5
        zarr[n][i] = cnt 
        cnt += 1 # 카운터 변수 
print(zarr)
        
#난수값으로 초기화된 다차원 배열 객체
arr = np.empty((2,4))
print('***arr***')
print(arr)

#1로 채워진 다차원 배열 객체
np_one = np.ones((3,2))
print(np_one)
#[[ 1.  1.]
# [ 1.  1.]
# [ 1.  1.]]

#3. np.arange(n): range() 기능 동일함
ar1 = np.arange(10) #0~9
print(ar1)

ar2 = np.arange(1,11) #1~10
print(ar2)

arr = np.array([ar1,ar2])
print(arr)

#type보기 / type 변환
print(arr.dtype) #int32

arr2 = np.array(['10','20','30'])
print(arr2, arr2.dtype)#['10' '20' '30'] <U2
#print(arr2 * 5) error발생, arr2는 문자니껜 

#문자열 -> int 형변환
print(arr2.astype(np.int32)*5) #정수형
print(arr2.astype(np.float64)*5) #실수형