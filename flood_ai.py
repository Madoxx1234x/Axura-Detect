import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# rainfall, river_level, terrain_slope
X = np.array([
    [200, 8, 2],
    [50, 3, 10],
    [300, 9, 1],
    [100, 4, 8],
    [250, 10, 1],
    [30, 2, 12],
    [180, 7, 3],
    [60, 4, 9],
    [270, 9, 2],
    [120, 5, 7],
    [240, 10, 1],
    [40, 3, 11],
    [190, 8, 2],
    [80, 4, 8],
    [260, 9, 1],
    [110, 5, 7],
    [230, 10, 1],
    [35, 2, 12],
    [210, 8, 2],
    [70, 3, 9],
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
try:
    model.fit(X, y, epochs=5, verbose=0)
except Exception:
    pass

def predict_flood(data):
    try:
        r = data.get("rainfall", 0)
        rl = data.get("river_level", 0)
        s = data.get("terrain_slope", 0)
        input_data = np.array([[r, rl, s]])
        return float(model.predict(input_data)[0][0])
    except Exception:
        return 0.0