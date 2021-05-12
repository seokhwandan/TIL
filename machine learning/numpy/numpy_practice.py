import numpy as np

data1 = [6, 7, 8, 9, 10]
arr1 = np.array(data1)
# print(arr1)
# print(arr1.shape)
data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)
# print(arr2)

# array의 행과 열
# print(arr2.shape)

# 요소가 모두 0인 array
# print(np.zeros((3, 6)))

# 요소가 모두 1인 array
# print(np.ones(10))

# 3 ~ 9까지의 array
# print(np.arange(3, 10))

arr = np.array([1, 2, 3, 4, 5], dtype=np.int64)
# print(arr.dtype)

# 데이터 타입 바꾸기
float_arr = arr.astype(np.float64)
# print(float_arr)
# print(float_arr.dtype)

# array 연산
arr1 = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.float64)
arr2 = np.array([[7, 8, 9], [10, 11, 12]], dtype=np.float64)

# print(arr1 + arr2)

# print(arr1 - arr2)

# print(arr1 * arr2)

# print(arr1 / arr2)

# print(arr1 * 2)

arr = np.arange(10)
# print(arr)

# print(arr[5])

# print(arr[5:8])

# print(arr[:])

arr2d = np.arange(1, 17).reshape((4, 4))
# print(arr2d)

# print(arr2d[2, :])

# print(arr2d[:, :2])

arr2d[:2, 1:3] = 0
# print(arr2d)

names = np.array(["Charles", "Kilho", "Hayoung", "Charles", "Hayoung", "Kilho", "Kilho"])

# array 성분을 랜덤으로 7x4 이차원 array 생성
# data = np.random.randn(7, 4)

data = np.arange(1, 29).reshape(7, 4)
# print(data)

# names array에서 True or False 출력
# print(names == "Charles")

# names == "Charles"의 True 가 0, 3 index 이므로, data[[0, 3], :]
# print(data[names == "Charles", :])

# or 연산도 가능
# print(data[(names == "Charles") | (names == "Kilho"), :])

# print(data[:, 3])

# 3열의 값이 12보다 작은 행만 True
# print(data[:, 3] < 12)

# 위의 값에서 True인 행만 출력
# print(data[data[:, 3] < 12, :])

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# 모든 값에 루트 씌우기
# print(np.sqrt(arr))

# 모든 값에 로그 씌우기
# log == 자연로그, log10
# print(np.log(arr))
# abs, square, exp, sign, ceil(소수점 첫자리 올림), floor(소수점 첫자리 내림), isnan, isinf, cos, cosh, sin, sinh, tan, tanh

x = np.arange(1, 10).reshape((3, 3))
y = np.arange(11, 20).reshape((3, 3))
# 같은 크기의 행렬의 값 비교 후 큰 값 출력
# print(np.maximum(x, y))

# 행렬의 모든 값 더하기
# axis=0: 각 열의 합, axis=1: 각 행의 합 (axis 생략 가능)
# print(x.sum(1))

# 행렬의 모든 값 평균 구하기
# print(x.mean())
#std(표준편차), var(분산), min, max, argmin, argmax(idx반환), cumsum(누적합), cumprod(누적곱)

# print(x > 5)
# 5보다 큰 값의 갯수(True = 1 이므로)
# print((x > 5).sum())

# 5보다 큰 값의 합
# print(x[x > 5].sum())

# 정렬 (2d인 경우, axis=0 각 열을 오름차순, axis=1 각 행을 오름차순)
# 오름차순
# print(np.sort(x))
# 내림차순 (1차원일때만)
a = np.arange(1, 100)
# print(np.sort(a)[::-1])

b = np.array([4, 4, 3, 3, 1, 1, 1, 2, 2, 4])
# 중복 제거 및 정렬
# print(np.unique(b))

# 데이터 불러오기
data = np.loadtxt("./movielens-1m/ratings.dat", delimiter="::", dtype=np.int64)
# print(data[:5, :])
# print(data.shape)

mean_rating_total = data[:, 2].mean()
# print(mean_rating_total)

user_ids = np.unique(data[:, 0])
# print(user_ids)
# print(user_ids[:5])
# print(user_ids.shape)

mean_rating_by_user_list = []
mrbul = []
for user_id in user_ids:
    data_for_user = data[data[:, 0] == user_id, :]
    mean_rating_for_user = data_for_user[:, 2].mean()
    mean_rating_by_user_list.append([user_id, mean_rating_for_user])

# print(mean_rating_by_user_list[:5])
mean_rating_by_user_array = np.array(mean_rating_by_user_list, dtype=np.float32)
# print(mean_rating_by_user_array[:5])
# print(mean_rating_by_user_array.shape)