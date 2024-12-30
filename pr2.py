import numpy as np

# Definiramo funkciju
def f(x):
    return np.sin(x)

# Trapezno pravilo
def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n  # širina podintervala
    x = np.linspace(a, b, n+1)  # točke podjele
    y = f(x)  # vrijednosti funkcije na tim točkama
    return h * (np.sum(y) - 0.5 * (y[0] + y[-1]))

# Parametri
a = 0  # početna točka
b = np.pi  # krajnja točka
n = 100  # broj podintervala

# Izračun
integral = trapezoidal_rule(f, a, b, n)
print("Aproksimacija integrala funkcije f(x) = sin(x) je:", integral)
