import sys
import math

[a, b, c] = [int(x) for x in sys.stdin.readline().split()]
delta = b**2 - 4*a*c

if delta < 0:
    print("NO SOLUTION")
elif delta == 0:
    x0 = -b/(2*a)
    print('{0:.{1}f}'.format(x0, 2))
else:
    x1 = (-b - math.sqrt(delta))/(2*a)
    x2 = (-b + math.sqrt(delta))/(2*a)
    print('{0:.{1}f}'.format(x1, 2), '{0:.{1}f}'.format(x2, 2))

