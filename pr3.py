import numpy as np

# Definiramo funkciju
def f(x):
    return x**2

# Trapezno pravilo
def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n  # širina podintervala
    x = np.linspace(a, b, n+1)  # točke podjele
    y = f(x)  # vrijednosti funkcije na tim točkama
    return h * (np.sum(y) - 0.5 * (y[0] + y[-1]))

# Parametri
a = 0  # početna točka
b = 1  # krajnja točka
n = 100  # broj podintervala

# Izračun
integral = trapezoidal_rule(f, a, b, n)
print("Aproksimacija integrala funkcije f(x) = x^2 je:", integral)
