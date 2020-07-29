import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
data = pd.read_csv('results.txt',header = None)
data[1].ix[(data[1] > 50000)] = 0
sns.lineplot(x = data[0], y = data[1])

plt.savefig('fig.png')
