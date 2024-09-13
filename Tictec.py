import math

def sigmoid(x, lambda_):
    return 1 / (1 + math.exp(-lambda_ * x))

def compute_neuron_output(x0, x1, weights, lambda_):
    w0, w1, w2 = weights
    g_x = w0 * x0 + w1 * x1 + w2
    return round(sigmoid(g_x, lambda_))

def main():
    # Parâmetros para AND
    weights_and = [-2, -2, 3]
    lambda_and = -3
    
    # Parâmetros para OR
    weights_or = [2, 2, -1]
    lambda_or = 3
    
    # Lendo as entradas
    inputs = []
    for _ in range(4):
        x0, x1 = map(int, input().split())
        inputs.append((x0, x1))
    
    # Calculando e exibindo os resultados
    for x0, x1 in inputs:
        and_output = compute_neuron_output(x0, x1, weights_and, lambda_and)
        or_output = compute_neuron_output(x0, x1, weights_or, lambda_or)
        print(and_output, or_output)

if __name__ == "__main__":
    main()
