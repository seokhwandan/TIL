# 히든레이어

# 라이브러리 사용
import tensorflow as tf
import pandas as pd

# 과거 데이터 준비
파일경로 = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/boston.csv'
데이터 = pd.read_csv(파일경로)

# 독립변수, 종속변수 분리

독립 = 데이터[['crim', 'zn', 'indus', 'chas', 'nox', 'rm', 'age', 'dis', 'rad', 'tax', 'ptratio', 'b', 'lstat']]
종속 = 데이터[['medv']]

# print(독립.shape, 종속.shape)

# 모델의 구조 만들기
X = tf.keras.layers.Input(shape=[13])
H = tf.keras.layers.Dense(10, activation='swish')(X)
Y = tf.keras.layers.Dense(1)(H)
model = tf.keras.models.Model(X, Y)
model.compile(loss='mse')

# print(model.summary())

# 데이터로 모델을 학습
model.fit(독립, 종속, epochs=1000, verbose=0)
model.fit(독립, 종속, epochs=10)

# 모델을 이용
print(model.predict(독립[:5]))
print(종속[:5])

# 모델의 수식 확인
model.get_weights()
print(model.get_weights())