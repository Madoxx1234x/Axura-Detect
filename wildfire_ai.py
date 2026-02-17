import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# temperature, humidity, wind_speed, forest_size
X = np.array([
    [35, 20, 30, 500],
    [25, 60, 10, 200],
    [40, 15, 35, 700],
    [30, 50, 15, 300],
    [45, 10, 40, 800],
    [28, 70, 5, 100],
    [38, 18, 28, 600],
    [32, 45, 20, 400],
    [42, 12, 37, 750],
    [27, 65, 8, 150],
    [36, 22, 33, 550],
    [29, 55, 12, 250],
    [41, 14, 36, 720],
    [31, 48, 18, 350],
    [44, 11, 39, 780],
    [26, 68, 7, 120],
    [37, 19, 32, 580],
    [33, 50, 22, 380],
    [43, 13, 38, 760],
    [30, 52, 16, 330],
])

y = np.array([
    1, 0, 1, 0, 1, 0, 
    1, 0, 1, 0, 
    1, 0, 1, 0, 1, 0, 
    1, 0, 1, 0
])

model = Sequential([
    Dense(16, activation='relu', input_shape=(4,)),
    Dense(8, activation='relu'),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy')
model.fit(X, y, epochs=100, verbose=0)

def predict_wildfire(data):
    input_data = np.array([[
        data["temperature"],
        data["humidity"],
        data["wind_speed"],
        data["forest_size"]
    ]])
    return float(model.predict(input_data)[0][0])
