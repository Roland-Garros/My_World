# -*- coding: utf-8 -*-

import pandas as pd

#========================================
# 시리즈와 데이터프레임 직접 만들기
#========================================
# 시리즈 직접 만들기
s = pd.Series(['banana', 42])
print(s)
print('-'*30)

s = pd.Series(['Wes Mckinney', 'Creator of Pandas'])
print(s)
print('-'*30)

s = pd.Series(['Wes Mckinney', 'Creator of Pandas'], index=['Person', 'Who'])
print(s)
print('-'*30)

# 데이터프레임 직접 만들기
scientists = pd.DataFrame({
    'Name' : ['Rosaline Franklin', 'William Gosset'],
    'Occupation' : ['Chemist', 'Statistician'],
    'Born' : ['1920-07-25', '1876-06-13'],
    'Died' : ['1958-04-16', '1937-10-16'],
    'Age' : [37, 61]
})
print( scientists )
print('-'*30)

scientists = pd.DataFrame(
    data = {
    'Name' : ['Rosaline Franklin', 'William Gosset'],
    'Occupation' : ['Chemist', 'Statistician'],
    'Born' : ['1920-07-25', '1876-06-13'],
    'Died' : ['1958-04-16', '1937-10-16'],
    'Age' : [37, 61]
    },
    index = ['Rosaline Franklin', 'William Gosset'],
    columns = ['Occupation', 'Born', 'Age', 'Died']
)
print( scientists )
print('-'*30)

# 순서가 보장된 딕셔너리 OrderedDict 사용
from collections import OrderedDict

scientists = pd.DataFrame(
    OrderedDict([
        ('Name', ['Rosaline Franklin', 'William Gosset']),
        ('Occupation', ['Chemist', 'Statistician']),
        ('Born', ['1920-07-25', '1876-06-13']),
        ('Died', ['1958-04-16', '1937-10-16']),
        ('Age', [37, 61])
    ])
)
print( scientists )
print('-'*30)


#========================================
# 시리즈 다루기 - 기초
#========================================
# 데이터프레임에서 시리즈 선택하기
scientists = pd.DataFrame(
    data = {
        'Occupation' : ['Chemist', 'Statistician'],
        'Born' : ['1920-07-25', '1876-06-13'],
        'Died' : ['1958-04-16', '1937-10-16'],
        'Age' : [37, 61]
    },
    index = ['Rosaline Franklin', 'William Gosset'],
    columns = ['Occupation', 'Born', 'Died', 'Age']
)
first_row = scientists.loc['William Gosset']
print( type(first_row) )
print( first_row )
print('-'*30)


# index, values 속성과 keys() 메서드 사용하기
print( first_row.index )
print('-'*30)

print( first_row.values )
print('-'*30)

print( first_row.keys() )
print('-'*30)

print( first_row.index[0] )
print('-'*30)

print( first_row.keys()[0] )
print('-'*30)


# 시리즈의 mean, min, max, std 메서드 사용하기
ages = scientists['Age']
print( ages )
print('-'*30)
# 평균
print( ages.mean() )
print('-'*30)
# 최소값
print( ages.min() )
print('-'*30)
# 최대값
print( ages.max() )
print('-'*30)
# 표준편차
print( ages.std() )
print('-'*30)


#========================================
# 시리즈 다루기 - 응용
#========================================
# 시리즈와 불린 추출 사용하기
scientists = pd.read_csv('../data/scientists.csv')

ages = scientists['Age']
print( ages.max() )
print('-'*30)

print( ages.mean() )
print('-'*30)

# 평균 보다 큰 값을 가지는 데이터만 출력
print( ages[ages > ages.mean()] )
print('-'*30)
# 원리 파악
print( ages > ages.mean() )
print('-'*30)

print( type(ages > ages.mean()) )
print('-'*30)

# Boolean 추출
manual_bool_values = [True, True, False, False, True, True, False, True]
print( ages[manual_bool_values] )
print('-'*30)


# 시리즈와 브로드캐스팅
# -> 시리즈나 데이터프레임에 있는 모든 데이터에 대해 한 번에 연산하는 것을 브로드캐스팅(Broadcasting)이라고 함.
# -> 시리즈처럼 여러 개의 값을 가진 데이터를 벡터라하고, 
# -> 단순 크기를 나타내는 데이터를 스칼라라고 함.
# 벡터 + 벡터 연산
print( ages + ages )
print('-'*30)
# 벡터 * 벡터 연산
print( ages * ages )
print('-'*30)
# 벡터 + 스칼라 연산
print( ages + 100 )
print('-'*30)
# 벡터 * 스칼라 연산
print( ages * 2 )
print('-'*30)

# 길이가 서로 다른 벡터 연산
print( pd.Series([1, 100]) )
print('-'*30)
print( ages + pd.Series([1, 100]) )
print('-'*30)

# 인덱스 역순으로 데이터 정렬
rev_ages = ages.sort_index( ascending=False )
print( rev_ages )
print('-'*30)
# 일치하는 인덱스 연산 수행
print( ages * 2 )
print('-'*30)
print( ages + rev_ages )
print('-'*30)


#========================================
# 데이터프레임 다루기
#========================================
# 불린 추출하기
print( scientists[scientists['Age'] > scientists['Age'].mean()] )
print('-'*30)
# 불린 데이터 출력하기
# print( scientists.loc[[True, True, False, True]] )
print('-'*30)
# 브로드캐스팅하기
print( scientists * 2 )
print('-'*30)


#========================================
# 시리즈와 데이터프레임의 데이터 처리하기
#========================================
print( scientists['Born'].dtype )
print('-'*30)
print( scientists['Died'].dtype )
print('-'*30)
# datetime 자료형 변환
born_datatime = pd.to_datetime( scientists['Born'], format='%Y-%m-%d' )
print( born_datatime )
print('-'*30)
# datetime 자료형 변환
died_datetime = pd.to_datetime( scientists['Died'], format='%Y-%m-%d' )
print( died_datetime )
print('-'*30)
# 2개 열 추가
scientists['born_dt'], scientists['died_dt'] = (born_datatime, died_datetime)
print( scientists.head() )
print('-'*30)
# 행,열 개수 파악
print( scientists.shape )
print('-'*30)
# datetime 객체 연산
scientists['age_days_dt'] = (scientists['died_dt'] - scientists['born_dt'])
print( scientists )
print('-'*30)

# 시리즈, 데이터프레임 데이터 섞기
print( scientists['Age'] )
print('-'*30)
import random
random.seed(42)
random.shuffle(scientists['Age'])
print( scientists['Age'] )
print('-'*30)

# 데이터프레임 열 삭제하기
print( scientists.columns )
print('-'*30)
scientists_dropped = scientists.drop(['Age'], axis=1)
print( scientists_dropped.columns )
print('-'*30)
print( scientists_dropped )
print('-'*30)


#========================================
# 데이터 저장하고 불러오기
#========================================
# 데이터를 피클, CSV, TSV 파일로 저장하고 불러오기
names = scientists['Name']
names.to_pickle('../output/scientists_names_series.pickle')
print('-'*30)
scientists.to_pickle('../output/scientists_df.pickle')