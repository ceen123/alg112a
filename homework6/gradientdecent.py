def vecfunc(p):
    return sum(x**2 for x in p)

def grad_desc(f, init_pt, lr=0.01, eps=1e-6, max_iter=1000):
    pt = list(init_pt)
    
    for i in range(max_iter):
        grad = [2 * x for x in pt]
        pt = [x - lr * g for x, g in zip(pt, grad)]
        
        if all(abs(g) < eps for g in grad):
            break

    return pt

init_pt = [1.0, 2.0]
lr = 0.1

result = grad_desc(vecfunc, init_pt, lr)

print("Optimal point:", result)
print("Optimal value:", vecfunc(result))
