'''
문2) 키보드로 최대 5개 정수를 입력하여 다음과 같이 처리하시오.
 조건1> 키보드로 입력한 데이터를 list 객체에 추가
 조건2> list 객체 원소를 대상으로 내림차순 정렬/출력
 조건3> list 객체 원소를 대상으로 최댓값과 최솟값 출력
 조건4> 100 이상의 값 입력 시 더 이상 키보드 입력 중단 후 <조건2, 3> 수행 
'''

# 문1) 키보드로 입력한 데이터를 list에 추가 
cnt = 1
data = []
while cnt <= 5:
    i = input('%d 번째 데이터 입력 :'%cnt)    
    print('input =', i) # 중복 출력
    data.append(int(i))
    cnt += 1 # 카운터 변수 
    if(int(i) >= 100): # exit 조건 
        break
        #sys.exit() # 프로그램 종료
print(data) # data에 저장된 원소 출력 

# 문2) list 원소를 내림차순 정렬 후  출력
data.sort(reverse=True)
print(data[:len(data)])


# 문3) 최댓값/최솟값 출력하기
max_num=-999; min_num=999
for d in data :
    if(max_num < d) :
        max_num = d
    elif(min_num > d) :
        min_num = d    
print('max =',max_num,', ','min =',min_num)        

