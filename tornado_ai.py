import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# wind_shear, pressure, temp_gradient
X = np.array([
    [30, 980, 20],
    [5, 1015, 2],
    [40, 970, 25],
    [10, 1005, 5],
    [35, 960, 30],
    [3, 1020, 1],
    [25, 985, 18],
    [8, 1010, 4],
    [38, 965, 28],
    [12, 1002, 6],
    [32, 975, 22],
    [6, 1012, 3],
    [28, 982, 19],
    [9, 1008, 5],
    [36, 968, 26],
    [15, 1000, 8],
    [34, 970, 24],
    [4, 1018, 2],
    [31, 978, 21],
    [7, 1011, 4],
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

def predict_tornado(data):
    try:
        ws = data.get("wind_shear", 0)
        p = data.get("pressure", 1013)
        tg = data.get("temp_gradient", 0)
        input_data = np.array([[ws, p, tg]])
        return float(model.predict(input_data)[0][0])
    except Exception:
        return 0.0
