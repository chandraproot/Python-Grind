import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy.integrate import odeint
from scipy.integrate import solve_ivp

def dvdt(t,v):
    return 3 *v **2 - 5
v0 = 0

t = np.linspace(0, 1, 100)
sol_m1 = odeint(dvdt, y0 = v0, t= t, tfirst=True)
sol_m2 = solve_ivp(dvdt, t_span=(0, max(t)), y0 = [v0], t_eval=t)


v_sol_m1 = sol_m1.T[0]
v_sol_m2 = sol_m2.y[0]

plt.plot(t, v_sol_m1)
plt.plot(t, v_sol_m2, '--')
plt.xlabel('$v(t)$', fontsize=15)
plt.ylabel('$t$', fontsize=22)
plt.show()