def f(x,y):
    if x > y or x == 28 or x == 36: return 0
    elif x == y: return 1
    else: return f(x+1,y) + f(x+5,y) + f(x*3,y)
print(f(2,18) * f(18,49) + f(2,30) * f(30,49) - f(2,18) * f(18,30)* f(30,49))