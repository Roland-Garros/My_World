# -*- coding: utf-8 -*-

import pandas

#========================================
# 실습용 csv 데이터 DataFrame 추출
#========================================
df = pandas.read_csv('../data/gapminder.tsv', sep='\t')

# df 상위 5개 데이터 출력
print( df.head() )
print('-'*30)
# df 데이터 포맷 출력
print( type(df) )
print('-'*30)
# df 행/열 구조 파악
print( df.shape )
print('-'*30)
# df 컬럼명 획득
print( df.columns )
print('-'*30)
# df 컬럼별 데이터 포맷 출력
print( df.dtypes )
print('-'*30)
# df 컬럼별 상세 정보 출력
print( df.info() )
print('-'*30)

#========================================
# 열 단위 데이터 추출하기
#========================================
# 데이터 포맷 출력
country_df = df['country']
print( type(country_df) )
print('-'*30)
# 상위 5개 데이터 출력
print( country_df.head() )
print('-'*30)
# 하위 5개 데이터 출력
print( country_df.tail() )
print('-'*30)

#========================================
# 여러개 열 데이터 추출하기
#========================================
# 데이터 포맷 출력
subset = df[['country', 'continent', 'year']]
print( type(subset) )
print('-'*30)
# 상위 5개 데이터 출력
print( subset.head() )
print('-'*30)
# 하위 5개 데이터 출력
print( subset.tail() )
print('-'*30)

#========================================
# loc 속성으로 행 단위 데이터 추출하기
#========================================
# 0번 인덱스 행 데이터 출력
print( df.loc[0] )
print('-'*30)
# 99번 인덱스 행 데이터 출력
print( df.loc[99] )
print('-'*30)
# 존재하지 않는 인덱스 행 데이터 출력
# -> 오류 발생
# print( df.loc[-1] )
# 마지막 행 데이터 출력
number_of_rows = df.shape[0]
last_row_index = number_of_rows - 1
print( df.loc[last_row_index] )
print('-'*30)
# 마지막 행 데이터 출력 2
print( df.tail(n=1) )
print('-'*30)
# 여러개 인덱스 데이터 출력
print( df.loc[[0, 99, 999]] )
print('-'*30)

#========================================
# iloc 속성으로 행 단위 데이터 추출하기
#========================================
print( df.iloc[1] )
print('-'*30)
print( df.iloc[99] )
print('-'*30)
print( df.iloc[-1] )
print('-'*30)
print( df.iloc[[0, 99, 999]] )
print('-'*30)

#========================================
# 슬라이싱 구문으로 데이터 추출하기
#========================================
subset = df.loc[:, ['year', 'pop']]
print( subset.head() )
print('-'*30)

subset = df.iloc[:, [2, 4, -1]]
print( subset.head() )
print('-'*30)

#========================================
# range 메서드로 데이터 추출하기
#========================================
small_range = list( range(5) )
print( small_range )
print('-'*30)

print( type(small_range) )
print('-'*30)

subset = df.iloc[:, small_range]
print( subset.head() )
print('-'*30)

small_range = list( range(3, 6) )
print( small_range )
print('-'*30)

subset = df.iloc[:, small_range]
print( subset.head() )
print('-'*30)

small_range = list( range(0, 6, 2) )
subset = df.iloc[:, small_range]
print( subset.head() )
print('-'*30)

subset = df.iloc[:, :3]
print( subset.head() )
print('-'*30)

subset = df.iloc[:, 0:6:2]
print( subset.head() )
print('-'*30)

print( df.iloc[[0, 99, 999], [0, 3, 5]] )
print('-'*30)

print( df.loc[[0, 99, 999], ['country', 'lifeExp', 'gdpPercap']] )
print('-'*30)

print( df.loc[10:13, ['country', 'lifeExp', 'gdpPercap']] )
print('-'*30)

#========================================
# 기초적인 통계 계산하기
#========================================
print( df.head(n=10) )
print('-'*30)
# `year` 열로 그룹화한 다음 `lifeExp` 열 평균 계산
print( df.groupby('year')['lifeExp'].mean() )
print('-'*30)

grouped_year_df = df.groupby('year')
print( type(grouped_year_df) )
print('-'*30)

print( grouped_year_df )
print('-'*30)

grouped_year_df_lifeExp = grouped_year_df['lifeExp']
print( type(grouped_year_df_lifeExp) )
print('-'*30)

mean_lifeExp_by_year = grouped_year_df_lifeExp.mean()
print( mean_lifeExp_by_year )
print('-'*30)

# `year`, `continent` 열로 그룹화한 그룹 데이터프레임에서 `lifeExp`, `gdpPercap` 열만 추출하여 평균값 계산
multi_group_year = df.groupby(['year', 'continent'])[['lifeExp', 'gdpPercap']].mean()
print( multi_group_year )
print('-'*30)

# `continent`를 기준으로 데이터프레임을 만들고 `country` 열만 추출하여 그룹화한 데이터 개수 세기
print( df.groupby('continent')['country'].nunique() )
print('-'*30)

#========================================
# 그래프 그리기
#========================================
import matplotlib.pyplot as plt

global_yearly_life_expectancy = df.groupby('year')['lifeExp'].mean()
print( global_yearly_life_expectancy )
global_yearly_life_expectancy.plot()