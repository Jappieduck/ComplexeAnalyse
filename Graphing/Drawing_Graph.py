import Graphing.Generate_Random_Point
import Graphing.Function
import matplotlib.pyplot as plt
import numpy as np
import random

x = np.linspace(-20, 20)

p1 = Graphing.Generate_Random_Point.generate(2)
p2 = Graphing.Generate_Random_Point.generate(2)
(p1x, p1y) = p1
(p2x, p2y) = p2
while p2 == p1 or p1x == p2x or p1y == p2y:
    p2 = Graphing.Generate_Random_Point.generate(2)
    (p2x, p2y) = p2

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

# Eliminate upper and right axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Show ticks in the left and lower axes only
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.set_xticks([])
ax.set_yticks([])

plt.xlim([-12, 12])
plt.ylim([-12, 12])

y = Graphing.Function.a(p1, p2, x)
plt.plot(x, y, label='(a)')

(y1, y2, xc) = Graphing.Function.b(1)
plt.plot(xc, y1, color='purple', label='(b)')
plt.plot(xc, y2, color='purple')

y = Graphing.Function.c(x)
plt.plot(y, x, color='red', label='(c)')

c = random.randint(-5, 5)
ax.fill_between(range(c, len(x)), min(x), max(x), alpha=0.3, label='(d)')

p3 = Graphing.Generate_Random_Point.generate(2)
p4 = Graphing.Generate_Random_Point.generate(2)
(p3x, p3y) = p3
(p4x, p4y) = p4
while p4 == p3 or p1x == p2x or p1y == p2y or p3y == 0:
    p2 = Graphing.Generate_Random_Point.generate(2)
    (p2x, p2y) = p2
y = Graphing.Function.e(p1, p2, x)
ax.fill_between(x, -20, y, alpha=0.3, color='yellow', label='(e)')

y11, y12, y21, y22, xf1, xf2 = Graphing.Function.f()
plt.plot(xf1, y11, color='blue', label='(f)')
plt.plot(xf1, y21, color='blue')
plt.plot(xf2, y12, color='blue')
plt.plot(xf2, y22, color='blue')

y, c = Graphing.Function.g(x)
plt.plot(x, y, label='(g) met c=' + str(round(c, 3)))

(u, v) = p1
plt.plot(u, v, marker='o', color='black',
         label='Punt voor (b) met P=(' + str(round(u, 1)) + ',' + str(round(v, 1)) + ')')
(u, v) = p2
plt.plot(u, v, marker='o', color='black', label='Punt voor (b) met P=(' + str(round(u, 1)) + ',' + str(round(v, 1)) + ')')
(u, v) = p3
plt.plot(u, v, marker='o', color='green', label='Punt voor (e) met P=(' + str(round(u, 1)) + ',' + str(round(v, 1)) + ')')
(u, v) = p4
plt.plot(u, v, marker='o', color='green', label='Punt voor (e) met P=(' + str(round(u, 1)) + ',' + str(round(v, 1)) + ')')

plt.xlabel("Reële as", loc='right')
plt.title("Imaginaire as")

ax.set_aspect('equal', adjustable='box')

plt.legend(bbox_to_anchor=(-0.72, 1), loc='upper left', borderaxespad=0)
plt.show()
