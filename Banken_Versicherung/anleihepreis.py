import matplotlib.pyplot as plt
import numpy as np

C = 50
r = 0.04
n = 5
F = 1000

C = 40
r = 0.04
n = 5
F = 1000

Anleihepreis = C * ((1-(1+r) ** -n) / r) + F/((1+r) ** n)

valsJ = []
valsJ2 = []
valsZ = []
valsComb = []
for i in range(1, 11):
    valsJ.append(C * ((1 - (1 + r) ** -i) / r) + F / ((1 + r) ** i))

for i in range(1, 11):
    r = 0.1 * i
    valsZ.append(C * ((1-(1+r) ** -n) / r) + F/((1+r) ** n))


for i in range(1, 11):
    r = 0.1 * i
    valsComb.append(C * ((1 - (1 + r) ** -i) / r) + F / ((1 + r) ** i))


# for i in range(1, 11):
#     valsJ2.append(C * ((1 - (1 + r) ** -i) / r) + F / ((1 + r) ** i))

print(f"Anleihepreis: {Anleihepreis}")

x = np.linspace(1, 10, 10)

print(valsJ)
# print(x)
plt.scatter(x, valsJ)
plt.plot(x, valsJ)
plt.title("Diskontierung: 0.04, Zinssatz: 0.04")
# plt.scatter(x, valsZ)
# plt.plot(x, valsZ)
# plt.scatter(x, valsComb)
# plt.plot(x, valsComb)
# plt.scatter(x, valsJ2)
# plt.plot(x, valsJ2)
plt.show()