'''
Created on 2016. 5. 27.

다차원 객체(ndarray)인덱싱/슬라이싱/연산
'''

#python List
li = [0,1,2,3,4,5]
print(li[3]) #->3
print(li[:3]) # [0, 1, 2]
print(li[-3:-1])#[3, 4]

#numpy 장착
import numpy as np
#np list
arr = np.arange(10)
print(arr[:5])#[0 1 2 3 4]
print(arr[1:3])#[1 2]
'''
list vs np 공통점
    - index 범위로 원소를 참조
    - 결과는 list로 반환
    
            차이점
    - np 객체는 범위 수정이 가능
    - np 객체는 view 생성으로 원본을 수정할 수 있다. 
'''

####슬라이싱
#list 객체 슬라이싱
li_slice = li[1:4]
print(li_slice)
#li_slice[:3] = 100 error! 범위 수정 불가능
li_slice[0] = 100

print('복사본\n',li_slice) #복사본 수정
print(li) #원본
#so, 원본 수정 불가능!!

#np 객체 대상 슬라이싱
arr_slice = arr[5:8] #view 생성
print(arr_slice) #[5 6 7]
arr_slice[:3] = 100
print(arr_slice) #[100 100 100]

#view 수정 -> 원본 수정됨
print(arr)

#3차원(행,열,면) 배열 객체 생성
r1 = [1,2,3]; r2 = [4,5,6]; r3 = [7,8,9]
arr2d = np.array([r1,r2,r3])
print(arr2d)
'''
[[1 2 3]
 [4 5 6]
 [7 8 9]]
'''

r4 = [10,11,12]
arr3d=np.array([[r1,r2],[r3,r4]])#2행 3열 2면
print('3차원\n',arr3d)
''' 
[[[ 1  2  3]
 [ 4  5  6]]

 [[ 7  8  9]
 [10 11 12]]]
'''
#3차원 배열index,indexing의 default는 면
print(arr3d[1]) #2면 출력
#-> [[ 7  8  9]
#   [10 11 12]]
print(arr3d[1,1,1]) #2면 2행 2열 #->11

# 3차원 배열에서 copy VS view
#copy가 원본에는 영향을 안줌
#view는 원본에 영향을 줌

print('\n3차원 배열 copy')
arr_copy=arr3d[0].copy() #1번째 면
print(arr_copy)
arr_copy[:] =100
print(arr_copy)

print('\n3차원 배열 view')
arr_slice = arr3d[1,0] #2면 1행
print(arr_slice)
arr_slice[:3] = 1000
print(arr_slice) #view 결과
print(arr3d) #원본 결과

####boolean 색인(조건식으로 indexing)
data = np.random.randn(5,4)
print(data)

names = np.array(['성향적','행동적','상황적','인문학','통찰력'])
print('\n성향적 data 출력')
print(data[names =='성향적']) # = data[0]

#전체 원소 중에서 조건에 만족하는 data 추출 가능
mask = (names == '성향적') | (names == '행동적')
print(data[mask]) 
print('0이상만 가져와')
print(data[data>0])

####다차원 배열객체 구조변경
arr = np.arange(20).reshape(4,5)
print(arr)

#전치행렬
print(arr.T)

arr2 = np.arange(12).reshape(3,2,2) #3행 2열 2면
print(arr2)

#각 면에서 행 <-> 열
print(arr2.swapaxes(1,2))

#tile(), 구조 변경
r1 = [1.4, 2.4]; r2 = [3.2, 4.2]
arr3 = np.array([r1,r2])
print(arr3)
#[[ 1.4  2.4]
# [ 3.2  4.2]]
result = np.tile(arr3, 3) #3: 반복수
print(result)
#[[ 1.4  2.4  1.4  2.4  1.4  2.4]
# [ 3.2  4.2  3.2  4.2  3.2  4.2]]
result = np.tile(arr3, (2,4)) #(2,4) ->(전체반복횟수, 행단위반복횟수)
print(result)
'''
[[ 1.4  2.4  1.4  2.4  1.4  2.4  1.4  2.4]
 [ 3.2  4.2  3.2  4.2  3.2  4.2  3.2  4.2]
 [ 1.4  2.4  1.4  2.4  1.4  2.4  1.4  2.4]
 [ 3.2  4.2  3.2  4.2  3.2  4.2  3.2  4.2]]
'''
#칼럼: axis = 0, 행: axis = 1
result_sum = result.sum(axis=1) #행 단위
result_sum = result.sum(axis=0) #열 단위

print(result_sum)
for r in result_sum:
    print(r)
'''
15.2
29.6
15.2
29.6
'''