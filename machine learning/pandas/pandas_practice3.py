import pandas as pd
import numpy as np

df1 = pd.DataFrame({"key": list("bbacaab"), "data1": range(7)})
df2 = pd.DataFrame({"key": list("abd"), "data2": range(3)})
# print(df1, df2)

# 병합 / 두 data에 key가 모두 존재할 경우
# print(pd.merge(df1, df2, on="key"))

# 병합 / 한쪽에만 key가 존재하는 경우 포함
# print(pd.merge(df1, df2, on="key", how="outer"))

# 앞의 인자 기준
# print(pd.merge(df1, df2, on="key", how="left"))

# 뒤의 인자 기준
# print(pd.merge(df1, df2, on="key", how="right")) 

df3 = pd.DataFrame({"lkey": list("bbacaab"), "data1": range(7)})
df4 = pd.DataFrame({"rkey": list("abd"), "data2": range(3)})

# 왼쪽 lkey 기준 정렬, 오른쪽 rkey 기준 정렬
# print(pd.merge(df3, df4, left_on="lkey", right_on="rkey"))

left1 = pd.DataFrame({'key': ['a', 'b', 'a', 'a', 'b', 'c'], 'value': range(6)})
right1 = pd.DataFrame({'group_val': [3.5, 7]}, index = ['a', 'b'])

# print(left1)
# print(right1)

# 오른쪽 인자를 _index=True를 통해 index명을 기준으로 놓기
# print(pd.merge(left1, right1, left_on="key", right_index=True))

left2 = pd.DataFrame([[1., 2.], [3., 4.], [5., 6.]], index=["a", "c", "e"], columns=["Seoul", "Incheon"])
right2 = pd.DataFrame([[7., 8.], [9., 10.], [11., 12.], [13, 14]], index=['b', 'c', 'd', 'e'], columns=['Daegu', 'Ulsan'])
# print(left2)
# print(right2)
# print(pd.merge(left2, right2, how="outer", left_index=True, right_index=True))

s1 = pd.Series([0, 1], index=['a', 'b'])
s2 = pd.Series([2, 3, 4], index=['c', 'd', 'e'])
s3 = pd.Series([5, 6], index=['f', 'g'])

# index가 증가하는 형태로 연결되어 새로운 Series 생성
# print(pd.concat([s1, s2, s3]))

# 열 방향으로 연걸
# print(pd.concat([s1, s2, s3], axis= 1))

s4 = pd.concat([s1 * 5, s3])
# print(s4)

# print(pd.concat([s1, s4], axis= 1))
# print(pd.concat([s1, s2, s3], axis=1, keys=['one', 'two', 'three']))

df5 = pd.DataFrame(np.arange(6).reshape(3, 2), index=['a', 'b', 'c'], columns=['one', 'two'])
df6 = pd.DataFrame(np.arange(4).reshape(2, 2), index=['a', 'c'], columns=['three', 'four'])
# print(pd.concat([df5, df6], axis=1))

df7 = pd.DataFrame(np.random.randn(3, 4), columns=['a', 'b', 'c', 'd'])
df8 = pd.DataFrame(np.random.randn(2, 3), columns=['b', 'd', 'a'])
# print(df7)
# print(df8)

# index를 처음부터 새로 붙여서 자연스럽게 붙이기
# ignore_index 가 없을 경우 index는 0 1 2 0 1 이 된다.
# print(pd.concat([df7, df8], ignore_index=True))

# 계층적 인덱스
s = pd.Series(np.random.randn(10), index=[['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'], [1, 2, 3, 1, 2, 3, 1, 2, 2, 3]])
# print(s)
# print(s.index)
# print(s['b'])
# print(s['b', 2])
# print(s[:, 2])

# 계층적 인덱싱
df = pd.DataFrame(np.arange(12).reshape((4, 3)), index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]], columns=[['Seoul', 'Seoul', 'Busan'], ['Green', 'Red', 'Green']] )
# print(df)
df.index.names = ['key1', 'key2']
df.columns.names = ['city', 'color']
# print(df)
# print(df['Seoul'])
# print(df['Seoul', 'Green'])
# print(df.loc['a'])
# print(df.loc['a', 1])
# print(df.loc['b', ('Seoul', 'Red')])
# print(df.loc[('b', 2), 'Busan'])
# print(df.loc[('b', 1), ('Seoul', 'Green')])

# 정렬 (axis=0 행방향, axis=1 열방향)
# print(df.sort_index(axis=0, level=1))
# print(df.sort_index(axis=0, level='key2'))

# 1번째 계층인 city를 알파벳 순서로 오름차순 / axis=1이므로 열방향 계층
# print(df.sort_index(axis=1, level=0))

# 2번째 계층인 color를 알파벳 순서로 오름차순
# print(df.sort_index(axis=1, level=1))

# Busan 계층의 Green열의 성분 오름차순
# print(df.sort_values(by=("Busan", "Green")))

# 통계함수

# 행방향 level=0인 1번째 index층을 기준(a, b)으로 열의 성분들의 합 구하기
# print(df.sum(axis=0, level=0))

# 행방향 level=1인 2번째 index층을 기준으로 합 구하기(첫번째 계층 무시)
# print(df.sum(axis=0, level=1))

# 열방향 'color' 계층의 평균 (다른 계층 무시)
# print(df.mean(axis=1, level="color"))

df2 = pd.DataFrame({
    'a': range(7), 
    'b': range(7, 0, -1), 
    'c': ['one', 'one', 'one', 'two', 'two', 'two', 'two'], 
    'd': [0, 1, 2, 0, 1, 2, 3]
})
# print(df2)

# 특정열에 포함된 열을 계층적 인덱스로 바꾸기(c, d 열 사라짐)
df3 = df2.set_index(['c', 'd'])
# print(df3)

# c, d 열을 유지하면서 index로 내려주기
# print(df2.set_index(['c', 'd'], drop=False))

# 계층적 인덱스를 열로 올리면서 기본 정수를 index로 주기
# print(df3.reset_index())

df4 = pd.DataFrame(np.arange(6).reshape((2, 3)), index=['Seoul', 'Busan'], columns=['one', 'two', 'three'])
df4.index.name = 'city'
df4.columns.name = 'number'
# print(df4)

# 단일컬럼을 단일 인덱스의 하위계층으로 붙게하기 (stack은 항상 최하위 계층으로)
# print(df4.stack())

df5 = df4.stack()

# 인덱스의 최하위 계층을 칼럼의 최하위 계층으로 올리기
# print(df5.unstack())

# 첫번째 계층의 index 올리기
# print(df5.unstack(level=0))
# print(df5.unstack(level='city'))




