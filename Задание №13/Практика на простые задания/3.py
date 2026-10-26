def f(x,y):
    if x > y: return 0
    elif x == y: return 1
    else: return f(x+2,y) + f(x+3,y) + f(x*4,y)
print(f(5,21) * f(21,65) + f(5,41) * f(41, 65) - 2 * f(5,21) * f(21,41) * f(41,65))