'''
 matplotlib API 이용 차트 그리기 
'''

import matplotlib.pyplot as plt
import numpy as np

data = np.arange(10) # 0 ~ 9
#plt.plot(data) # 차트 작성
#plt.show() # 차트 보이기

data2 = np.random.randn(100) 
#plt.plot(data2)
#plt.show() 

# sub plot 만들기 - 다수의 차트 표현 
flg = plt.figure() # 객체 생성
x1 = flg.add_subplot(2,2,1)
x2 = flg.add_subplot(2,2,2)
x3 = flg.add_subplot(2,2,3)
x4 = flg.add_subplot(2,2,4)

# 첫번째 플롯영역에 히스그램 그리기
x1.hist(np.random.randn(100), bins=30, alpha = 0.5) # alpha = 투명도 
#plt.show()

# 두번째 플롯영역에 산점도(x,y) 그리기 
x = np.arange(20)
y = np.arange(20) + 3 * np.random.randn(20)
x2.scatter(x, y)
#plt.show()

# 세번째 직선 그래프 그리기
x3.plot(np.arange(10))
#plt.show()

# 네번째 선 그래프 그리기 
x4.plot(np.random.randn(100).cumsum(), 'k--') # k-- : 검정색 점선 
plt.show()


# sub plot 만들기2 - 다수의 차트 표현 
flg2 = plt.figure() # 객체 생성
x11 = flg2.add_subplot(2,2,1)
x22 = flg2.add_subplot(2,2,2)
x33 = flg2.add_subplot(2,2,3)
x44 = flg2.add_subplot(2,2,4)

# 선 스타일 적용 
x11.plot(np.arange(5), np.arange(5), 'g--') # 'g--' : 녹색 점선 

# 선 스타일, 선 색 : linestyle='-', color='r'
x22.plot(np.arange(5), np.arange(5), linestyle='-', color='r')

x33.plot(np.random.randn(50), 'ko--') # 검정색 점선의 마킹 

# 하나의 sub plot에 다수 차트 그리기
data = np.random.randn(50).cumsum()

# 1) 선 그래프
x44.plot(data, 'k--', label='default') # label : 범례  
# 2) 계단형 그래프 
x44.plot(data, 'k-', drawstyle='steps-post', label='step') # drawstyle : 유형 
plt.legend(loc='best') # 범례 위치 : 최적 
plt.show()

# 차트 제목, x,y 축이름 
flg3 = plt.figure() # 객체 생성
chart = flg3.add_subplot(1,1,1)

data = np.random.randn(1000).cumsum()
chart.plot(data, color='r')
chart.set_xticks([0,250,500,750,1000]) # x축 범위 지정 
chart.set_title('Mat plot chart') # 차트 제목 
chart.set_ylabel('Random Number') # y축 이름
chart.set_xlabel('Stages') # x축 이름 

# 차트 저장하기
plt.savefig('random_number.png', dpi=500) # 이미지 저장 
plt.show() 
