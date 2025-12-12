import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import math as math
from matplotlib.patches import Circle

freq = 50
T=1/freq
modVa, modVb, modVc = 5, 5, 5 #RMS values
angVa, angVb, angVc = 90, -30, -150
x=np.linspace(0, T, 100)

polar2cart = lambda mod, ang: (np.cos(math.radians(ang))*mod, np.sin(math.radians(ang))*mod)
polar2senoide = lambda mod, ang: np.cos(2*np.pi*freq*x+math.radians(ang))*mod

QUIVER_OPTS = dict(
    angles="xy",
    scale=1,
    scale_units="xy"
)

fig, ax = plt.subplots(3, 3, constrained_layout=True)
ax[0,0].set_xlim(-10,10)
ax[0,0].set_ylim(-10,10)
ax[0,0].axvline(0, color="k", lw=0.2)
ax[0,0].axhline(0, color="k", lw=0.2)
ax[0,0].set_aspect("equal")
Va=ax[0,0].quiver(0, 0, *polar2cart(modVa, angVa), **QUIVER_OPTS, color="blue")
Vb=ax[0,0].quiver(0, 0, *polar2cart(modVb, angVb), **QUIVER_OPTS, color="green")
Vc=ax[0,0].quiver(0, 0, *polar2cart(modVc, angVc), **QUIVER_OPTS, color="red")

ax[0,1].set_xlim(-10,10)
ax[0,1].set_ylim(-10,10)
ax[0,1].axvline(0, color="k", lw=0.2)
ax[0,1].axhline(0, color="k", lw=0.2)
ax[0,1].set_aspect("equal")

Vax, Vay = polar2cart(modVa, angVa)
Vbx, Vby = polar2cart(modVb, angVb)
Vcx, Vcy = polar2cart(modVc, angVc)

Va_animado=ax[0,1].quiver(0, 0, Vax, Vay, **QUIVER_OPTS, color="blue")
Vb_animado=ax[0,1].quiver(0, 0, Vbx, Vby, **QUIVER_OPTS, color="green")
Vc_animado=ax[0,1].quiver(0, 0, Vcx, Vcy, **QUIVER_OPTS, color="red")
u_suma_abc_animado = sum(np.array(polar2cart(mod, ang))[0] for mod, ang in [(modVa, angVa), (modVb, angVb), (modVc, angVc)])
v_suma_abc_animado = sum(np.array(polar2cart(mod, ang))[1] for mod, ang in [(modVa, angVa), (modVb, angVb), (modVc, angVc)])
V_suma_abc_animado=ax[0,1].quiver(0, 0, u_suma_abc_animado, v_suma_abc_animado, **QUIVER_OPTS, color="lightblue")
circle1 = Circle((0, 0), modVa, fill=False, color="grey", lw=0.2)
circle2 = Circle((0, 0), 7.5, fill=False, color="grey", lw=0.2)
ax[0, 1].add_patch(circle1)
ax[0, 1].add_patch(circle2)

ax[0,2].set_xlim(0, T)
ax[0,2].set_ylim(-10, 10)

lineVa, = ax[0,2].plot(x, polar2senoide(modVa, angVa), color="blue")
lineVb, = ax[0,2].plot(x, polar2senoide(modVb, angVb), color="green")
lineVc, = ax[0,2].plot(x, polar2senoide(modVc, angVc), color="red")
ax[0,2].set_ylim(-10,10)

alphax = 2/3*(Vax+Vbx*-0.5+Vcx*-0.5)
alphay = 2/3*(Vay+Vby*-0.5+Vcy*-0.5)
betax = 2/3*(Vbx*(math.sqrt(3)/2)+Vcx*(-math.sqrt(3)/2))
betay = 2/3*(Vby*(math.sqrt(3)/2)+Vcy*(-math.sqrt(3)/2))

ax[1,0].set_xlim(-10,10)
ax[1,0].set_ylim(-10,10)
ax[1,0].axvline(0, color="k", lw=0.2)
ax[1,0].axhline(0, color="k", lw=0.2)
ax[1,0].set_aspect("equal")
ax[1,0].quiver(0, 0, alphax, alphay, **QUIVER_OPTS, color="purple")
ax[1,0].quiver(0, 0, betax, betay, **QUIVER_OPTS, color="orange")

ax[1,1].set_xlim(-10,10)
ax[1,1].set_ylim(-10,10)
ax[1,1].axvline(0, color="k", lw=0.2)
ax[1,1].axhline(0, color="k", lw=0.2)
ax[1,1].set_aspect("equal")

alpha=ax[1,1].quiver(0, 0, alphax, alphay, **QUIVER_OPTS, color="purple")
beta=ax[1,1].quiver(0, 0, betax, betay, **QUIVER_OPTS, color="orange")
suma_alpha_beta_animado = ax[1,1].quiver(0, 0, 0, 0, **QUIVER_OPTS, color="lightblue")

