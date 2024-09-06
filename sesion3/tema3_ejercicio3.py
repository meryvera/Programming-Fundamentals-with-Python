# ARREGLOS MULTIDIMENSIONALES

import numpy as np

arreglo_multidimensionales = np.array([
  # Primer grupo
  [
    ["Nombre", "Edad"],
    ["Ana", 10],
    ["Jose", 20],
  ],
  # Segundo grupo
  [
    ["Nombre", "Edad"],
    ["Sofia", 30],
    ["Luis", 40]
  ]
])
print(arreglo_multidimensionales[1])
print(arreglo_multidimensionales[1][2])
print(arreglo_multidimensionales[1][2][0])