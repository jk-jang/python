'''
문) iris.csv 파일을 이용하여 다음과 같이 차트를 그리시오.
  <조건1> iris.csv 파일을 iris 변수명으로 가져온 후 정보 보기  
  <조건2> 첫번째 칼럼과 세번째 칼럼을 대상으로 산점도 그래프 그리기(제목과 x,y축이름 표시) 
  <조건3> Species 칼럼을 제외한 나머지 4개 칼럼으로  분포곡선과 산점도 matrix 그리기 
  <조건4> Species 칼럼을 제외한 나머지 4개 칼럼의 평균을 계산하여 막대차트 그리기
'''
import pandas as pd
import matplotlib.pyplot as plt

# 각 칼럼 간 데이터 비교
iris = pd.read_csv('iris.csv')
print(iris.info()) 

plt.scatter(iris['Sepal.Length'], iris['Petal.Length'])
plt.title('Scatter of %s and %s column' %('Sepal.Length', 'Petal.Length'))
plt.xlabel('Sepal.Length'); plt.ylabel('Petal.Length')
plt.show()


# Species(꽃의 종류) 칼럼 제외한 나머지 4개 칼럼 가져오기
iris = iris[['Sepal.Length','Sepal.Width','Petal.Length','Petal.Width']]
print(iris)

print('\niris 칼럼  분포곡선과 산점도 matrix')
# diagonal='kde' : 밀도 그래프 제공
pd.scatter_matrix(iris, diagonal='kde', color='r') 
plt.show() 

# Species(꽃의 종류) 칼럼 제외한 나머지 4개 칼럼의 평균 계산하여 막대차트 그리기
col_sum = iris.mean(axis = 0)
print(col_sum)
col_sum.plot(alpha=0.8, kind='bar', use_index=True, rot=45, title='average of iris column' )
plt.show() 


