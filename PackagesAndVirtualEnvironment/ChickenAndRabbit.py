from sympy import Symbol, solve

x = Symbol('chicken')
y = Symbol('rabbit')

total_heads = 35
total_feets = 94

eq1 = x + y - total_heads
eq2 = 2*x + 4*y - total_feets
solution = solve((eq1, eq2), (x, y)) #solution is a dictionary
"""
eq1: x+y-35=0
eq2: 2x+4y-94=0
solve((eq1, eq2,...,eqn), (sbl1, sbl2,...,sbln))
"""

print('The number of chicken:',solution[x])
print('The number of rabbits:',solution[y])

print(type(solution)) #Check what type 'solution' is