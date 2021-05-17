import pandas as pd
import numpy as np

# index와 value를 동시에 확인
obj = pd.Series([1, 2, 3, 4])
# print(obj)

# values
# print(obj.values)

# index
# print(obj.index)

# data type
# print(obj.dtype)

obj2 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
# print(obj2)

data = { "남근형": 29, "설재홍": 28, "김동윤": 28, "단석환": 27 }
obj3 = pd.Series(data)
# print(obj3)

# Series 이름 지정
obj3.name = "스터디"
# index에 이름 지정
obj3.index.name = "이름"
# print(obj3)

# 인덱스 이름 변겅(크기가 같아야 함)
obj3.index = ['스', '터', '디', '원']
# print(obj3)

data1 = {
    "name": ["Kilho", "Kilho", "Kilho", "Charles", "Charles"],
    "year": [2014, 2015, 2016, 2015, 2016],
    "points": [1.5, 1.7, 3.6, 2.4, 2.9],
}
# 표처럼 만들기(키값 : Columns의 이름, 키값의 갯수 : 열의 갯수, 리스트의 성분 갯수 : 행의 index)
df = pd.DataFrame(data1)
# print(df)

# print(df.index)
# print(df.columns)
# print(df.values)
df.index.name = "Num"
df.columns.name = "Info"
# print(df)

df2 = pd.DataFrame(
    data1, 
    columns=["year", "points", "name", "Penalty_new"],
    index=["one", "two", "three", "four", "five"]    
)
# print(df2)

# 기본통계량 제공(총 갯수, 평균, 표준편차, 최소값, 퍼센트, 최대값)
# print(df2.describe())

df3 = pd.DataFrame(
    data1, 
    columns=["year", "names", "points", "penalty"],
    index=["one", "two", "three", "four", "five"]    
)
# index와 원하는 값 가져오기
# print(df3["year"])
# print(df3[["year", "points"]])

# 원하는 columns에 값 지정
df3["penalty"] = 0.5
df3["penalty"] = [0.1, 0.2, 0.3, 0.4, 0.5]
# print(df3)

# zeros 라는 열을 생성하고, 값 넣기
df3["zeros"] = np.arange(5)
# print(df3)

# 원하는 행에 원하는 값 넣기
val = pd.Series([-1.2, -1.5, -1.7], index=["one", "three", "five"])
df3["debt"] = val
# print(df3)

# 새로운 열에 기존 열의 값을 연산한 값 대입
df3["net_points"] = df3["points"] - df3["penalty"]
# print(df3)

# 조건문을 통해 boolean형 대입 가능
df3["high_points"] = df3["net_points"] > 2.0
# print(df3)

# 원하는 열 삭제
del df3["high_points"]
del df3["net_points"]
del df3["zeros"]
del df3["debt"]
# print(df3)
# print(df3.columns)
df3.index.name = "Order"
df3.columns.name = "Info"
# print(df3)

# 인덱싱
# print(df3[0:3])
# print(df3["two":"four"])

# loc와 iloc를 사용한 인덱싱
# print(df3.loc["two"])
# print(df3.loc["two":"four"])
# print(df3.loc["two":"four", "points"])

# 두개가 같다
# print(df3.loc[:, "points"])
# print(df3["points"])

# 열 값 변경
df3["names"] = ["Kilho", "Kilho", "Kilho", "Charles", "Charles"]
# 새로운 행 추가
df3.loc["six"] = [2013, "Hayoung", 4, 0.1]
df3.loc["seven"] = [2017, "Cho", 4, 1]
# print(df3)

# index=3, 즉 4행의 값 가져오기
# print(df3.iloc[3])

# print(df3.iloc[3:5, 0:2])
# print(df3.iloc[[0, 1, 3], [1, 2]])

# Boolean 인덱싱
# print(df3["year"] > 2014)

# print(df3.loc[df3["year"] > 2014, :])
# print(df3.loc[df3["names"] == "Kilho", ["names", "points"]])

# print(df3.loc[(df3["points"] > 2) & (df3["points"] < 3), :])
df3["penalty"] = [-1, -2, 5, -4, -5, 6, 7]
# print(df3)
df3.loc[df3["points"] > 3, "penalty"] = 0
# print(df3)

