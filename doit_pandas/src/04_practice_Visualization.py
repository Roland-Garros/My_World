# -*- coding: utf-8 -*-

#========================================
# 04. 그래프 그리기
#========================================
# 데이터 시각화가 필요한 이유
import seaborn as sns

anscombe = sns.load_dataset("anscombe")
print( anscombe )
print( type(anscombe) )
print('-'*30)

import matplotlib.pyplot as plt

dataset_1 = anscombe[anscombe['dataset'] == 'I']

# plt.figure()
# plt.plot( dataset_1['x'], dataset_1['y'] )
# plt.plot( dataset_1['x'], dataset_1['y'], 'o' )
# plt.show()
# plt.close()


# 시각화 데이터 추출
dataset_2 = anscombe[anscombe['dataset'] == 'II']
dataset_3 = anscombe[anscombe['dataset'] == 'III']
dataset_4 = anscombe[anscombe['dataset'] == 'IV']
# 그래프 격자가 위치할 기본 틀 생성
fig = plt.figure()
# 기본 틀 열 크기 설정
axis1 = fig.add_subplot(2, 2, 1)
axis2 = fig.add_subplot(2, 2, 2)
axis3 = fig.add_subplot(2, 2, 3)
axis4 = fig.add_subplot(2, 2, 4)
# 점그래프 표현
axis1.plot( dataset_1['x'], dataset_1['y'], 'o' )
axis2.plot( dataset_2['x'], dataset_2['y'], 'o' )
axis3.plot( dataset_3['x'], dataset_3['y'], 'o' )
axis4.plot( dataset_4['x'], dataset_4['y'], 'o' )
# 격자에 제목 추가
axis1.set_title('dataset_1')
axis2.set_title('dataset_2')
axis3.set_title('dataset_3')
axis4.set_title('dataset_4')
# 기본 틀에 제목 추가
fig.suptitle('Anscombe Data')
# 그래프 레이아웃 조절
fig.tight_layout()

# plt.show()
plt.close()


# matplotlib 라이브러리 자유자재로 사용하기
tips = sns.load_dataset('tips')
print( tips.head() )
print( type(tips) )
print('-'*30)

# 히스토그램 그래프 출력
fig = plt.figure()
axis1 = fig.add_subplot(1, 1, 1)
axis1.hist( tips['total_bill'], bins=10 )
axis1.set_title('Histogram of total Bill')
axis1.set_xlabel('Frequency')
axis1.set_ylabel('Total Bill')
# plt.show()
plt.close()

# 산점도 그래프 출력
scatter_plot = plt.figure()
axis1 = scatter_plot.add_subplot(1, 1, 1)
axis1.scatter(tips['total_bill'], tips['tip'])
# plt.show()
plt.close()

# 박스 그래프 출력
boxplot = plt.figure()
axis1 = boxplot.add_subplot(1, 1, 1)
axis1.boxplot([tips[tips['sex'] == 'Female']['tip'], tips[tips['sex'] == 'Male']['tip']], labels=['Female', 'Male'])
axis1.set_xlabel('Sex')
axis1.set_ylabel('Tip')
axis1.set_title('Boxplot of Tips by Sex')
# plt.show()
plt.close()

# 다변량 그래프 출력 - 산점도 그래프
def recode_sex(sex):
    if sex == 'Female':
        return 0
    else:
        return 1
tips['sex_color'] = tips['sex'].apply(recode_sex)

scatter_plot = plt.figure()
axis1 = scatter_plot.add_subplot(1, 1, 1)
axis1.scatter(
    x = tips['total_bill'],
    y = tips['tip'],
    s = tips['size'] * 10,
    c = tips['sex_color'],
    alpha = 0.5
)
axis1.set_title('Total Bill vs Tip Colored by Sex and Sized by Size')
axis1.set_xlabel('Total Bill')
axis1.set_ylabel('Tip')

# plt.show()
plt.close()


# seaborn 라이브러리 자유자재로 사용하기
# 단변량 그래프 그리기 - 히스토그램
import seaborn as sns
tips = sns.load_dataset('tips')

# 히스토그램, 밀집도 그래프 출력
ax = plt.subplots()
ax = sns.distplot(tips['total_bill'])
ax.set_title('Total Bill Histogram with Density Plot')
# plt.show()
plt.close()

# 히스토그램 그래프만 표현
ax = plt.subplots()
ax = sns.distplot(tips['total_bill'], kde=False)
ax.set_title('Total Bill Histogram')
ax.set_xlabel('Total Bill')
ax.set_ylabel('Frequency')
# plt.show()
plt.close()

# 밀집도 그래프만 표현
ax = plt.subplots()
ax = sns.distplot(tips['total_bill'], hist=False)
ax.set_title('Total Bill Density')
ax.set_xlabel('Total Bill')
ax.set_ylabel('Unit Probability')
# plt.show()
plt.close()

# 양탄자 그래프 표현
ax = plt.subplots()
ax = sns.distplot(tips['total_bill'], rug=True)
ax.set_title('Total Bill Histogram with Density and Fug Plot')
ax.set_xlabel('Total Bill')
# plt.show()
plt.close()

# 이산 그래프 표현
ax = plt.subplots()
ax = sns.countplot('day', data=tips)
ax.set_title('Count of days')
ax.set_xlabel('Day of the week')
ax.set_ylabel('Frequency')

# plt.show()
plt.close()