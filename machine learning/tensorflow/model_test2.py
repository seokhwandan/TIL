# 분류

# 라이브러리 사용
import tensorflow as tf
import pandas as pd

# 과거 데이터 준비
파일경로 = 'https://raw.githubusercontent.com/blackdew/tensorflow1/master/csv/iris.csv'
아이리스 = pd.read_csv(파일경로)
# print(아이리스.head())

# 원핫인코딩
인코딩 = pd.get_dummies(아이리스)
# print(인코딩.head())
# print(인코딩.columns)

# 독립변수, 종속변수
독립 = 인코딩[['꽃잎길이', '꽃잎폭', '꽃받침길이', '꽃받침폭']]
종속 = 인코딩[['품종_setosa', '품종_versicolor', '품종_virginica']]
# print(독립.shape, 종속.shape)

# 모델의 구조 만들기
X = tf.keras.layers.Input(shape=[4])
Y = tf.keras.layers.Dense(3, activation='softmax')(X)
model = tf.keras.models.Model(X, Y)
model.compile(loss='categorical_crossentropy', metrics='accuracy')

# 모델 학습
model.fit(독립, 종속, epochs=100)

# 모델 이용
model.predict(독립[-5:])
# print(종속[-5:])
print(model.get_weights())