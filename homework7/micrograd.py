from micrograd.engine import Value

def vecfunc(p):
    return sum(Value(x)**2 for x in p)

def grad_desc(f, init_pt, lr=0.01, eps=1e-6, max_iter=1000):
    pt = [Value(x) for x in init_pt]
    
    for i in range(max_iter):
        output = f(pt)
        output.backward()
        
        grad = [x.grad for x in pt]
        pt = [Value(x.data - lr * g) for x, g in zip(pt, grad)]
        
        if all(abs(g) < eps for g in grad):
            break

    return [x.data for x in pt]

init_pt = [1.0, 2.0]
lr = 0.1

result = grad_desc(vecfunc, init_pt, lr)

print("Optimal point:", result)
print("Optimal value:", vecfunc(result))
