import pandas as pd
import matplotlib.pyplot as plt

file_path = "star_with_gravity.csv"
df = pd.read_csv(file_path)

mass_list = df['Mass'].to_list()
radius_list = df['Radius'].to_list()
gravity_list = df['Gravity'].to_list()

mass_list.sort()
radius_list.sort()
gravity_list.sort()


plt.figure()
plt.plot(mass_list, radius_list, marker='o', linestyle='-', color='b')
plt.xlabel('Mass')
plt.ylabel('Radius')
plt.title('Mass vs. Radius')
plt.grid(True)
plt.show()

plt.figure()
plt.scatter(mass_list, gravity_list, marker='o', color='g')
plt.xlabel('Mass')
plt.ylabel('Gravity')
plt.title('Mass vs. Gravity')
plt.grid(True)
plt.show()

plt.figure()
plt.plot(radius_list, gravity_list, marker='o', linestyle='--', color='r')
plt.xlabel('Radius')
plt.ylabel('Gravity')
plt.title('Radius vs. Gravity')
plt.grid(True)
plt.show()