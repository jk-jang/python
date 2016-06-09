'''
list복습
'''
#단일 List
a = [1,2,3]
a.append(4)
a.append([5,'a'])
print(a) #[1, 2, 3, 4, [5, 'a']]
#문)'a'원소 출력
print(a[4][1])#5번째 list에 그 list에서 2번째 놈을 가져와
#index 출력
#2어디에 있노
print(a.index(2))
#'a'어디에 있노
print(a[4].index('a'))#->1: 2번째에 있다는 말



