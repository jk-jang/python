'''
Created on 2016. 5. 26.

list 내포
    - list + for
set/dict 자료구조
    - set: {} -> 중복 data 불가능
    - dict: {'key':'value'}
'''
#1. list 내포
#형식 [결과값 for 변수 in 자료구조(list,tuple,set,dict)]

#for문 예
values = [2,1,2,3,4,2]
float_val=[]
for v in values:
    float_val.append(float(v))

print(float_val)

#list 내포
fvalues = [float(v) for v in values]
print(fvalues)

#문 list에 각각 2를 곱해
data = [1,5,3]
result = [(i*2) for i in data]
print(result)

#set/dict 자료구조
d = {'a':1,'b':2,'c':3}
for i in d.keys():
    print(d[i]) #index = key(값, 첨자불가능)
    
test_set={} #빈 set
str_key = ['a','b','a','d'] #4개 원소 - a:2개
for k in str_key:     
    #key: value -> dict로 출력
    test_set[k] = test_set.get(k,0)+1 #0은 초기값임, 앞에 빈 set을 만들었으니깐
print(test_set)







































