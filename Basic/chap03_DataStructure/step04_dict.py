'''
Created on 2016. 5. 17.

dict 자료구조
    - key: value 형식으로 객체 생성
    형식1) 변수 = dict(key=value, key=value,...)
    형식2) 변수 = {'key':value, 'key':value} #이걸 더 많이 씀
    - key 이용해서 값을 참조(값 또는 index 참조 불가)
    - 출력 순서는 랜덤
'''

#dict 객체 생성 방법1
dic = dict(key1 = 100, key2 = '홍길동' ,key3 = 123.42)
print(dic)
#dict 객체 생성 방법2
dic2 = {'name':'홍길동', 'age':30,'급여':100}
print(type(dic),type(dic2))
#<class 'dict'> <class 'dict'>
print('dic 길이:', len(dic),len(dic2))

#급여조회 -> key이용
print(dic2['급여'])

#추가 및 수정
dic2['부서']='기획부'
print(dic2) #{'급여': 100, 'name': '홍길동', '부서': '기획부', 'age': 30}

#수정
del dic2['부서']
print(dic2) #{'급여': 100, 'name': '홍길동', 'age': 30}

member = {'id':'hong','pass':'1234','gender':'male'}
print(member)
print(member['gender'])#male
print(member.keys())#dict_keys(['pass', 'gender', 'id'])
print(member.items())#dict_items([('pass', '1234'), ('gender', 'male'), ('id', 'hong')])
print(member.values())#dict_values(['1234', 'male', 'hong'])

#dict에서 자료 조회(검색)
print('id' in member)#True
print('pay' in member)#False

for key in member.keys():
    print(key, end=', ')

#문) key값을 기준으로 해당 value값을 출력
for k in member.keys():
    v = member[k]
    print(v)
