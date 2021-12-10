import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

edad = np.arange(0,76,1)
manejo = np.arange(0,101,1)
riesgo = np.arange(0,101,1)

edad_joven = fuzz.trapmf(edad, [18,18,25,30])
edad_adulto = fuzz.trimf(edad, [20,35,50])
edad_mayor = fuzz.trapmf(edad, [40,60,70,70])

manejo_bajo= fuzz.trapmf(manejo,[0,0,10,20])
manejo_medio = fuzz.trimf(manejo, [10,40,50])
manejo_alto = fuzz.trapmf(manejo, [50,70,100,100])

riesgo_bajo = fuzz.trapmf(riesgo, [0,0,10,20])
riesgo_medio = fuzz.trimf(riesgo, [10,30,45])
riesgo_alto = fuzz.trapmf(riesgo, [40,55,100,100])

fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, figsize=(8, 9))

ax0.plot(edad, edad_joven, 'b', linewidth=1.5, label='Joven')
ax0.plot(edad, edad_adulto, 'g', linewidth=1.5, label='Adulto')
ax0.plot(edad, edad_mayor, 'r', linewidth=1.5, label='Mayor')
ax0.set_title('Edad')
ax0.legend()

ax1.plot(manejo, manejo_bajo, 'b', linewidth=1.5, label='Bajo')
ax1.plot(manejo, manejo_medio, 'g', linewidth=1.5, label='Medio')
ax1.plot(manejo, manejo_alto, 'r', linewidth=1.5, label='Alto')
ax1.set_title('Porcentaje manejo')
ax1.legend()

ax2.plot(riesgo, riesgo_bajo, 'b', linewidth=1.5, label='Bajo')
ax2.plot(riesgo, riesgo_medio, 'g', linewidth=1.5, label='Medio')
ax2.plot(riesgo, riesgo_alto, 'r', linewidth=1.5, label='Alto')
ax2.set_title('Porcentaje riesgo')
ax2.legend()

plt.show()