import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# magnitude, depth, historical_events
X = np.array([
    [6.5, 10, 50],
    [3.0, 30, 5],
    [7.0, 8, 70],
    [4.0, 40, 10],
    [6.8, 12, 60],
    [2.5, 50, 2],
    [6.0, 15, 45],
    [3.5, 35, 8],
    [7.2, 7, 75],
    [4.5, 38, 12],
    [6.9, 11, 65],
    [2.8, 48, 3],
    [6.3, 13, 55],
    [3.2, 32, 6],
    [7.1, 9, 72],
    [4.2, 42, 9],
    [6.7, 14, 62],
    [3.1, 36, 7],
    [6.4, 10, 58],
    [3.8, 34, 10],
])

y = np.array([
    1, 0, 1, 0, 1, 0,
    1, 0, 1, 0, 1, 0,
    1, 0, 1, 0, 1, 0,
    1, 0
])

model = Sequential([
    Dense(16, activation='relu', input_shape=(3,)),
    Dense(8, activation='relu'),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy')
model.fit(X, y, epochs=100, verbose=0)

def predict_earthquake(data):
    input_data = np.array([[
        data["magnitude"],
        data["depth"],
    ]])
    return float(model.predict(input_data)[0][0])
