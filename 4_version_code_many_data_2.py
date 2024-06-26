weights = [
    [0.1, 0.1, -0.3], # Травмы?
    [0.1, 0.2, 0.0], # Победа?
    [0.0, 1.3, 0.1]  # Печаль?
]

def w_sum(a, b):
    assert(len(a) == len(b))
    output = 0

    for i in range(len(a)):
        output += (a[i] * b[i])

    return output


def  vect_mat_mul(vect, matrix):
    assert(len(vect) == len(matrix))
    output = [0, 0, 0]

    for i in range(len(vect)):
        output[i] = w_sum(vect, matrix[i])

    return output


def neural_network(inputs, weirhts):
    pred = vect_mat_mul(inputs, weights)
    return pred

toes = [8.5, 9.5, 9.9, 9.0]
wlrec = [0.65, 0.8, 0.8, 0.9]
nfans = [1.2, 1.3, 0.5, 1.0]

inputs = [toes[0], wlrec[0], nfans[0]]
pred = neural_network(inputs=inputs, weirhts=weights)

print(pred)