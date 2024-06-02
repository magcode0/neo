weights = [.3, .2, .9]

def ele_mul(number, vector):
    output = [0, 0, 0]
    assert(len(output) == len(vector))

    for i in range(len(vector)):
        output[i] = number * vector[i]
    return output

def neural_network(inputs, weights):
    pred = ele_mul(inputs, weights)
    return pred

wlrec = [0.65, 0.8, 0.8, 0.9]
inputs = wlrec[0]
pred = neural_network(inputs, weights)
print(pred)