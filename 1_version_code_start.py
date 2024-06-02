weights = [0.1, 0.2, 0]

def w_sum(a, b):
    assert(len(a) == len(b)) # это булевы выражения, которые проверяют, является ли условие истинным (True).
    output = 0

    for i in range(len(a)):
        output += (a[i] * b[i])

    return output


def neural_network(inputs, weights):
    pred = w_sum(inputs, weights)
    return pred


toes = [8.5, 9.5, 9.9, 9.0] # Среднее число игр
wlrec = [0.65, 0.8, 0.8, 0.9] # Текущая доля игр, окончившихся победой (процент)
nfans = [1.2, 1.3, 0.5, 1.0] # Число болельщиков (в миллионах)

inputs = [toes[0], wlrec[0], nfans[0]]
pred = neural_network(inputs=inputs, weights=weights)
print(pred)
