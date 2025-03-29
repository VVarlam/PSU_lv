import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(open("mtcars.csv", "rb"), usecols=(1,2,3,4,5,6),
delimiter=",", skiprows=1)

mpg = data[:, 0]
hp = data[:, 3]
wt = data[:, 5]

plt.scatter(hp, mpg, s=wt*20, color='blue', alpha=0.6, edgecolors='black')
plt.xlabel('Konjske snage (hp)')
plt.ylabel('Potrosnja goriva (mpg)')
plt.title('Ovisnost potrosnje goriva o konjskim snagama')
plt.grid(True)
plt.show()

print(np.min(mpg))
print(np.max(mpg))
print(np.mean(mpg))

cyl = data[:, 1]
mpg_cyl6 = mpg[cyl == 6.0]
print(np.min(mpg_cyl6))
print(np.max(mpg_cyl6))
print(np.mean(mpg_cyl6))