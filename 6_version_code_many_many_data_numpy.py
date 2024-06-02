import numpy as np

ih_wgt = np.array([
    [0.1, 0.2, -0.1], # hid[0]
    [-0.1, 0.1, 0.9], # hid[1]
    [0.1, 0.4, 0.1] # hid[2]
]).T

hp_wgt = np.array([
    [0.3, 1.1, -0.3], # Травмы?
    [0.1, 0.2, 0.0], # Победа?
    [0.0, 1.3, 0.1] # Печаль?
]).T

weights = [ih_wgt, hp_wgt]

def neural_network(inputs, weights):
    hid = inputs.dot(weights[0])
    pred = hid.dot(weights[1])
    return pred

toes = [8.5, 9.5, 9.9, 9.0]
wlrec = [0.65, 0.8, 0.8, 0.9]
nfans = [1.2, 1.3, 0.5, 1.0]

inputs = [toes[0], wlrec[0], nfans[0]]
pred = neural_network(inputs=inputs, weights=weights)

print(pred)