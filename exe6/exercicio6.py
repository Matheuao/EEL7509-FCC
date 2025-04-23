"""
Escreva um código que receba os valores dos coeficientes de um
polinônimo de segunda ordem 𝑓(𝑥) = 𝑎𝑥 2 + 𝑏𝑥 + 𝑐 e calcule as suas raízes
usando o método solve do SymPy. Além disso, seu código deve calcular
analiticamente o valor de mínimo ou máximo de 𝑓(𝑥), fazendo as derivadas
necessárias para tal (primeira derivada para encontrar pontos críticos e segunda
derivada para determinar se trata-se de um mínimo ou máximo). Todos os
cálculos necessários devem ser feitos usando o SymPy. Para verificar os
resultados, faço um gráfico com a curva de 𝑓(𝑥), as raízes do polinômio, e os
pontos de mínimo ou máximo encontrados.
"""

import sympy as smp
import numpy as np
import matplotlib.pyplot as plt

def solve_quadratic_function(a,b,c):
    
    x = smp.symbols('x')
    f = a*x**2 + b*x + c

    f_diff = smp.diff(f, x)
    f_diff2 = smp.diff(f_diff, x)

    # Encontrar ponto crítico
    critical_points = smp.solve(f_diff, x)
    critical_point = critical_points[0] if critical_points else None

    # Classificar ponto crítico
    type = "inconclusivo"
    if critical_point is not None:
        second_deriv_at_cp = f_diff2.subs(x, critical_point)
        if second_deriv_at_cp > 0:
            type = "mínimo"
        elif second_deriv_at_cp < 0:
            type = "máximo"


    roots = smp.solve(f, x)

   
    print("\nFunção f(x):", f)
    print("Raízes da função:", roots)
    print("Ponto crítico:", critical_point)
    print("Tipo do ponto crítico:", type)
    if critical_point is not None:
        print("Valor de f(x) no ponto crítico:", f.subs(x, critical_point))

    f_lambdified = smp.lambdify(x, f, 'numpy')

    # Gerar valores para o gráfico
    x_vals = np.linspace(float(critical_point)-10, float(critical_point)+10, 400) if critical_point else np.linspace(-10, 10, 400)
    y_vals = f_lambdified(x_vals)

    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, label='f(x)', color='blue')
    
    # marcar as raizes
    for r in roots:
        if r.is_real:
            r_val = float(r)
            plt.plot(r_val, 0, 'ro', label='Raiz' if r == roots[0] else "")

    # Marcar ponto crítico
    if critical_point is not None:
        cp_x = float(critical_point)
        cp_y = float(f.subs(x, critical_point))
        plt.plot(cp_x, cp_y, 'go', label=f'{type.title()} local')

    plt.axhline(0, color='black', linewidth=0.5)
    plt.title('Gráfico de f(x), raízes e ponto crítico')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.legend()
    plt.show()


a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

solve_quadratic_function(a,b,c)