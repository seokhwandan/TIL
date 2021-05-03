import tensorflow as tf
import pandas as pd

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

cnt = 0
all_data = []
while cnt < len(nums):
    c = {}
    c['time'] = cnt + 1
    c['num'] = nums[cnt]
    all_data.append(c)
    cnt += 1

print(all_data)

df = pd.DataFrame(all_data)
df.to_csv('./nums.csv', index=False)
# print(df)

iv = df[['time']]
dv = df[['num']]

X = tf.keras.layers.Input(shape=[1])
Y = tf.keras.layers.Dense(1)(X)
model = tf.keras.models.Model(X, Y)
model.compile(loss='mse')

model.fit(iv, dv, epochs=10000, verbose=0)
print(model.predict(iv))
print(model.predict([[10]]))