df4 = pd.DataFrame(np.random.rand(6, 4))
# print(df4)
df4.columns = ["A", "B", "C", "D"]
# periods=6 은 입력날 날자로부터 6일에 대한 index 생성 즉, 6개의 행 생성
df4.index = pd.date_range("20160701", periods=6)
# print(df4)

# 성분에 NaN 을 대입하는 함수 np.nan
df4["F"] = [1.0, np.nan, 3.5, 6.1 , np.nan, 7.0]
# print(df4)
# any : 행의 성분에 NaN이 하나라도 있으면 그 행을 제거
# all : 행의 성분이 모두 NaN일 때 제거
# print(df4.dropna(how="any"))

# NaN의 value를 5.0으로
# print(df4.fillna(value=5.0))

# NaN인 성분만 True 나머지 False
# print(df4.isnull())
# print(df4.loc[df4.isnull()["F"], :])

# 날자명을 datetime데이터형으로 변환
# print(pd.to_datetime("20160701"))

# drop : 행 제거
# print(df4.drop(pd.to_datetime("20160701")))

# 열 제거 axis = 1
# print(df4.drop("F", axis=1))
# print(df4.drop(["B", "F"], axis=1))

data2 = [[1.4, np.nan], [7.1, -4.5], [np.nan, np.nan], [0.75, -1.3]]
df5 = pd.DataFrame(data2, columns=["one", "two"], index=["a", "b", "c", "d"])
# print(df5)

# axis=0 : 각 열 성분의 합, axis=1 : 각 행 성분의 합
# print(df5.sum(axis=0))
# print(df5.sum(axis=1))
# print(df5["one"].sum())

# 특정 행을 선택할 때는 loc
# print(df5.loc["b"].sum())

# mean() : 평균, var() : 분산 

# NaN이 있으면 값도 NaN -> skipna=False
# print(df5.sum(axis=1, skipna=False))

# fillna를 통해 NaN의 위치에 원하는 값을 넣을 수 있다.
one_mean = df5["one"].mean()
two_mean = df5["two"].min()
df5["one"] = df5["one"].fillna(value=one_mean)
df5["two"] = df5["two"].fillna(value=two_mean)
# print(df5)

df6 = pd.DataFrame(np.random.randn(6, 4), columns=["A", "B", "C", "D"], index=pd.date_range("20160701", periods=6))
# print(df6)

# corr : 상관계수 구하기 (피어슨 상관계수 공식)
# print(df6["A"].corr(df6["B"]))
# print(df6.corr()) 

# cov : 공분산 구하기
# print(df6["B"].cov(df6["C"]))
# print(df6.cov())

# permutation 함수를 통해 값을 섞고, reindex를 통해 index에 넣기
dates = df6.index
random_dates = np.random.permutation(dates)
df6 = df6.reindex(index=random_dates, columns=["D", "B", "C", "A"])
# print(df6)

# 행(index) 오름차순
# print(df6.sort_index(axis=0))

# 열(columns) 오름차순
# print(df6.sort_index(axis=1))

# 내림차순은 axis 뒤에 ,ascending = False 추가

# 특정 열의 값에 따라 오름차순
# print(df6.sort_values(by="D"))

# size는 리스트의 성분 갯수
df6["E"] = np.random.randint(0, 6, size= 6)
df6["F"] = ["alpha", "beta", "gamma", "gamma", "alpha", "gamma"]
# print(df6)

# 앞에서부터 순차적으로 오름차순
# print(df6.sort_values(by=["E", "F"]))

# 중복값 제거후 반환
# print(df6["F"].unique())

# 중복값 제거 및 갯수 반환
# print(df6["F"].value_counts())

# 포함여부 확인 ([값1, 값2]인 경우 or연산)
# print(df6["F"].isin(["alpha", "beta"]))
# print(df6.loc[df6["F"].isin(["alpha", "beta"]), :])

df7 = pd.DataFrame(np.random.randn(4, 3), columns=["b", "d", "e"], index=["Seoul", "Incheon", "Busan", "Daegu"])
# print(df7)

# func : 최대값 - 최소값 반환, apply() 함수를 통해 각 열(axis=0), 행(axis=1)에 대해 최대값 - 최소값 반환
func = lambda x: x.max() - x.min()
# print(df7.apply(func, axis=0))
# print(df7.apply(func, axis=1))