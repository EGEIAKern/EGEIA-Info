def f(x,y):
    if x < y: return 0
    elif x == y: return 1
    else: return f(x-2,y) + f(x-3,y) + f(x//5,y)
print(f(63, 47) * f(47,3) + f(63,25) * f(25,3) - 2 * f(63,47)* f(47,25)*f(25,3))