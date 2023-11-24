import random

def hillClimbing(f, x, y, h=0.001):
    failCount = 0                    
    while (failCount < 10000):       
        fxy = f(x, y)                
        dx = random.uniform(-h, h)   
        dy = random.uniform(-h, h)   
        if f(x+dx, y+dy) >= fxy:     
            x = x + dx               
            y = y + dy
            print('x={:.3f} y={:.3f} f(x,y)={:.3f}'.format(x, y, fxy))
            failCount = 0            
        else:                        
            failCount = failCount + 1
    return (x,y,fxy)                 

def f(x, y):
    return -1 * ( x*x -2*x + y*y +2*y - 2 )

hillClimbing(f, 0, 0)
