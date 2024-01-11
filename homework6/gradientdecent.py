import numpy as np

def df(f, p, k, step=1e-6):
    p1 = p.copy()
    p1[k] = p[k] + step
    return (f(p1) - f(p)) / step

def grad(f, p):
    gp = np.zeros_like(p, dtype=float)
    for k in range(len(p)):
        gp[k] = df(f, p, k)
    return gp

def gradient_descent(f, initial_point, learning_rate=0.01, epsilon=1e-6, max_iterations=1000):
    current_point = np.array(initial_point, dtype=float)
    
    for i in range(max_iterations):
        gradient = grad(f, current_point)
        current_point -= learning_rate * gradient
        
       
        if np.linalg.norm(gradient) < epsilon:
            print(f"Converged after {i+1} iterations.")
            break
    
    return current_point
    
def vector_function(p):
    return np.sum(np.square(p))

initial_point = np.array([1.0, 2.0])

learning_rate = 0.1

result = gradient_descent(vector_function, initial_point, learning_rate)

print("Optimal point:", result)
print("Optimal value:", vector_function(result))

