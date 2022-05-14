import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

sns.set_theme()

np.random.seed(0)
x = np.arange(0, 10, 0.1)
y = x**2 / 25 + x + np.random.normal(0, 1, len(x))

d = pd.DataFrame({"x": x, "y": y})

sns.scatterplot(data=d, x="x", y="y")


fig, axes = plt.subplots(1, 2, figsize=(8, 4), sharey=True)

Y1 = 0.2 * x
axes[0].plot(x, Y1, color='r')
axes[0].scatter(data=d, x="x", y="y")
axes[0].axis(xmin=0,xmax=10,ymin=0,ymax=18)
axes[0].title.set_text(r'model: $\hat{y} = 0.2 x$')

Y2 = 1.2 * x
axes[1].plot(x, Y2, color='r')
axes[1].scatter(data=d, x="x", y="y")
axes[1].axis(xmin=0,xmax=10,ymin=0,ymax=18)
axes[1].title.set_text(r'model: $\hat{y} = 1.2 x$')


np.random.seed(0)
x = np.concatenate([np.random.normal(0, 1, 50), np.random.normal(4, 0.5, 40), np.arange(0, 5, 0.1)])
y = np.concatenate([np.random.normal(8, 1, 50), np.random.normal(2, 1, 40), np.random.normal(-1, 0.2, 50)])

d = pd.DataFrame({"x": x, "y": y})

sns.scatterplot(data=d, x="x", y="y")


fig, axes = plt.subplots(1, 2, figsize=(8, 4), sharey=True)

circle1 = plt.Circle((3, 1), 4, alpha = 0.25, color = 'r')
circle2 = plt.Circle((0, 8), 3, alpha = 0.25, color = 'y')

axes[0].add_patch(circle1)
axes[0].add_patch(circle2)
axes[0].scatter(data=d, x="x", y="y")
axes[0].axis(xmin=-2,xmax=5,ymin=-2,ymax=12)
axes[0].title.set_text('2 clusters')

from matplotlib.patches import Ellipse

circle1 = plt.Circle((0, 8), 3, alpha = 0.25, color = 'y')
circle2 = plt.Circle((4, 2.5), 2.25, alpha = 0.25, color = 'r')
circle3 = Ellipse((2.5, -1), 5.5, 1.75, alpha = 0.25, color = 'g')

axes[1].add_patch(circle1)
axes[1].add_patch(circle2)
axes[1].add_patch(circle3)
axes[1].scatter(data=d, x="x", y="y")
axes[1].axis(xmin=-2,xmax=5,ymin=-2,ymax=12)
axes[1].title.set_text('3 clusters')

