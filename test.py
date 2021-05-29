from Biblioteki import color_generator, point_generator
import matplotlib.pyplot as plt
import math


punkty = generate_point([5, 5], 4, 20)

plt.scatter(x=[punkt[0] for punkt in punkty], y=[punkt[1] for punkt in punkty])
plt.show()
