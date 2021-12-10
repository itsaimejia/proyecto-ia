from os import pardir
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


edad = ctrl.Antecedent(np.arange(0,76,1),'edad')
imc = ctrl.Antecedent(np.arange(18,41,1),'imc')

paro_cardiaco = ctrl.Consequent(np.arange(0,101,1),'paro cardiaco')

edad['menor'] = fuzz.trapmf(edad.universe, [0,5,10,17])
edad['joven'] = fuzz.trimf(edad.universe,[15,25,35])
edad['mayor'] = fuzz.trapmf(edad.universe, [30,45,60,75])
edad.view()
imc['normal'] =  fuzz.trapmf(imc.universe, [19,22,24,26])
imc['sobrepeso'] = fuzz.trimf(imc.universe, [24,30,36])
imc['obesidad'] = fuzz.trapmf(imc.universe,[34,36,38,40])

paro_cardiaco['bajo'] = fuzz.trapmf(paro_cardiaco.universe,[1,10,30,40])
paro_cardiaco['medio'] = fuzz.trimf(paro_cardiaco.universe,[35,60,80])
paro_cardiaco['alto'] = fuzz.trapmf(paro_cardiaco.universe, [70,80,90,101])


# cs = ctrl.controlsystem(rules)

# sim = ctrl.ControlSystemSimulation(cs)

# sim.input['edad'] = int(input("Edad: "))