ax[1,2].set_xlim(0, T)
ax[1,2].set_ylim(-10, 10)
linealpha, = ax[1,2].plot(x, polar2senoide(math.hypot(alphax, alphay), 90), color="purple")
linebeta, = ax[1,2].plot(x, polar2senoide(math.hypot(betax, betay), 0), color="orange")

ax[2,1].set_xlim(-10,10)
ax[2,1].set_ylim(-10,10)
ax[2,1].axvline(0, color="k", lw=0.2)
ax[2,1].axhline(0, color="k", lw=0.2)
ax[2,1].set_aspect("equal")


vec_d = ax[2,1].quiver(0,0,5,0,**QUIVER_OPTS, color='tomato')
vec_q = ax[2,1].quiver(0,0,0,5, **QUIVER_OPTS, color='pink')
ax[2,2].set_xlim(0, T)
ax[2,2].set_ylim(-10, 10)
lineD, = ax[2,2].plot(x, np.full_like(x, 5), color="tomato")

ax[2,0].axis("off")
for i in range(0,3):
    for c in range(0,3):
        ax[c,i].set_xticks([])
        ax[c,i].set_yticks([])

ax[0,0].set_ylabel("abc", rotation=0, labelpad=15)
ax[1,0].set_ylabel(r'$\alpha\beta$',rotation=0, labelpad=15)
ax[2,1].set_ylabel("dq",rotation=0, labelpad=15)

def update(frame):
    angulo = frame/200*360
    lineVa.set_ydata(polar2senoide(modVa, angVa+angulo))
    lineVb.set_ydata(polar2senoide(modVa, angVb+angulo))
    lineVc.set_ydata(polar2senoide(modVa, angVc+angulo))

    Va_animado.set_UVC(*polar2cart(np.cos(math.radians(angVa+angulo))*modVa, angVa))
    Vb_animado.set_UVC(*polar2cart(np.cos(math.radians(angVb+angulo))*modVb, angVb))
    Vc_animado.set_UVC(*polar2cart(np.cos(math.radians(angVc+angulo))*modVc, angVc))

    u = sum(np.array(polar2cart(mod, ang))[0] for mod, ang in [(np.cos(math.radians(angVa+angulo))*modVa, angVa), 
                                    (np.cos(math.radians(angVb+angulo))*modVb, angVb), (np.cos(math.radians(angVc+angulo))*modVc, angVc)])
    v = sum(np.array(polar2cart(mod, ang))[1] for mod, ang in [(np.cos(math.radians(angVa+angulo))*modVa, angVa), 
                                    (np.cos(math.radians(angVb+angulo))*modVb, angVb), (np.cos(math.radians(angVc+angulo))*modVc, angVc)])
    V_suma_abc_animado.set_UVC(u, v)

    linealpha.set_ydata(polar2senoide(math.hypot(alphax, alphay), 90+angulo))
    linebeta.set_ydata(polar2senoide(math.hypot(betax, betay), 0+angulo))

    alpha.set_UVC(*polar2cart(np.cos(math.radians(90+angulo))*math.hypot(alphax, alphay), 90))
    beta.set_UVC(*polar2cart(np.cos(math.radians(0+angulo))*math.hypot(betax, betay), 0))

    u2 = sum(np.array(polar2cart(mod, ang))[0] for mod, ang in [(np.cos(math.radians(90+angulo))*math.hypot(alphax, alphay), 90), 
                                    (np.cos(math.radians(0+angulo))*math.hypot(betax, betay), 0)])
    v2 = sum(np.array(polar2cart(mod, ang))[1] for mod, ang in [(np.cos(math.radians(90+angulo))*math.hypot(alphax, alphay), 90), 
                                    (np.cos(math.radians(0+angulo))*math.hypot(betax, betay), 0)])
    
    suma_alpha_beta_animado.set_UVC(u2, v2)

    theta = 2 * np.pi * frame / 200  # gira 0 → 2π en 200 frames

    # Vector D
    u3d = 5 * np.cos(theta)
    v3d = -5 * np.sin(theta)
    vec_d.set_UVC(u3d, v3d)

    # Vector Q (90° respecto a D)
    u3q = 5 * np.cos(theta - np.pi/2)
    v3q = -5 * np.sin(theta - np.pi/2)
    vec_q.set_UVC(u3q, v3q)



    
    return lineVa, lineVb, lineVc, Va_animado, Vb_animado, Vc_animado, 
V_suma_abc_animado, linealpha, linebeta, alpha, beta, suma_alpha_beta_animado, vec_d, vec_q





ani = FuncAnimation(fig, update, frames=200, interval=20)



plt.show()