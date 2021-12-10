from os import pardir
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


edad = ctrl.Antecedent(np.arange(0,76,1),'edad')
imc = ctrl.Antecedent(np.arange(18,41,0.1),'imc')

paro_cardiaco = ctrl.Consequent(np.arange(0,101,0.1),'paro-cardiaco')

edad['menor'] = fuzz.trapmf(edad.universe, [0,5,10,17])
edad['joven'] = fuzz.trimf(edad.universe,[15,25,35])
edad['mayor'] = fuzz.trapmf(edad.universe, [30,45,60,75])
edad.view()
imc['normal'] =  fuzz.trapmf(imc.universe, [19,22,24,26])
imc['sobrepeso'] = fuzz.trimf(imc.universe, [24,30,36])
imc['obesidad'] = fuzz.trapmf(imc.universe,[34,36,38,40])
imc.view()

paro_cardiaco['bajo'] = fuzz.trapmf(paro_cardiaco.universe,[1,10,30,40])
paro_cardiaco['medio'] = fuzz.trimf(paro_cardiaco.universe,[35,60,80])
paro_cardiaco['alto'] = fuzz.trapmf(paro_cardiaco.universe, [70,80,90,101])
paro_cardiaco.view()

reglas = []

reglas.append(ctrl.Rule(edad['menor'] & imc ['normal'], paro_cardiaco['bajo']))
reglas.append(ctrl.Rule(edad['menor'] & imc ['sobrepeso'], paro_cardiaco['bajo']))
reglas.append(ctrl.Rule(edad['menor'] & imc ['obesidad'], paro_cardiaco['medio']))

reglas.append(ctrl.Rule(edad['joven'] & imc ['normal'], paro_cardiaco['bajo']))
reglas.append(ctrl.Rule(edad['joven'] & imc ['sobrepeso'], paro_cardiaco['medio']))
reglas.append(ctrl.Rule(edad['joven'] & imc ['obesidad'], paro_cardiaco['alto']))

reglas.append(ctrl.Rule(edad['mayor'] & imc ['normal'], paro_cardiaco['medio']))
reglas.append(ctrl.Rule(edad['mayor'] & imc ['sobrepeso'], paro_cardiaco['alto']))
reglas.append(ctrl.Rule(edad['mayor'] & imc ['obesidad'], paro_cardiaco['alto']))


cs = ctrl.ControlSystem(reglas)

sim = ctrl.ControlSystemSimulation(cs)

sim.input['edad'] = int(input("Edad: "))
sim.input['imc'] = float(input("IMC: "))

sim.compute()
print(sim.output['paro-cardiaco'])