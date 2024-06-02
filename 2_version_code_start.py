import numpy as np

weights = np.array([0.1, 0.2, 0])

def neural_network(inputs, weights):
    pred = inputs.dot(weights)
    return pred


toes = np.array([8.5, 9.5, 9.9, 9.0]) # Среднее число игр
wlrec = np.array([0.65, 0.8, 0.8, 0.9]) # Текущая доля игр, окончившихся победой (процент)
nfans = np.array([1.2, 1.3, 0.5, 1.0]) # Число болельщиков (в миллионах)

inputs = np.array([toes[0], wlrec[0], nfans[0]])
pred = neural_network(inputs=inputs, weights=weights)
print(pred)
