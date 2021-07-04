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


# seaborn 라이브러리로 산점도 그래프 그리기
# -> 회귀선 표시
ax = plt.subplots()
ax = sns.regplot(x='total_bill', y='tip', data=tips)
ax.set_title('Scatterplot of Total Bill and Tip')
ax.set_xlabel('Total Bill')
ax.set_ylabel('Tip')

# plt.show()
plt.close()

# seaborn 라이브러리로 산점도 그래프 그리기
# -> 회귀선 제거
ax = plt.subplots()
ax = sns.regplot(x='total_bill', y='tip', data=tips, fit_reg=False)
ax.set_title('Scatterplot of Total Bill and Tip')
ax.set_xlabel('Total Bill')
ax.set_ylabel('Tip')

# plt.show()
plt.close()

# 산점도 그래프와 히스토그램을 한 번에 그리기
joint = sns.jointplot(x='total_bill', y='tip', data=tips)
joint.set_axis_labels(xlabel='Total Bill', ylabel='Tip')
joint.fig.suptitle('Joint Plot of Total Bill and Tip', fontsize=10, y=1.03)

# plt.show()
plt.close()

# 육각 그래프 그리기
hexbin = sns.jointplot(x='total_bill', y='tip', data=tips, kind='hex')
hexbin.set_axis_labels(xlabel='Total Bill', ylabel='Tip')
hexbin.fig.suptitle('Hexbin Joint Plot of Total Bill and Tip', fontsize=10, y=1.03)

# plt.show()
plt.close()


# 이차원 밀집도 그리기
ax = plt.subplots()
ax = sns.kdeplot(data=tips['total_bill'], data2=tips['tip'], shade=True)
ax.set_title('Kernel Density Plot of Total Bill and Tip')
ax.set_xlabel('Total Bill')
ax.set_ylabel('Tip')

# plt.show()
plt.close()


# 바 그래프 그리기
ax = plt.subplots()
ax = sns.barplot(x='time', y='total_bill', data=tips)
ax.set_title('Bar Plot of Average Total Bill for Time of Day')
ax.set_xlabel('Time of day')
ax.set_ylabel('Average total bill')

# plt.show()
plt.close()


# 박스 그래프 그리기
ax = plt.subplots()
ax = sns.boxplot(x='time', y='total_bill', data=tips)
ax.set_title('Boxplot of Total Bill by Time of Day')
ax.set_xlabel('Time of day')
ax.set_ylabel('Total Bill')

# plt.show()
plt.close()


# 바이올린 그래프 그리기
ax = plt.subplots()
ax = sns.violinplot(x='time', y='total_bill', data=tips)
ax.set_title('Violin plot of total bill by time of day')
ax.set_xlabel('Time of day')
ax.set_ylabel('Total Bill')

# plt.show()
plt.close()


# 관계 그래프 그리기
fig = sns.pairplot(tips)

# plt.show()
plt.close()


# 관계 그래프 중복 없애기
pair_grid = sns.PairGrid(tips)
pair_grid = pair_grid.map_upper(sns.regplot)
pair_grid = pair_grid.map_lower(sns.kdeplot)
pair_grid = pair_grid.map_diag(sns.distplot, rug=True)

# plt.show()
plt.close()


# seaborn 라이브러리로 바이올린 그래프 그리기 - 색상추가
ax = plt.subplots()
ax = sns.violinplot(x='time', y='total_bill', hue='sex', data=tips, split=True)

plt.close()

# 산점도, 관계 그래프 그리기 - 색상 추가
scatter = sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', fit_reg=False)
fig = sns.pairplot(tips, hue='sex')

# plt.show()
plt.close()


# 산점도 그래프의 크기와 모양 조절하기
# scatter = sns.lmplot(x='total_bill', y='tip', data=tips, fit_reg=False, hue='sex', scatter_kws={'s': tips['size']*10})
# scatter = sns.lmplot(x='total_bill', y='tip', data=tips, fit_reg=False, hue='sex')
scatter = sns.lmplot(x='total_bill', y='tip', data=tips, fit_reg=False, hue='sex', markers=['o', 'x'])

# plt.show()
plt.close()


# lmplot 메서드로 4개의 데이터 그룹에 대한 그래프 한 번에 그리기
anscombe_plot = sns.lmplot(x='x', y='y', data=anscombe, fit_reg=False)

# plt.show()
plt.close()


# lmplot 메서드로 4개의 데이터 그룹 나누어 그리기
anscombe_plot = sns.lmplot(x='x', y='y', data=anscombe, fit_reg=False, col='dataset', col_wrap=2)

# plt.show()
plt.close()


# FaceGrid 클래스로 그룹별 그래프 그리기
facet = sns.FacetGrid(tips, col='time')
facet.map(sns.distplot, 'total_bill', rug=True)

# plt.show()
plt.close()

facet = sns.FacetGrid(tips, col='day', hue='sex')
facet = facet.map(plt.scatter, 'total_bill', 'tip')
facet = facet.add_legend()

# plt.show()
plt.close()


facet = sns.FacetGrid(tips, col='time', row='smoker', hue='sex')
facet.map(plt.scatter, 'total_bill', 'tip')

# plt.show()
plt.close()


# ========================================
# 데이터프레임과 시리즈로 그래프 그리기
# ========================================
# 데이터 프레임과 시리즈로 그래프 그리기
ax = plt.subplots()
ax = tips['total_bill'].plot.hist()

# plt.show()
plt.close()

# 투명도 조절
# -> alpha는 투명도, bins는 x축의 간격
fig, ax = plt.subplots()
ax = tips[['total_bill', 'tip']].plot.hist(alpha=0.5, bins=20, ax=ax)

# plt.show()
plt.close()

# 밀집도, 산점도, 육각 그래프 그리기
ax = plt.subplots()
ax = tips['tip'].plot.kde()

fig, ax = plt.subplots()
ax = tips.plot.scatter(x='total_bill', y='tip', ax=ax)

fig, ax = plt.subplots()
# ax = tips.plot.hexbin(x='total_bill', y='tip', ax=ax)
ax = tips.plot.hexbin(x='total_bill', y='tip', gridsize=10, ax=ax)

fig, ax = plt.subplots()
ax = tips.plot.box(ax=ax)

# plt.show()
plt.close()


# seaborn 라이브러리로 그래프 스타일 설정하기
sns.set_style('whitegrid')
fig, ax = plt.subplots()
ax = sns.violinplot(x='time', y='total_bill', hue='sex', data=tips, split=True)

# plt.show()
plt.close()


# for문을 이용하여 모든 스타일을 하나씩 적용한 그래프
fig = plt.figure()

seaborn_styles = ['darkgrid', 'whitegrid', 'dark', 'white', 'ticks']

for idx, style in enumerate(seaborn_styles):
    plot_position = idx + 1
    with sns.axes_style(style):
        ax = fig.add_subplot(2, 3, plot_position)
        violin = sns.violinplot(x='time', y='total_bill', data=tips, ax=ax)
        violin.set_title(style)

fig.tight_layout()

# plt.show()
plt.close()