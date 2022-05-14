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
axes[0].title.set_text(r'model: $0.2 x$')

Y2 = 1.2 * x
axes[1].plot(x, Y2, color='r')
axes[1].scatter(data=d, x="x", y="y")
axes[1].axis(xmin=0,xmax=10,ymin=0,ymax=18)
axes[1].title.set_text(r'model: $1.2 x$')