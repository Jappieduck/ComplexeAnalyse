import numpy as np
import math
import random


def a(p1, p2, var):
    f = []
    (x, y) = p1
    (u, v) = p2
    p = (x + u) / 2
    q = (y + v) / 2
    m = (y - v) / (x - u)
    for val in var:
        f.append((-1 / m) * (val - p) + q)
    return f


def b(r):
    theta = np.linspace(0, np.pi)
    var = []
    fup = []
    flow = []
    for t in theta:
        var.append(np.cos(t))
        fup.append(np.sin(t))
        flow.append(np.sin(-t))
    return fup, flow, var


def c(x):
    f = []
    for val in x:
        f.append(3)
    return f


def e(p1,p2, x):
    (a,b) = p1
    (u,v) = p2
    f = []
    for val in x:
        f.append(a*val/b - u/b)
    f = np.asarray(f)
    return f


def f():
    yp1 = []
    ym1 = []
    yp2 = []
    ym2 = []
    x1 = np.linspace(-0.5, 0.5)
    x2 = np.linspace(0.5, 20)
    for val in x1:
        yp1.append(math.sqrt(2*val+1))
        ym1.append(-math.sqrt(2*val+1))
    for val in x2:
        yp2.append(math.sqrt(2*val+1))
        ym2.append(-math.sqrt(2*val+1))
    return yp1, yp2, ym1, ym2, x1, x2


def g(x):
    c = random.uniform(-5,5)
    f = []
    for val in x:
        f.append(c)
    return f, c